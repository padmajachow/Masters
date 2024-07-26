# controller.py
# from views.register_view import RegisterView
# from views.login_view import LoginView
from views.admin_view import AdminView
# from model.bank_model import BankModel
import tkinter as tk
from views.user_details_view import UserDetailsView

class UserDetailsController:
    def __init__(self):
        print("INIT in user details controller")
        self.root = tk.Tk()
        self.root.geometry("800x600+100+100")
        self.root.title("User Details")

        # Initialize views
        self.home_page = UserDetailsView(self.root, self)
        # self.register_page = RegisterView(tk.Toplevel(), self)
        # self.login_page = LoginView(tk.Toplevel(), self)

        # Initially hide other pages
        # self.hide_other_page()

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("column1", "column2", "column3")  # Change column names accordingly
        self.tree.heading("#0", text="ID")
        self.tree.heading("column1", text="Column 1")
        self.tree.heading("column2", text="Column 2")
        self.tree.heading("column3", text="Column 3")
        self.tree.pack(fill="both", expand=True)

        # Show home page
        self.show_home_page()


    def show_home_page(self):
        # self.hide_other_page()
        if not self.home_page:
            print("User Details inside if")
            self.home_page = AdminView(self.root, self)
        else:
             print("User Details outside else")
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

