import os
import sys
import folium
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from geopy import distance

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

def get_avg_distance(dados, centroids, labels, mapa=None):
    distancia_media = 0.0

    for i in range(len(dados)):
        if mapa is not None:
            line = folium.PolyLine(
                locations=[dados[i], centroids[labels[i]]],
                color="blue",
                weight=1
            )
            line.add_to(mapa)

        distancia_media += (
            distance.distance(dados[i], centroids[labels[i]]).m
            / len(dados)
        )

    return distancia_media


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

def find_min_k(dados, threshold):
    k = 1

    while True:
        kmeans = KMeans(n_clusters=k, max_iter=1000)
        kmeans.fit(dados)

        avg = get_avg_distance(
            dados,
            kmeans.cluster_centers_,
            kmeans.labels_
        )

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
    household_sizes = [1000, 3000, 5000, 10000, 30000, 50000, 100000]

    print("\nQuestão 2:")

    for n in household_sizes:
        dados = load_points(file_path)

        kmeans = KMeans(n_clusters=k, max_iter=1000)
        kmeans.fit(dados)

        avg = get_avg_distance(
            dados,
            kmeans.cluster_centers_,
            kmeans.labels_,
            mapa=None
        )

        print(
            f"  Domicílios={n:6d} → Distância média={avg:.2f} m"
        )



def quest_3(file_path):
    data = load_points(file_path)
    k_arr = list(range(50, 401, 25))
    avg_arr = []

    print("\n Questão 3:")

    for k in k_arr:
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

    data_path = os.path.join(base_path, f"{CITY_CODES['Limeira']}.csv")
    quest_2(data_path)

    lim_10k_path = os.path.join(base_path, "lim_10k.csv")
    quest_3(lim_10k_path)


    print(f"\n EXERCÍCIO 4:")

    for city, code in CITY_CODES.items():
        print(f"{city}")
        data = load_points(lim_10k_path)

        # Exercício 4:
        for threshold in (350, 150):
            k, avg = find_min_k(data, threshold)
            print(f"  Distância ≤ {threshold}, k próximo a {k}, (avg={avg})")

            centroids, labels = fit_kmeans(data, k)


            # fmap = create_map(data, centroids, labels, CITY_COORDS[city])
            # fmap.save(f"mapa_{city}_{threshold}m_k{k}.html")
    print("fim!")