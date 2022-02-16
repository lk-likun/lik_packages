"""
给定列表和一个数字，找出列表内三数之和为该数字的元素索引
例子：
输入：列表[3, 2, 4, 1]，数字6。
输出：[0, 1, 5]
"""


def sum_3index(list_n, n):
    dic = dict()
    for i, v in enumerate(list_n):
        if n - v in dic:
            print(*dic[n - v], i)
            break
        for j in range(i):
            dic.update({list_n[i] + list_n[j]: [i, j]})


list_num = [3, 5, 4, 7, 6]
num = 17
sum_3index(list_num, num)
