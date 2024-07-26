# src/main.py
import tkinter as tk
# from views.register_view import RegisterView
# from views.bank_view import BankView
# from controllers.register_controller import register_user
# from controllers.login_controller import login_user
from controllers.bank_controller import BankController
def main():
    # root = tk.Tk()
    # Set window size to 800x600+100+100 pixels
    # root.geometry("800x600+100+100")
    # app = RegisterView(master=root)
    # app = BankView(master=root, register_controller=register_user, login_controller=login_user)
    # app.mainloop()
    controller = BankController()
    controller.root.mainloop()

if __name__ == "__main__":
    main()
