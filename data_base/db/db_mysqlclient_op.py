import MySQLdb

conn = MySQLdb.connect(
    host='39.103.166.17',
    port=3306,
    user='root',
    passwd='Admin123@pl',
    db='lik',
)
cur = conn.cursor()
cur.execute('desc student')
result = cur.fetchall()
x = [i[0] for i in result]
print(x)
cur.close()
conn.commit()
conn.close()
