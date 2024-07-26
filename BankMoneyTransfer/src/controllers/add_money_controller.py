# src/controllers/register_controller.py
from tkinter import messagebox
import tkinter as tk
from db import connect
import mysql
from views.add_money_view import AddMoneyView

class AddMoneyController:
    def __init__(self):
        print("Add Money controller")
        self.root = tk.Tk()
        self.root.geometry("800x600+100+100")

        # Initialize views
        self.home_page = AddMoneyView(self.root, self)
        # self.register_page = RegisterView(tk.Toplevel(), self)
        # self.login_page = LoginView(tk.Toplevel(), self)

        # Initially hide other pages
        # self.hide_other_page()

        # Show home page
        self.show_home_page()

    def show_home_page(self):
        # self.hide_other_page()
        if not self.home_page:
            print("Add Money inside if")
            self.home_page = AddMoneyView(self.root, self)
        else:
             print("Add Money outside else")
             self.home_page.master.deiconify()
        # self.home_page.show()
    
    def hide_other_page(self):
        # self.register_page.master.withdraw()
        # self.login_page.master.withdraw()
        pass
    
    def hide_home_page(self):
        self.home_page.root.withdraw()
    
    def show(self):
        self.root.mainloop()



# def login_user(username, password):
#     if username == "" or password == "":
#         messagebox.showerror("Error", "Please enter required fileds")
#         return

#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         if username == "admin" and password == "admin":
#             controller = AdminController()
#             return 1
#         else:
#             cursor.execute("SELECT * FROM users WHERE username = %s and pwd = %s", (username,password))
#             if cursor.fetchone():
#                 # Need to write code for user
#                 return

#             cursor.execute("INSERT INTO users (username, password, contact, house_no, street, land_mark, city, state, pin_code) VALUES (%s, %s)", (username, password, contact, house_no, street, land_mark, city, state, pin_code))
#             conn.commit()
#             messagebox.showinfo("Success", "Registration successful")
#             conn.close()

#     except mysql.connector.Error as e:
#         messagebox.showerror("Error", f"Error connecting to MySQL: {e}")
