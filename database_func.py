import sqlite3
from user import User


def create_database():
    conn = sqlite3.connect('quiz_database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS 
                users(
                      user_name VarChar(50) Primary Key,
                      password VarChar(50) NOT NULL,
                      points INTEGER NOT NULL)
    """)
    conn.commit()
    conn.close()


def create_user(name, password):
    conn = sqlite3.connect('quiz_database.db')
    c = conn.cursor()
    c.execute("""INSERT INTO users(user_name, password, points)
    VALUES(?, ?, ?)""", (name, password, 135))
    conn.commit()
    conn.close()


def get_user(user_name, password):
    conn = sqlite3.connect('quiz_database.db')
    try:
        c = conn.cursor()
        c.execute(f"""SELECT * FROM users WHERE user_name = '{user_name}' """)
        user = c.fetchone()
        if user:
            if user[1] == password:
                user = User(user[0], user[1], user[2])
                return user
            else:
                return 'Wrong password'
        else:
            return 'User does not exist'
    finally:
        conn.close()


def update_user(user):
    conn = sqlite3.connect('quiz_database.db')
    try:
        c = conn.cursor()
        c.execute(f"""UPDATE users SET points = {user.points} WHERE user_name = '{user.name}' """)
        conn.commit()
    finally:
        conn.close()