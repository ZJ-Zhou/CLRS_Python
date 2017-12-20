def insert_sorting(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        j = 1
        while (arr[i] < arr[i - j] and i - j >= 0):
            arr[i - j + 1], arr[i - j] = arr[i - j], arr[i - j + 1]
            j += 1
    return arr


if __name__ == '__main__':
    test_arr = [1, 4, 2, 6, 7]
    print(insert_sorting(test_arr))
