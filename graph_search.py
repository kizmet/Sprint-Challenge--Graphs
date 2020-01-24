from collections import deque


class GraphSearch:

    """Graph search emulation in python, from source
    http://www.python.org/doc/essays/graphs/"""

    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start, end, path=None):
        path = path or []

        path.append(start)
        if start == end:
            return path
        for node in self.graph.get(start, [])[0]:
            if node not in path:
                newpath = self.find_path(node, end, path[:])
                if newpath:
                    return newpath

    def find_all_path(self, start, end, path=None):
        path = path or []
        path.append(start)
        if start == end:
            return [path]
        paths = []
        for node in self.graph.get(start, [])[0]:
            if node not in path:
                newpaths = self.find_all_path(node, end, path[:])
                paths.extend(newpaths)
        return paths

    def find_shortest_path1(self, start, end, path=None):
        path = path or []
        path.append(start)

        if start == end:
            return path
        shortest = None
        for node in self.graph.get(start, [])[0]:
            if node not in path:
                newpath = self.find_shortest_path1(node, end, path[:])
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    # bfs / Queue()
    def find_shortest_path(self, start, end):
        dist = {start: [start]}
        q = deque([start])
        while len(q):
            at = q.popleft()
            for next in self.graph[at][0]:
                if next not in dist:
                    # dist[next] = [dist[at], next]
                    dist[next] = dist[at] + [next]

                    q.append(next)
        # print(dist)
        return dist.get(end)


def main():
    """
    # example of graph usage
    >>> graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}
    # initialization of new graph search object
    >>> graph1 = GraphSearch(graph)
    >>> print(graph1.find_path('A', 'D'))
    ['A', 'B', 'C', 'D']
    >>> print(graph1.find_all_path('A', 'D'))
    [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
    >>> print(graph1.find_shortest_path('A', 'D'))
    ['A', 'B', 'D']
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
