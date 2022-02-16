"""
给定列表和一个数字，找出列表内两数之和为该数字的元素索引
例子：
输入：列表[3, 2, 4]，数字6。
输出：[1, 2]
"""


def two_sum_index(list_n, n):
    dic = dict()
    for i, v in enumerate(list_n):
        if n - v in dic:
            return i, dic[n - v]
        dic.update({v: i})


list_num = [3, 2, 4, 7, 6]
num = 11
x = two_sum_index(list_num, num)
print(x)