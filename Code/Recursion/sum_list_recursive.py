# Hàm tính tổng tổng các phần tử trong list


# Dạng vòng lặp
def list_sum(a_list):
    result = 0
    for val in a_list:
        result += val
    return result


# Dạng đệ quy
def list_sum_recursive(a_list):
    if len(a_list) == 0:
        return 0
    return a_list[0] + list_sum_recursive(a_list[1:])


# Test
assert list_sum([2, 3, 5, 7]) == 17
assert list_sum([-4, -3, -2, -1, 10]) == 0

assert list_sum_recursive([2, 3, 5, 7]) == 17
assert list_sum_recursive([-4, -3, -2, -1, 10]) == 0
assert list_sum_recursive([]) == 0
assert list_sum_recursive([3]) == 3
assert list_sum_recursive([-5, -3]) == -8
