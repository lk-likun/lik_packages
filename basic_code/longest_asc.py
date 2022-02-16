"""
输入[2, 1, 5, 2, 4, 5, 1, 3, 7, 9, 1]，
输出[1, 2, 4, 5, 7, 9]
"""


def longest_asc_order(list_n):
    dic = dict()
    for i, v in enumerate(list_n[:-1]):
        ls = list()
        for k in range(i + 1, len(list_n)):
            tmp = [v]
            for j in range(k, len(list_n)):
                if tmp[-1] < list_n[j]:
                    tmp.append(list_n[j])
            ls.append(tmp)
        ls = list(sorted(ls, key=lambda x: len(x)))
        dic.update({i: ls[-1]})
    x = list(dict(sorted(dic.items(), key=lambda y: len(y[1]))).values())[-1]
    print(x)


list_num = [2, 1, 5, 2, 4, 5, 1, 3, 7, 9, 1]
longest_asc_order(list_num)
if __name__ == '__main__':
    dic = {'x': 1, 'y': 2, 'z': 3}
    print(dic.items())
