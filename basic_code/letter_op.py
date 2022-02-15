import time

'''
1、字母向后n位赋值
2、数字保持不变
'''


def trans_al(al_index, n):
    new_index = (al_index + n) % 26
    return new_index


def letter_op(long_str, num=1):
    new_list = list()
    min_up = ord('A')
    min_low = ord('a')
    max_up = ord('Z')
    for i in long_str:
        if not i.isalpha():
            new_list.append(i)
        else:
            if ord(i) <= max_up:
                p = ord(i) - min_up
                res = trans_al(p, num)
                new_list.append(chr(res + min_up))
            else:
                p = ord(i) - min_low
                res = trans_al(p, num)
                new_list.append(chr(res + min_low))

    new_str = ''.join(new_list)
    print(new_str)
    return new_str


t_1 = time.perf_counter()
str_1 = 'a' * 10000
letter_op(str_1, 1)
t_2 = time.perf_counter()
print(t_2 - t_1)

