import copy

import numpy as np
import pandas as pd

data_txt = pd.read_csv('D:\\lik_test\\one.txt')
# data_txt['level'] = 0
#
# data_txt.rename(columns={'DT': 'time', 'STCD': 'id', 'INTV': 'dtime', 'LATI': 'lat', 'LONG': 'lon', 'RAIN': 'data'},
#                 inplace=True)
#
# # print(data_txt)
# # data_txt.drop(axis=1, labels='WTHR', inplace=True)
#
# data_txt = data_txt[['level', 'time', 'dtime', 'id', 'lon', 'lat', 'data']]
# data_txt_ls = copy.deepcopy(data_txt)
# data_txt_ls['dtime'] = data_txt_ls['dtime'].apply(lambda x: float(x))
# print(data_txt_ls)
print(data_txt.columns.tolist())
x = np.array(data_txt.loc[0:2]).tolist()
print(x)
ls = np.array(data_txt[:])
print(ls)