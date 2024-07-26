from tkinter import messagebox
import tkinter as tk
from db import connect
import mysql
from views.user_view import UserView

class UserController:
    def __init__(self, username):
        print("User Controller")
        self.root = tk.Tk()
        self.root.geometry("800x600+100+100")
        self.username = username


        # Initialize views
        self.home_page = UserView(self.root, self, self.username)
        # self.register_page = RegisterView(tk.Toplevel(), self)
        # self.login_page = LoginView(tk.Toplevel(), self)

        # Initially hide other pages
        # self.hide_other_page()

        # Show home page
        self.show_home_page()

    def show_home_page(self):
        # self.hide_other_page()
        if not self.home_page:
            print("User Home inside if")
            self.home_page = UserView(self.root, self)
        else:
             print("User Home outside else")
             self.home_page.root.deiconify()
        # self.home_page.show()
    
    def hide_other_page(self):
        # self.register_page.master.withdraw()
        # self.login_page.master.withdraw()
        pass
    
    def hide_home_page(self):
        self.home_page.root.withdraw()
    
    def show(self):
        self.root.mainloop()