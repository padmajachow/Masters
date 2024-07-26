# controller.py
# from views.register_view import RegisterView
# from views.login_view import LoginView
from views.admin_view import AdminView
# from model.bank_model import BankModel
import tkinter as tk
from model.admin_model import AdminModel

class AdminController:
    def __init__(self):
        print("INIT in admin controller")
        self.root = tk.Tk()
        self.model = AdminModel()
        self.root.geometry("800x600+100+100")

        # Initialize views
        self.home_page = AdminView(self.root, self)
        # self.register_page = RegisterView(tk.Toplevel(), self)
        # self.login_page = LoginView(tk.Toplevel(), self)

        # Initially hide other pages
        # self.hide_other_page()

        # Show home page
        self.show_home_page()

    def show_home_page(self):
        # self.hide_other_page()
        if not self.home_page:
            print("Admin Home inside if")
            self.home_page = AdminView(self.root, self)
        else:
             print("Admin home outside else")
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

