import sqlite3
connect=sqlite3.connect('aa.db')
cursor=connect.cursor()
table='create table performance(prediction VARCHAR(25))'
cursor.execute(table)