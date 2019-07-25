import csv
from elsy.mongo import mongo_db
from elsy.config import SEED_FILE
from flask.cli import with_appcontext
import click

@click.command('db:seed')
@with_appcontext
def seed():
    content = None
    with open(SEED_FILE) as fseed:
        csv_reader = csv.reader(fseed)
        content = [ _parse_row(row) for row in csv_reader ]
    mongo_db.node.insert_many(content)

def _parse_row(row):
    return {
        "nama": row[0],
        "jabatan": row[1],
        "alamat": row[2],
        "latitude": _dms_to_dd(row[3]),
        "longitude": _dms_to_dd(row[4])
    }

def _dms_to_dd(dms_str):
    degree, minute, second = dms_str.split("-")
    return float(degree) + (float(minute) / 60.0) + (float(second) / 3600.0)