from elsy.routes.blueprint import bp
from elsy.mongo import mongo_db, Node, Edge
from elsy.core import Graph, dijkstra, shortest_path_to

@bp.route("/test/dijkstra")
def test_dijkstra():
    nodes = [ Node.fromdict(doc) for doc in mongo_db.node.find() ]
    edges = [ Edge.fromdict(doc) for doc in mongo_db.edge.find() ]

    nodes_ids = [ str(n._id) for n in nodes ]

    source = nodes[0]
    target = nodes[15]

    graph = Graph.frommongo(nodes, edges)

    result = dijkstra(source, graph)
    print(result)

    return "OK"
