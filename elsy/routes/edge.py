from flask import request, jsonify
from .blueprint import bp
from elsy.mongo import mongo_db, Edge
from bson.objectid import ObjectId
import pprint

@bp.route("/edges-delete-all", methods=["GET"])
def delete_all_edges():
    mongo_db.edge.delete_many({})
    return "OK"

@bp.route("/edges", methods=["POST"])
def create_edge():
    content = request.json
    node = Edge.fromdict(content)
    result = mongo_db.edge.insert_one(node.todict())
    return str(result.inserted_id)

@bp.route("/edges/<id>", methods=["DELETE"])
def delete_edge(id):
    _id = ObjectId(id)
    _filter = {
        "_id": _id
    }
    del_result = mongo_db.edge.delete_one(_filter)
    return "OK"

@bp.route("/edges", methods=["GET"])
def find_edges():
    results = list(mongo_db.edge.find())
    return jsonify(results)