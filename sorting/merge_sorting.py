def merge(a,b):
    rs=[]
    i_a, i_b = 0, 0
    while i_a < len(a) and i_b < len(b):
        if a[i_a] <= b[i_b]:
            rs.append(a[i_a])
            i_a += 1
        else:
            rs.append(b[i_b])
            i_b += 1
    rs += a[i_a:] + b[i_b:]
    return rs


def merge_sorting(arr):
    if len(arr) <= 1:
        return arr
    return merge(merge_sorting(arr[:len(arr)//2]), merge_sorting(arr[len(arr)//2:]))


if __name__ == '__main__':
    test_arr = [7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6]
    print(merge_sorting(test_arr))