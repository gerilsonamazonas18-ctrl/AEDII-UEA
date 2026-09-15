def insertion_sort(lista_original):

    lista = lista_original.copy()

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        print(f"comparação:{lista[j]} {chave}")
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
        print("troca:" + str(lista))
    return lista


array_teste = [29, 10, 14, 37, 13]


print(f"Array Original: {array_teste}\n")
print(f"Resultado Insertion Sort: {insertion_sort(array_teste)}")
