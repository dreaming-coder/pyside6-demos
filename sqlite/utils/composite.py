import sqlite3
from datetime import datetime


def convert_datetime(time_str: bytes):
    return datetime.strptime(time_str.decode(encoding="utf-8"), "%Y-%m-%d %H:%M:%S")


def adapt_datetime(date_time: datetime):
    return date_time.strftime("%Y-%m-%d %H:%M:%S").encode(encoding="utf-8")


sqlite3.register_adapter(datetime, adapt_datetime)

sqlite3.register_converter("dt", convert_datetime)

con = sqlite3.connect("../test.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = con.cursor()

cur.execute("create table if not exists test(id integer, p dt)")

cur.execute("insert into test values (?, ?)", (2, datetime.now(),))
cur.execute("insert into test values (?,?)", (2, "2023-08-08 08:59:59",))

cur.execute("select * from test")
result = cur.fetchall()

print("查询数据库结果:", result[0])  # (2, datetime.datetime(2023, 8, 6, 15, 34, 7))
print("查询数据库结果:", result[1])  # (2, datetime.datetime(2023, 8, 8, 8, 59, 59))
print('查询结果类型: ', type(result[0][1]))  # <class 'datetime.datetime'>
print('查询结果类型: ', type(result[1][1]))  # <class 'datetime.datetime'>

cur.close()
con.commit()
con.close()
