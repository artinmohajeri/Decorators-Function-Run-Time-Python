from datetime import datetime
def calculate_time(sum_func):
    def wrapper(num):
        start = datetime.now()
        sum_func(num)
        end = datetime.now()
        return f"the calculation time is: {end - start}"
    return wrapper


@calculate_time
def get_sum(number):
    result = 0
    for i in range(number):
        result += i
    return result

print(get_sum(10000))
