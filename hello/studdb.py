import sqlite3

con=sqlite3.connect("login.db")
con.execute("""create table student(id integer
            primary key autoincrement,name text not null,mail text,
            phone integer)""")
con.close()
