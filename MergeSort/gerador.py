import random

lista = []   # lista que vai armazenar os números aleatórios

for i in range(0, 100000):                    # repete 100.000 vezes
    lista.append(random.randint(0, 500000))   # gera um número aleatório entre 0 e 500000 e adiciona à lista

with open("arquivo.txt", "w") as f:                    # cria (ou sobrescreve) o arquivo "arquivo.txt"
    f.write("\n".join(str(n) for n in lista))          # escreve os números no arquivo, um por linha