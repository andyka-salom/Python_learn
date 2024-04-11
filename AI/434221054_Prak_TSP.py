import itertools

def tsp_brute_force(graph, start, cities):
    # Generate all possible permutations of cities
    permutations = itertools.permutations(cities)

    min_cost = float('inf')
    best_path = None

    for perm in permutations:
        if perm[0] != start:
            continue

        # Calculate total cost for current permutation
        total_cost = 0
        prev_city = start
        for city in perm:
            total_cost += graph[prev_city][city]
            prev_city = city

        # Check if this permutation yields the minimum cost
        if total_cost < min_cost:
            min_cost = total_cost
            best_path = perm + (start,)

    return best_path, min_cost

def main():
    # Input jumlah kota
    num_cities = int(input("Masukkan jumlah kota: "))

    # Input kota asal dan kota tujuan
    start_city = input("Masukkan kota asal: ")
    end_city = input("Masukkan kota tujuan: ")

    # Inisialisasi graf sebagai dictionary bersarang
    graph = {}
    cities = set()

    # Input bobot untuk setiap pasangan kota
    print("Masukkan bobot untuk setiap pasangan kota:")
    for i in range(num_cities):
        city1, city2, weight = input().split()
        weight = float(weight)

        # Tambahkan kota ke set kota
        cities.add(city1)
        cities.add(city2)

        # Inisialisasi sub-dictionary jika belum ada
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}

        # Tambahkan bobot ke graf
        graph[city1][city2] = weight
        graph[city2][city1] = weight

    # Solusi menggunakan metode brute force
    best_path, min_cost = tsp_brute_force(graph, start_city, cities)

    # Output hasil
    if best_path is None:
        print("Tidak ada jalur yang ditemukan.")
    else:
        print(f"Jalur terbaik: {' -> '.join(best_path)}")
        print(f"Biaya terendah: {min_cost}")

if __name__ == "__main__":
    main()
