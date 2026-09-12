def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


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
    return lista


if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", numbers)
    print("Lista ordenada:", merge_sort(numbers))
