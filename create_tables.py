import sqlite3

conn = sqlite3.connect('students.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE student
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(250) NOT NULL,
           program VARCHAR(300) NOT NULL,
           classification VARCHAR(20) NOT NULL,
           enroll_status VARCHAR(10) NOT NULL,
           enroll_date VARCHAR(50) NOT NULL,
           type VARCHAR(30) NOT NULL,
           minor VARCHAR(300),
           min_credit INTEGER(3),
           supervisor VARCHAR(250),
           undergrad_degree VARCHAR(300)
           )
          ''')

conn.commit()
conn.close()
