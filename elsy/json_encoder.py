from flask.json import JSONEncoder
from bson.objectid import ObjectId
from elsy.core import SimpleEdge

class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, SimpleEdge):
            return o.__dict__
        return JSONEncoder.default(self, o)