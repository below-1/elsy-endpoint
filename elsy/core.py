class _Edge:
    def __init__(self, edge):
        self.aId = str(edge.aId)
        self.bId = str(edge.bId)
        self._id = str(edge._id)
        self.length = edge.length

    def __repr__(self):
        return f"(_id={self._id}, aId={self.aId}, bId={self.bId}, length={self.length})"


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.path = {}

    def construct_edge_map(self):
        for e in self.edges:
            key = frozenset({ e.aId, e.bId })
            self.path[key] = e

    def length(self, u: str, v: str):
        key = frozenset({ u, v })
        if key not in self.path:
            raise Exception("Path not found")
        print(self.path[key])
        return float(self.path[key].length)

    def edge_for(self, u, v):
        for e in self.edges:
            if u == e.aId:
                if v == e.bId:
                    return e
            elif u == e.bId:
                if v == e.aId:
                    return e
        return None

    @staticmethod
    def frommongo(nodes, edges):
        _nodes = [ str(n._id) for n in nodes ]
        _edges = [ _Edge(e) for e in edges ]
        graph = Graph(_nodes, _edges)
        graph.construct_edge_map()
        return graph

def dijkstra(source: str, graph: Graph):
    edges = graph.edges
    nodes = graph.nodes
    Q = set()
    dist = {}
    prev = {}

    def min_dist():
        items = dist.items()
        in_q = [ it for it in items if it[0] in Q ]
        return min(in_q, key=lambda it: it[1])[0]

    def neighbours(u: str):
        results = []
        for e in edges:
            a = e.aId
            b = e.bId
            v = None

            if a == u:
                v = b
            elif b == u:
                v = a
            else:
                continue

            if v in Q:
                results.append(v)
        return results

    for n in nodes:
        Q.add(n)
        dist[n] = float('inf')
        prev[n] = None

    dist[source] = 0

    while len(Q) != 0:
        u = min_dist()
        Q.remove(u)

        for v in neighbours(u):
            du = dist[u]
            dv = dist[v]
            lv = graph.length(u, v)
            alt = du + lv

            if alt < dv:
                dist[v] = alt
                prev[v] = u

    return dist, prev

def shortest_path(source: str, target: str, prev):
    S = []
    u = target
    if prev[u] != None or u != source:
        while u:
            S.append(u)
            u = prev[u]
    else:
        raise Exception("Source and target not connected")

    return S

def shortest_path_to(source, targets, prev):
    return [ shortest_path(source, t, prev) for t in targets ]