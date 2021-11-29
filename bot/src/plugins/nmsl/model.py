from peewee import *

db = SqliteDatabase('my_database.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = BigIntegerField(unique=True, primary_key=True)


if __name__ == '__main__':
    db.connect()
    db.create_tables([User])
