
#import openrouteservice
#import cartopy
import folium



# O código abaixo cria um mapa centrado em campinas.
# 1) Mude o centro do mapa para a FT de Limeira.
# 2) Crie três versões do mapa, uma com zoom mostrando o estado de
# São Paulo. Um mostrando a cidade de Limeira e outro mostrando o
# Campus da FT.

lat = -22.56191
long = -47.42395

zoom_list = [7, 10, 30]

for zoom in zoom_list:
    mapa = folium.Map(location=[lat, long], zoom_start=zoom)
    mapa.save(f"Mapa_zoom_{zoom}.html")

print("fim!")
