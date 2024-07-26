# src/views/login_view.py
import tkinter as tk
from tkinter import messagebox
# from controllers.bank_controller import BankController
# from controllers.login_controller import login_user
from views.add_money_view import AddMoneyView
from views.check_balance_view import CheckBalanceView
from views.transfer_money import TransferMoneyView

class UserView(tk.Frame):
    def __init__(self, root=None, controller=None, username=None):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.username = username
        print("UserView",self.username)
        self.root.geometry("800x600+100+100")
        self.root.configure(bg="light blue")
        self.root.title("User Home")
        self.add_money_view = AddMoneyView(tk.Toplevel(), self, self.username)
        self.add_money_view.hide()
        self.transfer_money_view = TransferMoneyView(tk.Toplevel(), self, self.username)
        self.transfer_money_view.hide()
        self.check_balance_view = CheckBalanceView(tk.Toplevel(), self, self.username)
        self.check_balance_view.hide()
        self.create_widgets()
        self.label = tk.Label(root, text="Welcome to Central Michingan University Student Bank", font=('Helvetica', 18))
        self.label.pack(pady=20)



        # Adding a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Add Money", command=self.got_to_add_money_page)
        self.file_menu.add_command(label="Transfer Money", command=self.got_to_transfer_money_page)
        self.file_menu.add_command(label="Balance", command=self.got_to_check_balance_page)
        self.file_menu.add_command(label="Logout", command=self.go_to_home)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        

    def create_widgets(self):
        pass
   
    def show(self):
        self.root.deiconify()
    
    def hide(self):
        self.root.withdraw()
    
    def go_to_home(self):
        self.controller.show_home_page()
        self.hide()
    
    def got_to_add_money_page(self):
        if not self.add_money_view:
            self.add_money_view = AddMoneyView(tk.Toplevel(), self, self.username)
        else:
             self.add_money_view.master.deiconify()
        self.hide()
    
    def got_to_transfer_money_page(self):
        if not self.transfer_money_view:
            self.transfer_money_view = TransferMoneyView(tk.Toplevel(), self, self.username)
        else:
             self.transfer_money_view.master.deiconify()
        self.hide()
    
    def got_to_check_balance_page(self):
        if not self.check_balance_view:
            self.check_balance_view = CheckBalanceView(tk.Toplevel(), self, self.username)
        else:
             self.check_balance_view.master.deiconify()
        self.hide()



