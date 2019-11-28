from peewee import *
import os

print(os.path.join(os.path.dirname(__file__), 'data1.db'))
db = SqliteDatabase(os.path.join(os.path.dirname(__file__), 'data1.db'))


class DataModel(Model):
	organic_sessions = CharField()
	date = DateTimeField()
	bounce_rate = CharField()
	view_id = CharField()

	class Meta:
		database = db


db.connect()
db.create_tables([DataModel])
