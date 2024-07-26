# src/views/login_view.py
import tkinter as tk
from tkinter import messagebox
from db import connect
import mysql
# from controllers.add_money_controller import add_money_to_acc

class AddMoneyView(tk.Frame):
    def __init__(self, master=None, controller=None, username=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.username = username
        print("AddMoneyView:", self.username)
        self.master.geometry("800x600+100+100")
        self.master.configure(bg="light blue")
        self.master.title("Add Money")
        self.create_widgets()

        # Adding a menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Home", command=self.go_to_home)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        

    def create_widgets(self):
        self.money_label = tk.Label(self.master, text="Add Money in INR:")
        self.money_label.grid(row=0, column=50, padx=10, pady=5)
        self.money_entry = tk.Entry(self.master)
        self.money_entry.grid(row=0, column=51, padx=10, pady=5)
        

        self.register_button = tk.Button(self.master, text="Add", command=self.add_money)
        self.register_button.grid(row=11, column=50, columnspan=2, pady=10)

    def add_money(self):
        money = self.money_entry.get()
        print("Money:", money)
        try:
            conn = connect()
            cursor = conn.cursor()
            query = f"SELECT account_no FROM users WHERE username = '{self.username}'"
            print(query)
            cursor.execute(query)
            account_no = cursor.fetchone()
            account_no = account_no[0]
            if account_no:
                print(account_no)
                query = f"SELECT balance FROM accounts WHERE account_no = '{account_no}'"
                print(query)
                cursor.execute(query)
                old_balance = cursor.fetchone()
                old_balance = old_balance[0]
                if old_balance != None:
                    current_balance = old_balance + float(money)
                    print(current_balance)
                    query = f"INSERT INTO transaction_history (account_no, old_balance, current_balance, amount, status) VALUES ('{account_no}', '{old_balance}', '{current_balance}', '{money}','Deposit')"
                    print(query)
                    cursor.execute(query)
                    query = f"UPDATE accounts SET balance = '{current_balance}' WHERE account_no = '{account_no}'"
                    print(query)
                    cursor.execute(query)
                    conn.commit()
                    message = f"Your current balance is: {current_balance}"
                    messagebox.showinfo("Success", message)
                    conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error connecting to MySQL: {e}")

        # check = add_money_to_acc(money)
        # if check == 1:
        #     self.hide()

    def show(self):
        self.master.deiconify()
    
    def hide(self):
        self.master.withdraw()
    
    def go_to_home(self):
        self.hide()
        self.controller.show()
        

