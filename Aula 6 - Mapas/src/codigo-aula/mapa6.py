import folium
from sklearn.cluster import KMeans
from geopy import distance
import sys

campinas = [-22.9064, -47.0616]
americana = [-22.73873175710013, -47.32914496719679]
limeira = [-22.5642953232023, -47.400086049564536]

mapa = folium.Map(location=limeira, zoom_start=13)

# O Código abaixo converte cada linha do arquivo em
# uma coordenada. Adiciona a coordenada em dados
# e imprime um ponto no mapa para cada domicílio.

arquivo = open(sys.argv[1], 'r')
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
k = int(sys.argv[2])

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




#continuação
# Conecta cada ponto com o respectivo centroid com uma linha
# calcule a distância média entre cada ponto e o centroide
# mais próximo
distancia_media = 0.0
for i in range(len(dados)):
    # Cria uma linha conectando o ponto ao seu centróide
    line = folium.PolyLine(locations=[dados[i], centroids[labels[i]]], color='blue')
    # Adiciona a linha ao mapa
    line.add_to(mapa)
    # Calcula a distância média
    distancia_media += distance.distance(dados[i], centroids[labels[i]]).m / len(dados)

# Cria um marcador com a informação da distância média
folium.Marker(campinas, popup=f'<b>k={k} Distância média={distancia_media}</b>').add_to(mapa)
mapa.save(f"Mapa_n_{len(dados)}_k_{k}_.html")
print("fim!")

#Para a instância 10k.csv responda:

#1) O que acontece se k=3?
#
#2) Descubra quantos pontos de ônibus são necessários,
#no mínimo, para que a distância média entre cada domícilio e o ponto mais próximo
#seja menor igual:
# a) 350m em Campinas.
# b) 150m em Campinas.
# a) 350m em Limeira.
# b) 150m em Limeira.

