# src/controllers/register_controller.py
from tkinter import messagebox
from db import connect
import mysql
from controllers.admin_controller import AdminController
from controllers.user_controller import UserController
def login_user(username, password):
    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter required fileds")
        return

    try:
        conn = connect()
        cursor = conn.cursor()
        if username == "admin" and password == "admin":
            controller = AdminController()
            return 1
        else:
            cursor.execute("SELECT * FROM users WHERE username = %s and pwd = %s", (username,password))
            if cursor.fetchone():
                # Need to write code for user
                controller = UserController(username)
                return 1

           
            messagebox.showinfo("Login Failed", "Incorrect UserName/Passsword")
            conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error connecting to MySQL: {e}")
