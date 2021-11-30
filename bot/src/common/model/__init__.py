import datetime
import re

from peewee import *

db = SqliteDatabase('../../../my_database.db')
# db = SqliteDatabase('my_database.db')


def make_table_name(model_class):
    model_name = model_class.__name__
    return re.sub(
        r'((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))', r'_\1',
        model_name).lower().lstrip("_")


class BaseModel(Model):
    class Meta:
        table_function = make_table_name
        database = db


class Account(BaseModel):
    id = IntegerField(unique=True, primary_key=True)
    qq = BigIntegerField(unique=True)
    amount = IntegerField(default=0)
    add_time = DateTimeField(default=datetime.datetime.now)


class TradingRecord(BaseModel):
    id = IntegerField(unique=True, primary_key=True)
    qq = BigIntegerField(unique=True)
    trading_type = IntegerField()
    amount = IntegerField()
    add_time = DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':
    db.connect()
    db.drop_tables([TradingRecord])
    db.create_tables([TradingRecord])
