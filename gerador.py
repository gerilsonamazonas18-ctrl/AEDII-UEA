import random

lista = []

for i in range(0, 100000):
    lista.append(random.randint(0, 500000))

with open("arquivo.txt", "w") as f:
    f.write("\n".join(str(n) for n in lista))