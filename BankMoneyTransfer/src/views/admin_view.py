# src/views/login_view.py
import tkinter as tk
from tkinter import messagebox
# from controllers.bank_controller import BankController
# from controllers.login_controller import login_user
from views.user_details_view import UserDetailsView

class AdminView(tk.Frame):
    def __init__(self, root=None, controller=None):
        super().__init__(root)
        self.root = root
        self.controller = controller
        self.root.geometry("800x600+100+100")
        self.root.configure(bg="light blue")
        self.root.title("Admin Home")
        self.user_details_page = UserDetailsView(tk.Toplevel(), self)
        self.user_details_page.hide()
        self.create_widgets()


        # Adding a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Users Details", command=self.got_to_user_details)
        self.file_menu.add_command(label="Logout", command=self.go_to_home)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.label = tk.Label(root, text="Welcome to Central Michingan University Student Bank", font=('Helvetica', 18))
        self.label.pack(pady=20)

    def create_widgets(self):
        pass
   
    def show(self):
        self.root.deiconify()
    
    def hide(self):
        self.root.withdraw()
    
    def go_to_home(self):
        self.controller.show_home_page()
        self.hide()
    
    def got_to_user_details(self):
        if not self.user_details_page:
            self.user_details_page = UserDetailsView(tk.Toplevel(self.root), self)
        else:
             self.user_details_page.master.deiconify()
        self.hide()



