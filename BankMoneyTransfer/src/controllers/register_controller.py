# src/controllers/register_controller.py
from tkinter import messagebox
from db import connect
import mysql
import calendar
import datetime

def register_user(username, password, contact, house_no, street, land_mark, city, state, pin_code):
    if username == "" or password == "" or contact == "" or house_no=="" or street=="" or land_mark=="" or city=="" or state=="" or  pin_code=="":
        messagebox.showerror("Error", "Please enter required fileds")
        return

    try:
        conn = connect()
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}'"
        print(query)

        cursor.execute(query)
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists")
            return
        date = datetime.datetime.utcnow()
        balance = 0
        account_number = int(calendar.timegm(date.utctimetuple())*10)
        query=f"INSERT INTO users (username, pwd, contact, house_no, street, land_mark, city, state, pin_code, account_no) VALUES ('{username}', '{password}', '{contact}', '{house_no}', '{street}', '{land_mark}', '{city}', '{state}', '{pin_code}', '{account_number}')"
        query1=f"INSERT INTO accounts (account_no, balance) VALUES ('{account_number}', {balance})"
        print(query)

        cursor.execute(query)
        cursor.execute(query1)
        conn.commit()
        messagebox.showinfo("Success", "Registration successful")
        conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL: {e}")
