import folium
from sklearn.cluster import KMeans
from geopy import distance
import sys

# campinas = [-22.9064, -47.0616]

# mapa = folium.Map(location=campinas, zoom_start=13)

# # O Código abaixo converte cada linha do arquivo em
# # uma coordenada. Adiciona a coordenada em dados
# # e imprime um ponto no mapa para cada domicílio.

# arquivo = open(input("Nome do arquivo com os dados:"), 'r')
# linhas = arquivo.readlines()
# raio = 1
# dados = []
# for i in range(1, len(linhas)):
#     linha = linhas[i].split(";")
#     coordenada = [float(linha[3]), float(linha[4])]
#     dados.append(coordenada)
#     folium.Circle(radius=raio, location=coordenada, color='black', fill=True,
#                   fill_opacity=1).add_to(mapa)
# mapa.save("Mapa_pontos.html")

# # Altere o programa para imprimir os pontos de Limeira.
# # Centre o mapa em Limeira.

# #https://www.ibge.gov.br/estatisticas/sociais/populacao/38734-cadastro-nacional-de-enderecos-para-fins-estatisticos.html

# print("fim!")


if __name__ == "__main__":
    file_path = sys.argv[1]
    coord_lime = [-22.5645,-47.4004]

    mapa = folium.Map(location=coord_lime, zoom_start=13)
    with open(file_path) as f:
        lines = f.readlines()
        raio = 1
        dados = []
        for i in range(1, len(lines)):
            line = lines[i].split(";")
            coord = [float(line[3]), float(line[4])]
            dados.append(coord)
            folium.Circle(
                radius=raio,
                location=coord, 
                color='black',
                fill=True,
                fill_opacity=1
            ).add_to(mapa)
    mapa.save("Mapa_pontos.html")
    print("fim!")

