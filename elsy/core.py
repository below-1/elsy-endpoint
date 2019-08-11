import random
import math

class SimpleEdge:

    allowed_keys = { "_id", "aId", "bId", "length" }

    def __init__(self, _id=None, aId=None, bId=None, length=0):
        self.aId = str(aId)
        self.bId = str(bId)
        self._id = str(_id)
        self.length = float(length)

    def __repr__(self):
        return f"(_id={self._id}, aId={self.aId}, bId={self.bId}, length={self.length})"

    @staticmethod
    def fromdict(d):
        df = {k: v for k, v in d.items() if k in SimpleEdge.allowed_keys }
        return SimpleEdge(**df)

class Graph:
    def __init__(self, nodes, edges):
        '''
        For the love of Mother Earth, you should ensure that nodes you suplied,
        is linked to at least one other node.
        And BTW this is undirected graph.
        :param nodes: nodes.
        :param edges: edges.
        '''
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
        return float(self.path[key].length)

    def direct_edge_for(self, u, v):
        '''
        Construct direct edge that joining node u and v.
        :param u: Node
        :param v: Node.
        :return: Edge that connect u and v.
        '''
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
        _nodes = [ str(n['_id']) for n in nodes ]
        _edges = [ SimpleEdge.fromdict(e) for e in edges ]
        graph = Graph(_nodes, _edges)
        graph.construct_edge_map()
        return graph


def dijkstra(source: str, graph: Graph):
    '''
    Calculate the minimum route and its distance
    for each route from source to every other nodein graph.
    :param source: starting point of algorithm
    :param graph: The the graph.
    :return: (dist, prev) dist is map of minimum distance from source.
        and prev is some kind of map we use to travel back to starting point.
    '''
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

        uneighbours = neighbours(u)
        for v in uneighbours:
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
    if prev.get(u, None) != None or u != source:
        while u:
            S.append(u)
            u = prev[u]
    else:
        raise Exception("Source and target not connected")

    # Return reversed S. because we starting from target all the way back to the source.
    return list(reversed(S))

def shortest_path_to(source, targets, prev):
    return [ shortest_path(source, t, prev) for t in targets ]


