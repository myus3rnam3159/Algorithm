#Thuật toán đo độ dài chuỗi

#Dạng vòng lặp
def iterative_str_len(a_str):
    result = 0
    for i in range(len(a_str)):
        result += 1
    return result

#Dạng đệ quy
def recursive_str_len(a_str):
    if a_str == "":
        return 0
    return recursive_str_len(a_str[1:])  + 1

input_str = "I love recursion"
print(len(input_str))
print(iterative_str_len(input_str))
print(recursive_str_len(input_str))
