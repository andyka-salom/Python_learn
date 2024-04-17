import itertools

def calculate_path_length(path, graph):
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i]][path[i+1]]
    length += graph[path[-1]][path[0]]  
    return length

def traveling_salesman(num_cities, graph):
    cities = [i for i in range(num_cities)]
    shortest_path = None
    shortest_length = float('inf')

    for perm in itertools.permutations(cities):
        length = calculate_path_length(perm, graph)
        if length < shortest_length:
            shortest_length = length
            shortest_path = perm

    return shortest_path, shortest_length

def main():
    num_cities = int(input("Masukkan jumlah kota: "))
    graph = [[] for _ in range(num_cities)]

    # Input bobot/jarak antar kota
    for i in range(num_cities):
        for j in range(num_cities):
            if i == j:
                graph[i].append(0)
            else:
                weight = float(input(f"Masukkan bobot antara kota {i} dan {j}: "))
                graph[i].append(weight)

    start_city = int(input("Masukkan kota asal (dalam range 0 sampai {num_cities - 1}): "))
    end_city = int(input("Masukkan kota tujuan (dalam range 0 sampai {num_cities - 1}): "))

    shortest_path, shortest_length = traveling_salesman(num_cities, graph)
    print(f"Jalur terpendek: {shortest_path}")
    print(f"Panjang jalur terpendek: {shortest_length}")

if __name__ == "__main__":
    main()
