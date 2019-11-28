from peewee import *
import os

print(os.path.join(os.path.dirname(__file__), 'data.db'))
db = SqliteDatabase(os.path.join(os.path.dirname(__file__), 'data.db'))


class DataModel(Model):
	sessions = CharField()
	date = DateTimeField()
	bounce_rate = CharField()
	view_id = CharField()

	class Meta:
		database = db


db.connect()
db.create_tables([DataModel])
