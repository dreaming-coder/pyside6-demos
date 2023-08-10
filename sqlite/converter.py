import sqlite3
from datetime import datetime


def convert_datetime(time_str: bytes):
    return datetime.strptime(time_str.decode(encoding="utf-8"), "%Y-%m-%d %H:%M:%S")


sqlite3.register_converter("dt", convert_datetime)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.cursor()

cur.execute("create table test(id integer, p dt)")

cur.execute("insert into test values (?,?)", (2, "2023-08-08 08:59:59",))

cur.execute("select * from test")
result = cur.fetchone()

print("查询数据库结果:", result)  # (2, datetime.datetime(2023, 8, 8, 8, 59, 59))
print('查询结果类型: ', type(result[1]))  # <class 'datetime.datetime'>

cur.close()
con.close()
