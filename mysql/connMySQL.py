# coding:utf8
import MySQLdb

# print MySQLdb

conn = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    db='python_mysql',
    user='root',
    passwd='root',
    charset='utf8')
print conn

cursor = conn.cursor()
# print cursor

sql = 'select * from user'
cursor.execute(sql)
print cursor.rowcount

# rs = cursor.fetchone()
# print rs
# rs = cursor.fetchmany(2)
# print rs
rs = cursor.fetchall()
print rs

sql_insert = "insert user(id,name) values('10','june')"
sql_update = "update user set name='july' where id='5'"
sql_delete = "delete from user where id='10'"

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    conn.commit()
except Exception as e:
    print e
    conn.rollback()

cursor.close()
conn.close()
