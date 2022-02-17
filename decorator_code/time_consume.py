import time


# def time_c(*arg, **kwarg):
#     a = sum(arg)
#
#     def time_a(func):
#         def time_s(*args, **kwargs):
#             s = time.perf_counter()
#             result = func(*args, **kwargs)
#             e = time.perf_counter()
#             print(e - s)
#             return result, e - s, a, kwarg
#
#         return time_s
#
#     return time_a


def time_c(func):
    print('123')

    def time_s(*args, **kwargs):
        print('a')
        result = func(*args, **kwargs)
        print(1)
        return *result, 1

    print('e')
    return time_s


def time_v(func):
    print('1234')

    def time_s(*args, **kwargs):
        # print('b')
        result = func(*args, **kwargs)
        print(2)
        return *result, 2

    print('w')
    return time_s


def time_b(func):
    print('12345')

    def time_s(*args, **kwargs):
        print('c')
        result = func(*args, **kwargs)
        print(3)
        return result, 3

    print('q')
    return time_s


@time_c
@time_v
@time_b
def cycle_num(n):
    time.sleep(1)
    print("运行的函数")

    return n


# @time_c
# def cycle_num_2(n, b):
#     time.sleep(1)
#     print("运行的函数")
#
#     return n + b
#
#
# @time_c
# def cycle_num_1():
#     time.sleep(1)
#     print("运行的函数")
#
#     return 9999


# num = 123
# x = cycle_num(num)
# print(*x)

# num = 123
# bum = 1
# x = cycle_num_2(num, b=2)
# print(*x)
#
# x = cycle_num_1()
# print(x)

if __name__ == '__main__':
    i = ()
    print(1, 2, 3,)