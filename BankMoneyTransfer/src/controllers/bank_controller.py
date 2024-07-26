# controller.py
from views.register_view import RegisterView
from views.login_view import LoginView
from views.bank_view import HomePageView
from model.bank_model import BankModel
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class BankController:
    def __init__(self):
        self.root = tk.Tk()
        self.model = BankModel()
        self.root.geometry("800x600+100+100")
        self.root.configure(bg="light blue")
        self.image = Image.open("./assets/images/bank_bg_image.jpg")
        self.bg_image = ImageTk.PhotoImage(self.image)
        # Create a label with the image as its background
        background_label = tk.Label(self.root, image=self.bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Initialize views
        self.home_page = HomePageView(self.root, self)
        self.register_page = RegisterView(tk.Toplevel(), self)
        self.login_page = LoginView(tk.Toplevel(), self)

        # Initially hide other pages
        self.hide_other_page()

        # Show home page
        self.show_home_page()

    def show_home_page(self):
        self.hide_other_page()
        if not self.home_page:
            self.home_page = HomePageView(self.root, self)
        else:
             self.home_page.root.deiconify()
        # self.home_page.show()

    def show_register_page(self):
        if not self.register_page:
            self.register_page = RegisterView(tk.Toplevel(self.root), self)
        else:
             self.register_page.master.deiconify()
        self.hide_home_page()
        # self.register_page.show()

        # self.register_page.show()
    
    def show_login_page(self):
        if not self.login_page:
            self.login_page = LoginView(tk.Toplevel(self.root), self)
        else:
             self.login_page.master.deiconify()
        self.hide_home_page()
    
    def hide_other_page(self):
        self.register_page.master.withdraw()
        self.login_page.master.withdraw()
    
    def hide_home_page(self):
        self.home_page.root.withdraw()
    
    def show(self):
        self.root.mainloop()

