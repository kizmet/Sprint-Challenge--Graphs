from collections import deque


def find_path(graph, start, end, path=None):
    path = path or []

    path.append(start)
    if start == end:
        return path
    for node in graph.get(start, [])[0]:
        if node not in path:
            newpath = graph.find_path(node, end, path[:])
            if newpath:
                return newpath


def find_all_path(graph, start, end, path=None):
    path = path or []
    path.append(start)
    if start == end:
        return [path]
    paths = []
    for node in graph.get(start, [])[0]:
        if node not in path:
            newpaths = graph.find_all_path(node, end, path[:])
            paths.extend(newpaths)
    return paths


def find_shortest_path1(graph, start, end, path=None):
    path = path or []
    path.append(start)

    if start == end:
        return path
    shortest = None
    for node in graph.get(start, [])[0]:
        if node not in path:
            newpath = graph.find_shortest_path1(node, end, path[:])
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


# bfs / Queue()
def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at][0]:
            if next not in dist:
                # dist[next] = [dist[at], next]
                dist[next] = dist[at] + [next]

                q.append(next)
    # print(dist)
    return dist.get(end)