class ElsyTSPABC:
    def __init__(self, nodes, inters, edges):
        self.nodes = nodes
        self.inters = inters
        self.edges = edges
        self._dist = {}
        self._prev = {}
        self._graph = None

    def calc_nodes_dist(self):
        all_nodes = [*self.nodes, *self.inters]
        graph = Graph(all_nodes, self.edges)
        graph.construct_edge_map()
        self._graph = graph
        for source in self.nodes:
            dist, prev = dijkstra(source, graph)

            # Make sure there is valid connection between this node and the rest of graph
            dvals = list(dist.values())
            total_inf = sum(v == float('inf') for v in dvals)
            if total_inf == len(dvals) - 1:
                msg = f"This node is not connected to the rest of graph. source={source}"
                raise Exception(msg)

            self._dist[source] = dist
            self._prev[source] = prev

    def fitness(self, path):
        if len(self._dist) == 0 or len(self._prev) == 0:
            raise Exception("Distance and Prev not yet computed. please call calc_nodes_dist first")
        
        if len(path) < 2:
            raise Exception("path must have at least 2 elements")
        
        total = 0
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            total += self._dist[u][v]
        return total

    def abc(self, source, n=100, limit=10, maxiter=100):

        Xs = []
        Fx = []
        abandoned = []

        global_min_sol = None
        global_min_fx = float("inf")

        # Init phase
        for i in range(n):
            Xs.append(None)
            Fx.append(None)
            abandoned.append(True)

        for i in range(maxiter):
            # Scout bees first
            # Take abandoned, modifying iterable while we iterating it.
            # Iterate the copy then
            for (ab_idx, abandon) in enumerate(abandoned):
                if not abandon:
                    continue

                temp = self.nodes[:]
                # Remove source for a while
                temp = [ t for t in temp if t != source ]

                # Jiggle Jiggle Little Shuffle
                random.shuffle(temp)

                # So we can put it in front of solution and the back of solution
                temp = [ source, *temp, source ]

                Xs[ab_idx] = temp

                # Calculate fitness
                Fx[ab_idx] = self.fitness(temp)

                # Mark it as fresh one
                abandoned[ab_idx] = False

            # Employed phase
            for j, xs in enumerate(Xs):
                vs = self._shuff_sol(xs)
                assert vs[0] == source == vs[-1]
                x_fit = Fx[j]
                v_fit = self.fitness(vs)
                if v_fit < x_fit:
                    Xs[j] = vs
                    Fx[j] = v_fit

            # Onlooker phase
            # Our objective is finding solution with minimum fitness
            # So we need to make sure that the smallest fitness get the highest probability
            max_fit = max(Fx)
            invert_Fx = [ max_fit - fx for fx in Fx ]
            total_fit = sum(invert_Fx)
            Px = [ (fx * 1.0 / total_fit) for fx in invert_Fx ]

            if abs(sum(Px) - 1.0) > 0.01:
                msg = "total Px is not equal 1"
                raise Exception(msg)

            onlook_xs = self._choose_weighted(Xs, Px)

            # Here the "j" record the original index of solution.
            for j, xs in onlook_xs:
                temp = xs[:]
                count = 0
                for k in range(limit):
                    modified = self._shuff_sol(temp)
                    m_fit = self.fitness(modified)
                    x_fit = Fx[j]
                    if m_fit < x_fit:
                        Xs[j] = modified
                        Fx[j] = m_fit
                        break
                    count += 1
                if count >= limit:
                    abandoned[j] = True
            min_Fx = min(Fx)
            if min_Fx < global_min_fx:
                min_index = Fx.index(min_Fx)
                # Just copy it
                global_min_sol = Xs[min_index][:]
                global_min_fx = min_Fx

        # Construct the path
        route = self._construct_shortest_route(global_min_sol)
        return (global_min_sol, route)

    def _shuff_sol(self, xs):
        vs = xs[:]
        assert len(vs) >= 4

        # Get index to swap
        # 0 < index < len(vs) - 2
        # We need to exclude first and third index from the end
        # last index is len(vs) - 3
        i_swap_1 = random.randint(1, len(vs) - 3)
        i_swap_2 = i_swap_1 + 1
        a = vs[i_swap_1]
        b = vs[i_swap_2]
        a, b = b, a
        vs[i_swap_1] = a
        vs[i_swap_2] = b
        return vs
    
    def _choose_weighted(self, opts, ws):
        assert len(opts) == len(ws)
        assert abs(sum(ws) - 1.0) < 0.001

        results = []
        for n_onlook in range(len(opts)):
            r = random.random()
            for i, opt in enumerate(opts):
                if r <= ws[i]:
                    results.append((i, opt))
        return results

    def _edge_connected(self, e1, e2):
        candidate_1 = e1.aId
        if candidate_1 == e2.aId or candidate_1 == e2.bId:
            return True
        candidate_2 = e1.bId
        if candidate_2 == e2.aId or candidate_2 == e2.bId:
            return True
        return False

    def _construct_shortest_route(self, path):
        result = []
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]

            # Here we construct the indirect route.
            subpath = shortest_path(u, v, self._prev[u])

            assert subpath[0] == u
            assert subpath[-1] == v

            # After we get the indirect route,
            # We need to span/unfold the indirect into direct one.
            # Because the assumption states that each node at least connected one time,
            # There must be a direct route connected u and v.
            subresult = []
            for j in range(len(subpath) - 1):
                sub_u = subpath[j]
                sub_v = subpath[j + 1]
                edge = self._graph.direct_edge_for(sub_u, sub_v)
                if edge is None:
                    msg = f"Can't find direct route between sub_u={sub_u} and sub_v={sub_v}"
                    raise Exception(msg)
                subresult.append(edge)
            # subresult = list(reversed(subresult))
            result.extend(subresult)
        # for i in range(len(result) - 1):
        #     e1 = result[i]
        #     e2 = result[i + 1]
        #     assert self._edge_connected(e1, e2)
        return result