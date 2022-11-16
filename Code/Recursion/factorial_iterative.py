# Hàm giai thừa dạng vòng lặp
def factorial_iterative_while(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result


# Kiểm tra xem hàm giai thừa có chạy đúng hay không
# Giải thích keyword assert: https://www.w3schools.com/python/ref_keyword_assert.asp

assert factorial_iterative_while(4) == 24
assert factorial_iterative_while(6) == 720
assert factorial_iterative_while(1) == 1
assert factorial_iterative_while(0) == 1
assert factorial_iterative_while(-7) == 1
assert factorial_iterative_while(50) == 30414093201713378043612608166064768844377641568960512000000000000