def insertion_sort(lista_original):
    # Copia a lista para não modificar a original
    lista = lista_original.copy()

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Desloca os elementos maiores que a chave para a direita
        print("comparação:"  + str(lista[j]) + " " + str(chave))
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
        print("troca:" + str(lista))
    return lista


# --- Execução e Comparação ---
array_teste = [29, 10, 14, 37, 13]


print(f"Array Original: {array_teste}\n")
print(f"Resultado Insertion Sort: {insertion_sort(array_teste)}")
