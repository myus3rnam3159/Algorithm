#Thuật toán quick sort đệ quy
def quicksort(arr):
    #Trả về kết quả nếu mảng có một phần tử
    if len(arr) <= 1:
        return arr
    #Chọn pivot
    pivot = arr[len(arr) // 2]
    #Chia thành 3 mảng con
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

data = [1, 6, 5, 5, 2, 6, 1]
print(quicksort(data))

