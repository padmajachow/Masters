# src/views/register_view.py
import tkinter as tk
from tkinter import messagebox
from controllers.register_controller import register_user

class RegisterView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.master.geometry("800x600+100+100")
        self.master.configure(bg="light blue")
        self.master.title("User Registration")
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
        self.username_label.grid(row=0, column=50, padx=10, pady=5)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=51, padx=10, pady=5)
        

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.grid(row=1, column=50, padx=10, pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=51, padx=10, pady=5)

        self.contact_label = tk.Label(self.master, text="Contact No:")
        self.contact_label.grid(row=2, column=50, padx=10, pady=5)
        self.contact_entry = tk.Entry(self.master)
        self.contact_entry.grid(row=2, column=51, padx=10, pady=5)

        self.house_label = tk.Label(self.master, text="House No:")
        self.house_label.grid(row=3, column=50, padx=10, pady=5)
        self.house_entry = tk.Entry(self.master)
        self.house_entry.grid(row=3, column=51, padx=10, pady=5)

        self.area_label = tk.Label(self.master, text="Street:")
        self.area_label.grid(row=4, column=50, padx=10, pady=5)
        self.area_entry = tk.Entry(self.master)
        self.area_entry.grid(row=4, column=51, padx=10, pady=5)

        self.land_label = tk.Label(self.master, text="Apartment No:")
        self.land_label.grid(row=5, column=50, padx=10, pady=5)
        self.land_entry = tk.Entry(self.master)
        self.land_entry.grid(row=5, column=51, padx=10, pady=5)

        self.city_label = tk.Label(self.master, text="City:")
        self.city_label.grid(row=6, column=50, padx=10, pady=5)
        self.city_entry = tk.Entry(self.master)
        self.city_entry.grid(row=6, column=51, padx=10, pady=5)

        self.state_label = tk.Label(self.master, text="State:")
        self.state_label.grid(row=7, column=50, padx=10, pady=5)
        self.state_entry = tk.Entry(self.master)
        self.state_entry.grid(row=7, column=51, padx=10, pady=5)

        self.pin_label = tk.Label(self.master, text="PIN Code:")
        self.pin_label.grid(row=8, column=50, padx=10, pady=5)
        self.pin_entry = tk.Entry(self.master)
        self.pin_entry.grid(row=8, column=51, padx=10, pady=5)

        self.register_button = tk.Button(self.master, text="Register", command=self.register)
        self.register_button.grid(row=11, column=50, columnspan=2, pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        contact = self.contact_entry.get()
        house_no = self.contact_entry.get()
        street = self.area_entry.get()
        land_mark = self.land_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        pin_code = self.pin_entry.get()

        register_user(username, password, contact, house_no, street, land_mark, city, state, pin_code)
    
    def show(self):
        self.master.deiconify()
    
    def hide(self):
        self.master.withdraw()
    
    def go_to_home(self):
        self.controller.show_home_page()
