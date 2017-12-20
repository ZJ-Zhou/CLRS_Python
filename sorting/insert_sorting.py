def insert_sorting(arr):
    for i in range(1, len(arr)):
        j = 1
        tmp = arr[i]
        while (arr[i] < arr[i - j] and i - j >= 0):
            arr[i - j + 1] = arr[i - j]
            j += 1
        arr[i - j + 1] = tmp
    return arr


if __name__ == '__main__':
    test_arr = [1, 4, 2, 6, 7]
    print(insert_sorting(test_arr))
