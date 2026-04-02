from geopy import distance

# O código abaixo testa a distância após somar 0.001 na latitude
# e depois ao se somar 0.001 na longitude, usando como referencia
# campinas.
#1) Qual o resultado ao se mudar a localização para Ushuaia - Argentina?
#2) O que acontece se mudar a latitude para 89? Explique o resultado.
#3) Altere o código abaixo para calcular a disância entre FT-Limeira e
# Unicamp de Barão Geraldo em quilômetros.

delta = 0.001

 

lat = -22.562102902969997
long = -47.424065478538715

dist = distance.distance([lat + delta, long], [lat, long]).m
print(dist)

dist = distance.distance([lat, long + delta], [lat, long]).m
print(dist)


