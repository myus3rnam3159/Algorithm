import sys
from trace_recursion import trace

#Hàm giai thừa dạng đệ quy
#Chú ý: hàm này chỉ chịu được n < 1000


def factorial(n):
    if n<=1:
        return 1 # Đây là base case
    return n * factorial(n-1)

#Test
# print(factorial(4))
# print(factorial(6))
# print(factorial(1))
# print(factorial(0))
# print(factorial(-7))

#Biểu diễn các lời gọi hàm đệ quy ra màn hình
# factorial = trace(factorial)
# factorial(5)

#Gia tăng giới hạn cho hàm giai thừa quá n > 1000
sys.setrecursionlimit(1002)
print(sys.getrecursionlimit())
print(factorial(1000))