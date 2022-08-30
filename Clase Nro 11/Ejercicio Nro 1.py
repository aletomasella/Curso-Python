import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_student(conn, student):
    sql = ''' INSERT INTO students(first_name, last_name, age)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    return cur.lastrowid

def get_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return rows

def get_student(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    row = cur.fetchone()
    return row

def delete_student(conn, id):
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    return cur.rowcount


conn = create_connection(r"./data/sqlite3.db")
print(conn)

students_table ="""CREATE TABLE IF NOT EXISTS
                                students (id integer PRIMARY KEY, first_name text,
                                last_name text, age integer)"""

if conn is not None:
    create_table(conn, students_table)


def user_input():
    first_name = input("Enter student first name: ")
    last_name = input("Enter student last name: ")
    age = input("Enter student age: ")
    return (first_name, last_name, age)


while True:
    print("1. Insert student")
    print("2. Get students")
    print("3. Get student")
    print("4. Delete student")
    print("5. Exit")

    option = input("Enter option: ")

    if option == "1":
        student = user_input()
        create_student(conn, student)
        print("Student added successfully")
    elif option == "2":
        students = get_students(conn)
        print("All students:")
        for student in students:
            print(student)
    elif option == "3":
        id = int(input("Enter student id: "))
        student = get_student(conn, id)
        if student is not None:
            print(student)
        else:
            print("Student not found")
    elif option == "4":
        id = int(input("Enter student id: "))
        delete_student(conn, id)
        print("Student deleted successfully")
    elif option == "5":
        conn.close()
        break
    else:
        print("Invalid option")
        break














