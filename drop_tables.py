import sqlite3

conn = sqlite3.connect('students.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE student
          ''')

conn.commit()
conn.close()
