import pandas as pd

ls = [
    {'姓名': '小明', '年龄': 20, '性别': '男', '班级': '一班'},
    {'姓名': '小华', '年龄': 18, '性别': '女', '班级': '二班'},
    {'姓名': '小张', '年龄': 21, '性别': '男', '班级': '三班'}
]

# dic = {
#     '姓名': ['小明', '小华', '小张', '小李'],
#     '年龄': [20, 18, 20, 22],
#     '性别': ['男', '女', '男', '男'],
#     '班级': ['一班', '二班', '三班', '三班'],
#     '学校': ['一中', '二中', '二中', '二中']
# }

df = pd.DataFrame(ls)

file_xlsx_path = 'D:\\lik_test\\test.xlsx'
file_txt_path = 'D:\\lik_test\\test.txt'
df_r = pd.read_excel(file_xlsx_path)
df.loc[2, '年龄'] = 20
dic = {'姓名': ['小李'], '年龄': [22], '性别': ['男'], '班级': ['三班']}
dic2 = {'学校': ['一中', '二中', '二中', '二中']}
df1 = pd.DataFrame(dic)
df2 = pd.DataFrame(dic2)
res = pd.concat([df, df1], axis=0).reset_index(drop=True)
res2 = pd.concat([res, df2], axis=1)
# res2.columns = ['a', 'b', 'c', 'd', 'e']
# res2.drop(axis=1, labels=['性'], inplace=True)
# res2.drop(axis=0, labels=[2], inplace=True)
# print(res2)

res2.to_excel('D:\\lik_test\\test.xlsx')
res2.to_csv('D:\\lik_test\\test.txt', sep='\t', index=False)

df_r_txt = pd.read_csv('D:\\lik_test\\test.txt', sep='\t')
print(df_r_txt)
# with open('D:\\lik_test\\test.txt','r',encoding='utf8') as f:
#     data = f.read()
#     print(data)
# data_excel = pd.read_excel('D:\\lik_test\\test.xlsx')
# print(data_excel)