import copy

import numpy as np
import pandas as pd

ls = [
    {'num1': 'one', 'num2': 'two', 'num3': 'three'},
    {'num1': 'one', 'num2': 'two', 'num3': 'three'}
]
# ls_df = pd.DataFrame(ls, columns=['num1', 'num2', 'num3'], index=['a', 'b'])
ls_df = pd.DataFrame(ls)

print(ls_df)
dic = {'num1': ['one', 'one'], 'num2': ['two', 'two'], 'num3': ['three', 'three']}
dic_df = pd.DataFrame(dic)
# print(dic_df)

dic1 = {
    'num1': {'0': 'one', '1': 'one'},
    'num2': {'a': 'two', 'b': 'two'},
    'num3': {'c': 'three', 'd': 'three'},
}
dic1_df = pd.DataFrame(dic1)
# print(dic1_df)

ls = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ls_ary = np.array(ls)
ls_b = ls

ls_b[2] = [1, 2, 3]

a = ls[2][0]
b = ls_b[2][0]

# print(id(a))
# print('====')
# print(id(b))
