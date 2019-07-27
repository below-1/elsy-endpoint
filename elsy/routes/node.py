from flask import request, jsonify
from .blueprint import bp
from elsy.mongo import mongo_db, Node
from bson.objectid import ObjectId
import pprint

@bp.route("/nodes-delete-all", methods=["GET"])
def delete_all_nodes():
    mongo_db.node.delete_many({})
    return "OK"

@bp.route("/nodes", methods=["POST"])
def create_node():
    content = request.json
    node = Node.fromdict(content)
    result = mongo_db.node.insert_one(node.todict())
    pprint.pprint(result.inserted_id)
    return str(result.inserted_id)

@bp.route("/nodes/<id>", methods=["PUT"])
def update_node(id):
    _id = ObjectId(id)
    content = request.json
    _filter = {
        "_id": _id
    }
    _payload = {
        "$set": {
            **content
        }
    }
    update_result = mongo_db.node.find_one_and_update(_filter, _payload)
    return jsonify(update_result)

@bp.route("/nodes/<id>", methods=["DELETE"])
def delete_node(id):
    _id = ObjectId(id)

    _filter = {
        "_id": _id
    }
    # First we need to delete all edge connection to/from this node.
    delete_filter = {
      "$or": [
        { "aId": id },
        { "bId": id }
      ]
    }
    mongo_db.edge.delete_many(delete_filter)
    mongo_db.node.delete_one(_filter)
    return "OK"

@bp.route("/nodes", methods=["GET"])
def find_nodes():
    filter = {}

    if 'jabatan' in request.args:

        jabatan = request.args['jabatan']
        if jabatan == 'all':
            filter["$or"] = [
                {"jabatan": "rt"},
                {"jabatan": "rw"}
            ]
        elif jabatan == 'rw':
            filter["jabatan"] = "rw"
        elif jabatan == "rt":
            filter["jabatan"] = "rt"
        elif jabatan == "kl":
            filter["jabatan"] = "kl"
        elif jabatan == 'intersection':
            filter["jabatan"] = "intersection"


    results = list(mongo_db.node.find(filter))
    return jsonify(results)

@bp.route("/nodes/<id>", methods=["GET"])
def find_one_node(id):
    _id = ObjectId(id)
    _filter = {
        "_id": _id
    }
    return jsonify(mongo_db.node.find_one(_filter))