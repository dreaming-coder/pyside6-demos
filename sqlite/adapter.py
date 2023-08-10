import sqlite3

from datetime import datetime


def adapt_datetime(date_time: datetime):
    return date_time.strftime("%Y-%m-%d %H:%M:%S").encode(encoding="utf-8")


sqlite3.register_adapter(datetime, adapt_datetime)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
cur = con.cursor()

cur.execute("create table test(id integer, t text)")

cur.execute("insert into test values (?, ?)", (2, datetime.now(),))
cur.execute('select * from test')

print("查询结果:", cur.fetchone())  # 查询结果: (2, b'2023-08-06 15:17:09')

cur.close()
con.close()
