from elsy.config import MONGO_URI
from pymongo import MongoClient
from werkzeug.local import LocalProxy
from flask import g

client = MongoClient(MONGO_URI)

def _get_db():
    if "mongo_db" not in g:
        g.mongo_db = client.peta_kolhua
    return g.mongo_db

mongo_db = LocalProxy(_get_db)

Node_allowed_keys = ('_id', 'nama', 'jabatan', 'lokasiJabatan', 'alamat', 'latitude', 'longitude')
Edge_allowed_keys = ('_id', 'a', 'b', 'aId', 'bId', 'length')

class Node:
    def __init__(self, _id=None, nama=None, jabatan=None, lokasiJabatan=None, alamat=None, latitude=None, longitude=None):
        self._id = _id
        self.nama = nama
        self.jabatan = jabatan
        self.lokasiJabatan = lokasiJabatan
        self.alamat = alamat
        self.latitude = latitude
        self.longitude = longitude

    @classmethod
    def fromdict(cls, d):
        df = {k: v for k, v in d.items() if k in Node_allowed_keys}
        return cls(**df)

    def todict(self):
        items = ( (k, getattr(self, k)) for k in Node_allowed_keys)
        not_none = ( (k, v) for k, v in items if v is not None )
        return { k: v for k,v in not_none }

class Edge:
    def __init__(self, _id=None, aId=None, bId=None, a=None, b=None, length=None):
        self._id = _id
        self.aId = aId
        self.bId = bId
        self.a = a
        self.b = b
        self.length = length
    
    @classmethod
    def fromdict(cls, d):
        df = {k: v for k, v in d.items() if k in Edge_allowed_keys}
        return cls(**df)

    def todict(self):
        items = ( (k, getattr(self, k)) for k in Edge_allowed_keys)
        not_none = ( (k, v) for k, v in items if v is not None )
        return { k: v for k,v in not_none }

