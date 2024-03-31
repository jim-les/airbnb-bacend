import mysql.connector
from mysql.connector import Error
from fastapi import HTTPException
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    email: str
    full_name: str

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='zantrik.cluy0icsgtj9.us-east-1.rds.amazonaws.com',
            database='sports',
            user='admin',
            password='admin123'
        )

        if connection.is_connected():
            return connection
        
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

def create_user(user: User):
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, email, full_name) VALUES (%s, %s, %s, %s)",
                       (user.username, user.password, user.email, user.full_name))
        connection.commit()
        return user
    except Error as e:
        print(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Error creating user")
    finally:
        cursor.close()
        connection.close()

def get_user(username: str):
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        return user
    except Error as e:
        print(f"Error getting user: {e}")
        raise HTTPException(status_code=500, detail="Error getting user")
    finally:
        cursor.close()
        connection.close()
