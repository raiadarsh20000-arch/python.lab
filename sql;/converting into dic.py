import sqlite3



db_path=r'C:\Users\acer\OneDrive\Desktop\test.01\sql;\test.db'
connection=sqlite3.connect(db_path)
connection.row_factory=sqlite3.Row

cursoe= connection.cursor()

SQL="SELECT*FROM sales_info;"
coursor.execute(SQL)
results=coursor.fetchall()
for result in results:
    (dict(result))


connection.close()
