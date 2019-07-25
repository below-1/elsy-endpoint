from elsy.routes.blueprint import bp
from elsy.mongo import mongo_db, Node, Edge
from elsy.core import Graph, dijkstra, shortest_path_to

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

    result = dijkstra(source, graph)
    print(result)

    return "OK"
