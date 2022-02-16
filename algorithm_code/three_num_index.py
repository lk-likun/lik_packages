"""
给定列表和一个数字，找出列表内三数之和为该数字的元素索引
例子：
输入：列表[3, 2, 4, 1]，数字6。
输出：[0, 1, 5]
"""


def two_sum_index(list_n, n):
    tmp = dict()
    for i, v in enumerate(list_n):
        if n - v in tmp:
            return tmp[n - v], i
        tmp.update({v: i})


def test(ls, n):
    tmp = dict()
    for i, v in enumerate(ls):
        tmp_ls = tmp.keys()
        z = two_sum_index(tmp_ls, n - v)
        if z:
            return *z, i
        tmp.update({v: i})


list_num = [3, 5, 4, 7, 6]
num = 13
x = test(list_num, num)
print(x)
