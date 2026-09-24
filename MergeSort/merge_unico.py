def merge_sort(arr):
    if len(arr) <= 1:
        return arr


    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    right = merge_sort(arr[meio:])

    return merge(esquerda, right)

def merge(left, right):
    lista = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lista.append(left[i])
            i += 1
        else:
            lista.append(right[j])
            j += 1
            
    lista.extend(left[i:])
    lista.extend(right[j:])
    with open("arquivo_ordenado.txt", "w") as f:
        f.write("\n".join(map(str, lista)))
    return lista


if __name__ == "__main__":
    with open("arquivo.txt") as arquivo:
        numbers = list(map(int, arquivo))
    merge_sort(numbers)
    print("Lista ordenada: CONCLUIDA")