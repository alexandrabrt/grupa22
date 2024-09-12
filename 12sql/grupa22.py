import mysql.connector
from password import parola

my_db = mysql.connector.connect(
    database='grupa22',
    host='localhost',
    user='root',
    password=parola
)

# print(my_db)
cursor = my_db.cursor()
# try:
#     cursor.execute("CREATE DATABASE grupa22")
# except mysql.connector.errors.DatabaseError:
#     pass

# try:
#     cursor.execute('CREATE TABLE projects (id INT AUTO_INCREMENT PRIMARY KEY,'
#                    'name VARCHAR(255), '
#                    'address VARCHAR(255), '
#                    'project_number INTEGER)')
# except mysql.connector.errors.ProgrammingError:
#     pass

# try:
#     cursor.execute('ALTER TABLE projects ADD COLUMN varsta INTEGER')
# except mysql.connector.errors.ProgrammingError:
#     pass

# cursor.execute('ALTER TABLE projects DROP column varsta')
# sql = "INSERT INTO projects (name, address, project_number) VALUES (%s, %s, %s)"
# val = [
#     ('Petre', 'Bucuresti', 123),
#     ('Amalia', 'Ploiesti', 321),
#     ('Mihai', 'Bacau', 224)
# ]
# cursor.executemany(sql, val)
# my_db.commit()

sql = "UPDATE projects SET address='Bucuresti' where id=2"
cursor.execute(sql)
my_db.commit()
