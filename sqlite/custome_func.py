import sqlite3


def map_str(num):
    match num:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Other"


connection = sqlite3.connect("test.db")
connection.create_function("map_str", 1, map_str)

cursor = connection.cursor()
cursor.execute("create table if not exists dd (id int, str text)")

cursor.execute("insert into dd values (1,map_str(2))")
cursor.execute("insert into dd values (2,map_str(1))")
cursor.execute("insert into dd values (3,map_str(0))")

connection.commit()
