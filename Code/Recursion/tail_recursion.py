#Mô phỏng tail call recursion
import inspect

#Trường hợp không dùng tới tail call
def factorial(n):
    print("Tối ưu không dùng tailed opitmised stack size: ", len(inspect.stack(0)))
    if n == 0:
        return 1
    return factorial(n-1) * n

#Dùng tail call
def tail_factorial_attempt(n, accumulator = 1):
    print("Attempted tail optimised stack size: ", len(inspect.stack(0)))
    if n == 0:
        return accumulator
    return tail_factorial_attempt(n-1, accumulator * n)

if __name__ == "__main__":
    print(factorial(5))
    print(tail_factorial_attempt(5))