"""
列表第三大的数字
"""


def third_max_num(list_num):
    new_set = set(list_num)
    new_list = list(new_set)
    return new_list[-3]


num = [1, 3, 4, 7, 1, 4, 2, 0]
third_max_num(num)

