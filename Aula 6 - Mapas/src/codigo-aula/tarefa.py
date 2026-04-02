import os
import sys
import folium
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from geopy.distance import distance

CITY_CODES = {
    "Campinas": "3509502",
    "Limeira": "3526902"
}

CITY_COORDS = {
    "Campinas": (-22.9064, -47.0616),
    "Americana": (-22.73873175710013, -47.32914496719679),
    "Limeira": (-22.5642953232023, -47.400086049564536)
}

MAX_ITER = 1000
SEED = 42


def load_points(file_path):
    points = []
    with open(file_path, "r") as f:
        next(f) 
        for line in f:
            parts = line.strip().split(";")
            points.append((float(parts[3]), float(parts[4])))
    return points



def fit_kmeans(data, k):
    model = KMeans(
        n_clusters=k,
        max_iter=MAX_ITER,
        random_state=SEED,
        n_init="auto"
    )
    model.fit(data)
    return model.cluster_centers_, model.labels_


def get_avg_distance(points, centroids, labels):
    total = 0.0
    for p, idx in zip(points, labels):
        total += distance(p, centroids[idx]).meters
    return total / len(points)


def create_map(points, centroids, labels, center):
    fmap = folium.Map(location=center, zoom_start=13)

    for p in points:
        folium.Circle(
            location=p,
            radius=1,
            color="black",
            fill=True,
            fill_opacity=1
        ).add_to(fmap)

    for p, idx in zip(points, labels):
        folium.PolyLine(
            locations=[p, centroids[idx]],
            color="blue",
            weight=1
        ).add_to(fmap)

    return fmap


def plot_curve(x, y, xlabel, ylabel, title, filename):
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

def find_min_k(data, threshold, k_start=1):
    k = k_start
    while True:
        centroids, labels = fit_kmeans(data, k)
        avg = get_avg_distance(data, centroids, labels)
        if avg <= threshold:
            return k, avg
        k += 1


def k_distance(data, k_values):
    distances = []
    for k in k_values:
        centroids, labels = fit_kmeans(data, k)
        distances.append(get_avg_distance(data, centroids, labels))
    return distances

def quest_2(file_path):
    k = 250
    size_arr = [1000, 3000, 5000, 10000, 30000, 50000, 100000]
    avg_arr = []

    print("\n Questão 2:")

    for n in size_arr:
        data = load_points(file_path)
        centroids, labels = fit_kmeans(data, k)
        avg = get_avg_distance(data, centroids, labels)
        avg_arr.append(avg)
        print(f"  Domicílios={n:6d} → Distância média={avg:.2f} m")

    plot_curve(
        size_arr,
        avg_arr,
        "Número de domicílios",
        "Distância média",
        "Número de domicílios vs Distância média",
        "q2.png"
    )

def quest_3(file_path):
    data = load_points(file_path)
    k_arr = list(range(50, 401, 25))
    avg_arr = []

    print("\n Questão 3:")

    for k in k_values:
        centroids, labels = fit_kmeans(data, k)
        avg = get_avg_distance(data, centroids, labels)
        avg_arr.append(avg)
        print(f"k={k} → Distância média={avg}")

    plot_curve(
        k_arr,
        avg_arr,
        "Número de pontos de ônibus",
        "Distância média",
        "Distância média vs Número pontos de ônibus",
        "q3.png"
    )




if __name__ == "__main__":
    base_path = sys.argv[1]

    lim_data_path = os.path.join(base_path, f"{CITY_CODES['Limeira']}.csv")
    quest_2(camp_data_path)

    lim_10k = os.path.join(base_path, "10k.csv")
    quest_3(lim_10k)

    for city, code in CITY_CODES.items():
        print(f"{city}")

        file_path = os.path.join(base_path, f"{code}.csv")
        data = load_points(file_path)

        # Exercício 4:
        print(f"\n EXERCÍCIO 4:")
        for threshold in (350, 150):
            k, avg = find_min_k(data, threshold)
            print(f"  Distância ≤ {threshold} m → k ≈ {k} (avg={avg} m)")

            centroids, labels = fit_kmeans(data, k)


            # fmap = create_map(data, centroids, labels, CITY_COORDS[city])
            # fmap.save(f"mapa_{city}_{threshold}m_k{k}.html")
    print("fim!")