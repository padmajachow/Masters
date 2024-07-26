# src/views/login_view.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db import connect
import mysql
# from controllers.bank_controller import BankController
# from controllers.login_controller import login_user

class CheckBalanceView(tk.Frame):
    def __init__(self, root=None, controller=None, username=None):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.username = username
        self.root.geometry("800x600+100+100")
        self.root.configure(bg="light blue")
        self.root.title("Balance Details")


        self.create_widgets()

         # Adding a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        # self.file_menu.add_command(label="Users Details", command=self.got_to_user_details)
        self.file_menu.add_command(label="User Home", command=self.go_to_home)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
    

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("account_no", "balance")  # Change column names accordingly
        self.tree.heading("account_no", text="Account Number")
        self.tree.heading("balance", text="balance")

        self.tree.pack(fill="both", expand=True)
        
        self.populate_treeview()


       
    
    def get_database_data(self):
        try:
            conn = connect()
            cursor = conn.cursor()
            query = f"SELECT account_no FROM users WHERE username='{self.username}'"
            cursor.execute(query)
            account_num = cursor.fetchone()
            account_num = account_num[0]
            if account_num:
                query = f"SELECT account_no, balance, update_date FROM accounts WHERE account_no='{account_num}'"
                cursor.execute(query)
                data = account_num = cursor.fetchall()
            return data
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error connecting to MySQL: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    def populate_treeview(self):
        data = self.get_database_data()
        for record in data:
            self.tree.insert("", "end", text=record[2], values=(record[0], record[1]))  # Adjust values accordingly

    def create_widgets(self):
        pass
   
    def show(self):
        self.root.deiconify()
    
    def hide(self):
        self.root.withdraw()
    
    def go_to_home(self):
        self.controller.show()
        self.hide()
    
    def got_to_user_details(self):
        pass

    def show(self):
        self.root.mainloop()


