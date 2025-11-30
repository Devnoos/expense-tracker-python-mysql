import mysql.connector as sql

def get_connection():
    conn= sql.connect(
        host="localhost",
        user="root",
        password="",
        db="expense_tracker"
    )
    return conn
