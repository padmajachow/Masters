# src/views/login_view.py
import tkinter as tk
from tkinter import messagebox
from controllers.login_controller import login_user
from tkinter import PhotoImage
from PIL import Image, ImageTk

class LoginView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.master.geometry("800x600+100+100")
        self.master.configure(bg="light blue")
        self.master.title("User Login")

        self.image = Image.open("./assets/images/login.jpg")
        self.bg_image = ImageTk.PhotoImage(self.image)
        # Create a label with the image as its background
        background_label = tk.Label(self.master, image=self.bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

        # Adding a menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Home", command=self.go_to_home)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        

    def create_widgets(self):
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.register_button = tk.Button(self.master, text="Login", command=self.login)
        self.register_button.grid(row=11, column=1, columnspan=5, pady=10)

        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=0)
        self.master.rowconfigure(1, weight=0)
        self.master.rowconfigure(11, weight=0)


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        check = login_user(username, password)
        if check == 1:
            self.hide()

    def show(self):
        self.master.deiconify()
    
    def hide(self):
        self.master.withdraw()
    
    def go_to_home(self):
        self.controller.show_home_page()
        self.hide()

