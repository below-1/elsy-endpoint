from elsy.routes.blueprint import bp
from elsy.mongo import mongo_db, Node, Edge, get_edges_by_ids
from elsy.core import Graph, dijkstra, shortest_path_to, shortest_path, SimpleEdge, ElsyTSPABC, edge_connected
from flask import jsonify

@bp.route("/dijkstra/<source>/<target>")
def dijkstra_route(source, target):
    main_node_filter = {
        '$or': [
            {'jabatan': 'rt'},
            {'jabatan': 'rw'}
        ]
    }

    nodes = list(mongo_db.node.find(main_node_filter))
    inters = list(mongo_db.node.find({'jabatan': 'intersection'}))

    nodes = [str(n['_id']) for n in nodes]

    assert source in nodes

    inters = [str(n['_id']) for n in inters]

    edges = list(mongo_db.edge.find())
    edges = [SimpleEdge.fromdict(e) for e in edges]

    # return jsonify(edges)
    abc = ElsyTSPABC(nodes, inters, edges)
    abc.calc_nodes_dist()

    subpath = shortest_path(source, target, abc._prev[source])

    subresult = []
    for j in range(len(subpath) - 1):
        sub_u = subpath[j]
        sub_v = subpath[j + 1]
        edge = abc._graph.direct_edge_for(sub_u, sub_v)
        if edge is None:
            msg = f"Can't find direct route between sub_u={sub_u} and sub_v={sub_v}"
            raise Exception(msg)
        subresult.append(edge)

    edges = get_edges_by_ids([e._id for e in subresult])

    for i in range(len(edges) - 1):
        e1 = SimpleEdge.fromdict(edges[i])
        e2 = SimpleEdge.fromdict(edges[i + 1])
        assert edge_connected(e1, e2)

    return jsonify(edges)