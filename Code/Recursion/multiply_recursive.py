#Thuật toán mô phỏng lại phép nhân 
def multiply_recursive(n, a):
    if n == 1:
        return a
    return multiply_recursive(n-1, a) + a

#Test
assert multiply_recursive(5, 4) == 20
assert multiply_recursive(5, -4) == -20
assert multiply_recursive(1, 4) == 4
assert multiply_recursive(7, 8) == 56