import string

import MySQLdb
import numpy as np
import pandas as pd
from data_base.config import DSN
from dbutils.pooled_db import PooledDB

# dsn = {
#     'host': '39.103.166.17',
#     'port': '3306',
#     'user': 'root',
#     'passwd': 'Admin123@pl',
#     'db': 'lik'
# }
#
# spl = PooledDB(MySQLdb, **dsn)
#
# sql = ""
# conn = spl.connection()
# try:
#     with conn.cursor() as cs:
#         cs.execute(sql, args=(1,))
#     conn.commit()
# except MySQLdb.Error as e:
#     print(e)
# finally:
#     conn.close()
SPL = PooledDB(MySQLdb, **DSN)


class DB:

    @staticmethod
    def trans_key(dic: dict, join=', '):
        left = list(dic.keys())
        right = ['=%s'] * len(dic)
        res = [left[i] + right[i] for i in range(len(dic))]
        return join.join(res)

    @staticmethod
    def filter(table, show_list=None, **condition):
        conn = SPL.connection()
        try:
            if show_list:
                show_str = ', '.join(show_list)
            else:
                show_str = '*'
            condition.update({'1': 1})
            con_str = DB.trans_key(condition, ' and ')
            sql = f'select {show_str} from {table} where {con_str}'
            with conn.cursor() as cs:
                cs.execute(sql, args=condition.values())
                result = cs.fetchall()
                if show_list is None:
                    cs.execute(f'desc {table}')
                    col = cs.fetchall()
                    show_list = [i[0] for i in col]
            conn.commit()
            res = pd.DataFrame(result, columns=show_list)
            return res
        except MySQLdb.Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def create(table, insert_list=None, insert_res=None):
        # INSERT INTO table1(a,b) VALUES(a1,b1);
        # INSERT INTO table1(a,b) VALUES(a1,b1),(a2,b2),(a3,b3),(a4,b4);
        conn = SPL.connection()
        try:
            with conn.cursor() as cs:
                if insert_res:
                    insert_str = ','.join(insert_list)
                    insert_res_str = ','.join(['(' + str(i)[1:-1] + ')' for i in insert_res])
                    # insert_res_str = str([tuple(i) for i in insert_res])
                sql = f'INSERT INTO {table}({insert_str}) VALUES{insert_res_str}'
                print(sql)
                cs.execute(sql)
            conn.commit()
        except MySQLdb.Error as e:
            print(e)
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def update(table, update_dic=None, **condition):
        # UPDATE 表名 SET 字段1 = 值1,字段2=值2... WHERE 字句
        conn = SPL.connection()
        try:
            if update_dic:
                condition.update({'1': 1})
                key_str = DB.trans_key(update_dic)
                con_str = DB.trans_key(condition, join=' and ')
                sql = f"update {table} set {key_str} where {con_str}"
                values = list(update_dic.values())
                values.extend(list(condition.values()))
                with conn.cursor() as cs:
                    cs.execute(sql, values)
                    # if update_dic and condition is None:
                    #     sql = 'update {} set '.format(table) + ('="{}",'.join(update_dic.keys()) + '="{}"').format(
                    #         *update_dic.values()) + ' where 1=1'
                    # if condition:
                    #     sql = 'update {} set '.format(table) + '="{}",'.join(update_dic.keys()) + '="{}"'
                    #     sql = sql.format(*update_dic.values()) + ' where ' + '="{}" and '.join(condition.keys()) + '="{}"'
                    #     sql = sql.format(*condition.values())
                    #     cs.execute(sql)
                conn.commit()
        except MySQLdb.Error as e:
            print(e)
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def delete(table, **condition):
        # DELETE FROM table_name [WHERE Clause]
        conn = SPL.connection()
        try:
            with conn.cursor() as cs:
                condition.update({'1': 1})
                con_str = DB.trans_key(condition, join=' and ')
                sql = f"delete from {table} where {con_str}"
                print(sql)

                # if condition:
                #     con_str = DB.trans_key(condition, join=' and ')
                #
                # #     sql = 'delete from {}'.format(table) + ' where '
                # #     sql += '="{}" and '.join(delete_dic.keys()) + '="{}"'
                # # sql = sql.format(*delete_dic.values())
                # else:
                #     condition.update({'1': 1})
                # sql = f"delete from {table} where {con_str}"
                # cs.execute(sql)
                # print(sql)
            conn.commit()
        except MySQLdb.Error as e:
            print(e)
            conn.rollback()
        finally:
            conn.close()


data_txt = pd.read_csv('D:\\lik_test\\one.txt')
create_col = data_txt.columns.tolist()
create_col[4] = 'LON'
create_res = np.array(data_txt[:]).tolist()
DB.create('onehour', insert_list=create_col, insert_res=create_res)
# 'STCD', 'VARCHAR(50)'
# df = DB.filter('student', show_list=['name', 'class', 'age'], age=15)
# df.loc[df['name'] == '小明', 'age'] = 16
# rest = df.to_dict(orient='records')
# print(rest)

# df.loc[0, 'age'] = 16
# print(df)

# DB.update('student', name='小徐', age=16)
# con = {'name': '小徐', 'age': 16}
# DB.delete('student', **con)

