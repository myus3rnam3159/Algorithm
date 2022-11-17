from functools import wraps

#Hàm để theo dõi các lời gọi hàm
def trace(func): # Nhận một hàm làm tham số
    func_name = func.__name__

    #Dùng dấu "|" để phân tách các lần gọi hàm khi in ra màn hình
    separator = '| '

    #Đặt độ sâu đệ quy ban đầu là 0(mỗi lần gọi + 1)
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs): #Giải thích tham số: https://www.reddit.com/r/learnpython/comments/7dsn1s/what_are_args_and_kwargs/ 
        # Hiển thị thông tin lời gọi hàm
        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        # Bắt đầu đệ quy
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # Exit current level
        trace.recursion_depth -= 1
        # Display return value
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')

        return result

    return traced_func