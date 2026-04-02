import folium
from sklearn.cluster import KMeans
from geopy import distance

# coordenada1 = [-22.9064, -47.0616]
# coordenada2 = [-22.9064+0.01, -47.0616+0.01]
# coordenada3 = []

# mapa = folium.Map(location=coordenada1, zoom_start=13)
# # line
# line = folium.PolyLine(locations=[coordenada1, coordenada2], color='blue')
# # Adiciona a linha ao mapa
# line.add_to(mapa)

# # Cria um marcador
# folium.Marker(coordenada1, popup=f' Campinas').add_to(mapa)
# mapa.save("Mapa_linha.html")
# print("fim!")

# # Tarefa: Crie um triângulo (3 linhas) ligando as cidades de Campinas,
# Piracicaba e Limeira. Coloque um marcador em cada cidade,
# contendo o nome da cidade.

if __name__ == "__main__":
    coord_lime = [-22.5645,-47.4004]
    coord_camp = [-22.5421, -47.0339]
    coord_pira = [-22.4230, -47.3801]

    mapa = folium.Map(location=coord_lime, zoom_start=13)
    line = folium.PolyLine(locations = [coord_lime, coord_camp, coord_pira, coord_lime], color='red')
    line.add_to(mapa)

    folium.Marker(coord_camp, popup=f'  Campinas').add_to(mapa)
    folium.Marker(coord_lime, popup=f'  Limeira').add_to(mapa)
    folium.Marker(coord_pira, popup=f'  Piracicaba').add_to(mapa)

    mapa.save("Mapa_linha.html")

    print("fim!")