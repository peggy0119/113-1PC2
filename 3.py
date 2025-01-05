def count_inversions(arr):
    """計算逆序對數量，使用歸併排序法"""
    def merge_sort_and_count(array, temp_array, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += merge_sort_and_count(array, temp_array, left, mid)
            inv_count += merge_sort_and_count(array, temp_array, mid + 1, right)
            inv_count += merge_and_count(array, temp_array, left, mid, right)

        return inv_count

    def merge_and_count(array, temp_array, left, mid, right):
        i = left       # 左子陣列起點
        j = mid + 1    # 右子陣列起點
        k = left       # 暫存陣列起點
        inv_count = 0  # 逆序對計數

        while i <= mid and j <= right:
            if array[i] <= array[j]:
                temp_array[k] = array[i]
                i += 1
            else:
                temp_array[k] = array[j]
                inv_count += (mid - i + 1)  # 計算逆序對
                j += 1
            k += 1

        # 複製剩餘元素
        while i <= mid:
            temp_array[k] = array[i]
            i += 1
            k += 1

        while j <= right:
            temp_array[k] = array[j]
            j += 1
            k += 1

        # 將排序後的子陣列複製回原陣列
        for i in range(left, right + 1):
            array[i] = temp_array[i]

        return inv_count

    n = len(arr)
    temp_array = [0] * n
    return merge_sort_and_count(arr, temp_array, 0, n - 1)


# 讀取輸入
n = int(input("請輸入陣列元素個數："))
array = list(map(int, input("請輸入陣列元素：").split()))

# 計算逆序對數量
result = count_inversions(array)

# 輸出結果
print(f"Output：{result}")
