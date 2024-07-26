# src/db.py
import mysql.connector

def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="bank"
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
