import folium
#scikit-learn.
from sklearn.cluster import KMeans
from geopy import distance

campinas = [-22.9064, -47.0616]

mapa = folium.Map(location=campinas, zoom_start=13)

# O Código abaixo converte cada linha do arquivo em
# uma coordenada. Adiciona a coordenada em dados
# e imprime um ponto no mapa para cada domicílio.

arquivo = open(input("Nome do arquivo com os dados:"), 'r')
linhas = arquivo.readlines()
raio = 1
dados = []
for i in range(1, len(linhas)):
    linha = linhas[i].split(";")
    coordenada = [float(linha[3]), float(linha[4])]
    dados.append(coordenada)
    folium.Circle(radius=raio, location=coordenada, color='black', fill=True,
                  fill_opacity=1).add_to(mapa)

# Continuação:
# O código abaixo executa o k-means nos dados
# número de pontos de ônibus
k = int(input("Digite o número de pontos de ônibus:"))

# Inicializa o objeto K-means
kmeans = KMeans(n_clusters=k,max_iter=1000)

# Ajuste os centroids do K-means de acordo com os dados
kmeans.fit(dados)

# Obtenha o centróides o os rótulos de
# cada ponto
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Coordenadas dos centroides
print(centroids)
# Agrupamento de cada ponto
print(labels)



print("fim!")
