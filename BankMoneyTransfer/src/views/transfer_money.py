# src/views/login_view.py
import tkinter as tk
from tkinter import messagebox
from db import connect
import mysql
# from controllers.add_money_controller import add_money_to_acc

class TransferMoneyView(tk.Frame):
    def __init__(self, master=None, controller=None, username=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.username = username
        print("TransferMoneyView:", self.username)
        self.master.geometry("800x600+100+100")
        self.master.configure(bg="light blue")
        self.master.title("Transfer Money")
        self.create_widgets()

        # Adding a menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Home", command=self.go_to_home)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        

    def create_widgets(self):
        self.account_label = tk.Label(self.master, text="Account Number:")
        self.account_label.grid(row=0, column=50, padx=10, pady=5)
        self.account_entry = tk.Entry(self.master)
        self.account_entry.grid(row=0, column=51, padx=10, pady=5)

        self.bank_name_label = tk.Label(self.master, text="Bank Name:")
        self.bank_name_label.grid(row=1, column=50, padx=10, pady=5)
        self.bank_name_entry = tk.Entry(self.master)
        self.bank_name_entry.grid(row=1, column=51, padx=10, pady=5)
        
        self.ifsc_label = tk.Label(self.master, text="IFSC Code:")
        self.ifsc_label.grid(row=2, column=50, padx=10, pady=5)
        self.ifsc_entry = tk.Entry(self.master)
        self.ifsc_entry.grid(row=2, column=51, padx=10, pady=5)

        self.money_label = tk.Label(self.master, text="Money in INR:")
        self.money_label.grid(row=3, column=50, padx=10, pady=5)
        self.money_entry = tk.Entry(self.master)
        self.money_entry.grid(row=3, column=51, padx=10, pady=5)

        self.register_button = tk.Button(self.master, text="Transfer", command=self.transfer_money)
        self.register_button.grid(row=6, column=50, columnspan=2, pady=10)

    def transfer_money(self):
        transfer_account_num = self.account_entry.get()
        bank_name = self.bank_name_entry.get()
        ifsc_code = self.ifsc_entry.get()
        money = self.money_entry.get()
        print("Money:", money)

        # Need to write code here
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
                if old_balance != None and old_balance >= float(money):
                    current_balance = old_balance - float(money)
                    print(current_balance)
                    transfer_to = transfer_account_num + " " + bank_name + " " + ifsc_code
                    query = f"INSERT INTO transaction_history (account_no, old_balance, current_balance, amount, status, transfer_to) VALUES ('{account_no}', '{old_balance}', '{current_balance}', '{money}','Debit', '{transfer_to}')"
                    print(query)
                    cursor.execute(query)
                    query = f"UPDATE accounts SET balance = '{current_balance}' WHERE account_no = '{account_no}'"
                    print(query)
                    cursor.execute(query)
                    conn.commit()
                    message = f"Your current balance is: {current_balance}"
                    messagebox.showinfo("Success", message)
                    conn.close()
                else:
                    message = "Insufficient Amount in your account"
                    messagebox.showinfo("Insufficient", message)
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
        self.controller.show()
        self.hide()

