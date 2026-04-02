import folium

lat = -22.5645
long = -47.4004

mapa = folium.Map(location=[lat, long], zoom_start=15)

# O código abaixo cria um círculo ao redor da coordenada
# 1) aumente o raio para 500, coloque opacidade 0.2 e cor
# vermelha
# 2) Mude o centro do mapa para a FT unicamp.
raio = 500
folium.Circle(radius=raio, location=[lat, long], color='red', fill=True,
              fill_opacity=0.2).add_to(mapa)

mapa.save("Mapa_circulo.html")

print("fim!")


