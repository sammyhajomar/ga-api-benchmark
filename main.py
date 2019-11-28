from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os
import pandas as pd
from threading import Thread
from datetime import datetime
import time
from config import VIEW_ID
from model import DataModel
from peewee import fn


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = '{}/cred.json'.format(BASE_DIR)

""" Analytics Reporting API V4."""

def initialize_analytics_reporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
      An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics


def get_report(analytics, view_id):
    """Queries the Analytics Reporting API V4.

    Args:
      analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
      The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': view_id,
                    'dateRanges': [{
                        'startDate': "2019-01-01",
                        'endDate': "2019-10-31"}],
                    'metrics': [{'expression': 'ga:sessions'}, {'expression': 'ga:bounceRate'}],
                    'dimensions': [{'name': 'ga:date'}]
                }]
        }
    ).execute()


def print_response(response):
    """Parses and prints the Analytics Reporting API V4 response.
    Args:
      response: An Analytics Reporting API V4 response.
    """

    output = []
    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

        for row in report.get('data', {}).get('rows', []):
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])
            dict = {}
            for header, dimension in zip(dimensionHeaders, dimensions):
                dict[header] = dimension

            for i, values in enumerate(dateRangeValues):
                print('Date range: ' + str(i))
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    dict[metricHeader.get('name')] = value
            output.append(dict)
    return output


def to_db(output, vid):
    for row in output:
        data_model = DataModel(sessions=row['ga:sessions'], date=str(pd.to_datetime(row['ga:date'])), bounce_rate=row['ga:bounceRate'], view_id=vid)
        data_model.save()
    return


def main(vid):
    analytics = initialize_analytics_reporting()
    response = get_report(analytics, vid)
    output = print_response(response)
    to_db(output, vid)

    time.sleep(0.5)
    return


def queried_data():
    date_query = DataModel.select(DataModel.date).distinct().where(DataModel.view_id.in_(VIEW_ID))
    dates = [dq.date.strftime("%Y-%m-%d") for dq in date_query]

    results = []
    for date in dates:
        dm = DataModel.select(fn.SUM(DataModel.sessions).alias("sessions"), DataModel.date, fn.SUM(DataModel.bounce_rate).alias("bounce_rate")).where(DataModel.date == date).where(DataModel.view_id.in_(VIEW_ID))
        for d in dm:
            results.append({'date': d.date, 'sessions': d.sessions, 'sessions_avg': d.sessions//len(VIEW_ID), 'bounce_rate': d.bounce_rate//len(VIEW_ID)})
    return results


def to_dataframe():
    query = DataModel.select()
    return pd.DataFrame(list(query.dicts()))


def to_dataframe_v2():
    return pd.DataFrame(queried_data())


if __name__ == '__main__':
    for vid in VIEW_ID:
        worker = Thread(target=main, args=(vid, ))
        worker.start()
        worker.join()

    df = to_dataframe_v2()
    df.to_csv('{}/sheets/{}.csv'.format(BASE_DIR, 'sammy', vid), index=False)
    time.sleep(0.5)
    DataModel.drop_table()
