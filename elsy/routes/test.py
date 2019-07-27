from elsy.routes.blueprint import bp
from elsy.mongo import mongo_db, Node, Edge
from elsy.core import Graph, dijkstra, shortest_path_to, SimpleEdge, ElsyTSPABC
from flask import jsonify

main_nodes = [ f"{i}" for i in range(1, 8) ]
int_nodes =[ f"n{i}" for i in range(1, 11) ]
all_nodes = [*main_nodes, *int_nodes]

def e_from_dict(d):
    # Add a and b
    d['a'] = None
    d['b'] = None
    return Edge.fromdict(d)

edges = [
    { '_id': 'e1', 'aId': '1', 'bId': 'n1', 'length': 5 },
    { '_id': 'e2', 'aId': '1', 'bId': 'n2', 'length': 4 },
    { '_id': 'e3', 'aId': '2', 'bId': 'n1', 'length': 6 },
    { '_id': 'e4', 'aId': '2', 'bId': 'n4', 'length': 3 },
    { '_id': 'e5', 'aId': '3', 'bId': 'n3', 'length': 3 },
    { '_id': 'e6', 'aId': '3', 'bId': 'n5', 'length': 2 },
    { '_id': 'e7', 'aId': '4', 'bId': 'n9', 'length': 2.5 },
    { '_id': 'e8', 'aId': '4', 'bId': 'n6', 'length': 1.75 },
    { '_id': 'e9', 'aId': '5', 'bId': 'n1', 'length': 6 },
    { '_id': 'e10', 'aId': '5', 'bId': 'n10', 'length': 5.5 },
    { '_id': 'e11', 'aId': '6', 'bId': 'n7', 'length': 2 },
    { '_id': 'e12', 'aId': '6', 'bId': 'n8', 'length': 2 },
    { '_id': 'e13', 'aId': '7', 'bId': 'n8', 'length': 2 },
    { '_id': 'e14', 'aId': 'n5', 'bId': 'n6', 'length': 3.75 },
    { '_id': 'e15', 'aId': 'n9', 'bId': 'n10', 'length': 5.5 },
    { '_id': 'e16', 'aId': 'n3', 'bId': 'n4', 'length': 3 },
    { '_id': 'e17', 'aId': 'n6', 'bId': 'n7', 'length': 2.5 },
    { '_id': 'e18', 'aId': 'n2', 'bId': 'n3', 'length': 3 }
]
edges = [ e_from_dict(d) for d in edges ]

# Convert edge to Edge type

@bp.route("/test/dijkstra")
def test_dijkstra():
    source = main_nodes[0]
    target = main_nodes[5]

    graph = Graph(all_nodes, edges)
    graph.construct_edge_map()

    dist, prev = dijkstra(source, graph)
    path = shortest_path_to(source, target, prev)
    
    # path = shortest_path_to(source, target, prev)
    print("prev")
    print(prev)
    print("dist")
    print(dist)

    return "OK"

@bp.route("/test/dijkstra-mongo")
def test_dijkstra_mongo():
    main_node_filter = {
      '$or': [
        { 'jabatan': 'rt' },
        { 'jabatan': 'rw' }
      ]
    }

    nodes = list(mongo_db.node.find(main_node_filter))
    inters = list( mongo_db.node.find({ 'jabatan': 'intersection' }) )

    nodes = [ str(n['_id']) for n in nodes ]
    inters = [ str(n['_id']) for n in inters ]

    all_nodes = [ *nodes, *inters ]

    edges = list(mongo_db.edge.find())
    edges = [ SimpleEdge.fromdict(e) for e in edges ]

    graph = Graph(all_nodes, edges)
    graph.construct_edge_map()

    source = nodes[1]
    targets = [ t for t in nodes if t != source ]

    dist, prev = dijkstra(source, graph)

    path = shortest_path_to(source, targets, prev)

    return jsonify({
      "source": source,
      "target": targets
    })

@bp.route("/test/abc")
def test_abc_tsp():
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

    abc = ElsyTSPABC(nodes, inters, edges)
    abc.calc_nodes_dist()
    route = abc.abc(nodes[0], n=10, limit=10)

    # for n in nodes:
    #     print(f"n={n}")
    #     maps = abc._dist[n]
    #     for k, v in maps.items():
    #         if k not in nodes:
    #             continue
    #         print(f"{k} -> {v}")
    #     input()

    return jsonify(route)