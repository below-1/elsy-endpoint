from elsy.routes.blueprint import bp
from elsy.mongo import mongo_db, Node, Edge, get_edges_by_ids
from elsy.core import Graph, dijkstra, shortest_path_to, SimpleEdge, ElsyTSPABC
from flask import jsonify

@bp.route("/abc/<source>")
def abc_tsp(source):
    main_node_filter = {
        '$or': [
            {'jabatan': 'rt'},
            {'jabatan': 'rw'}
        ]
    }

    nodes = list(mongo_db.node.find(main_node_filter))
    inters = list(mongo_db.node.find({'jabatan': 'intersection'}))

    nodes = [str(n['_id']) for n in nodes]
    inters = [str(n['_id']) for n in inters]

    edges = list(mongo_db.edge.find())
    edges = [SimpleEdge.fromdict(e) for e in edges]

    # return jsonify(edges)
    abc = ElsyTSPABC(nodes, inters, edges)
    abc.calc_nodes_dist()
    route = abc.abc(nodes[0], n=10, limit=10)
    edges_ids = [ r._id for r in route ]

    edges = get_edges_by_ids(edges_ids)

    return jsonify(edges)