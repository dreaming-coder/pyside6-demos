import sqlite3

connection = sqlite3.connect(":memory:")


cursor = connection.cursor()

cursor.execute("create table if not exists user(id integer primary key, name text, age int)")

data = [
    (1, "ice", 18),
    (2, "亚索", 39),
    (3, "瑞雯", 16),
    (4, "泰米达尔", 28)
]

cursor.executemany("insert into user values (?, ?, ?)", data)

x = 1

cursor.execute("select * from user where 1 = ?", [x])

results = cursor.fetchall()

script = """
insert into user values (5, "菲奥娜", 14);
insert into user values (6, "盖伦", 58);
"""

cursor.executescript(script)  # 自带开启事务并 commit


