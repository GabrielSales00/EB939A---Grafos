
#Este código reduz o tamanho do arquivo.
#Seleciona um elemento a cada k elementos
# k é definido como n/tamanho
# onde n é o número de domicílio, mais de 500k
# para campinas e tamanho é o tamanho aproximado
# do arquivo de saída após este filtro.

arquivo = open('3526902.csv', 'r')
linhas = arquivo.readlines()
print(len(linhas))

tamanho = int(input("Num. de domicílios após filtro (approx):"))

espacamento = len(linhas)//tamanho

linhas = linhas[::espacamento]

saida = open(f"{tamanho//1000}k.csv","w")

for linha in linhas:
    saida.write(linha)

saida.close()
arquivo.close()