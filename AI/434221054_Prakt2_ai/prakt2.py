from collections import defaultdict

def shortest_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    shortest_paths_list = []
    for node in graph[start]:
        if node not in path:
            newpaths = shortest_paths(graph, node, end, path)
            for newpath in newpaths:
                shortest_paths_list.append(newpath)
    return shortest_paths_list

def add_edge(graph, vertex1, vertex2):
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

def main():
    graph = defaultdict(list)

    add_edge(graph, 'A', 'C')
    add_edge(graph, 'C', 'D')
    add_edge(graph, 'D', 'E')
    add_edge(graph, 'E', 'B')
    add_edge(graph, 'A', 'F')
    add_edge(graph, 'F', 'G')
    add_edge(graph, 'G', 'H')
    add_edge(graph, 'H', 'E')

    start_city = 'A'
    end_city = 'B'

    shortest_paths_list = shortest_paths(graph, start_city, end_city)
    if shortest_paths_list:
        print("Semua jalur terpendek antara", start_city, "dan", end_city, "adalah:")
        for i, path in enumerate(shortest_paths_list, 1):
            print(f"Jalur {i}: {path}")
    else:
        print("Tidak ada jalur yang tersedia antara", start_city, "dan", end_city)

if __name__ == "__main__":
    main()
