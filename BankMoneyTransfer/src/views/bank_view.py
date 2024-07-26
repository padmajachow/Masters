# home_page.py
import tkinter as tk

class HomePageView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Creating the main window
        self.root.title("Home Page")
        self.root.configure(bg="light blue")

        # Adding a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Registration", command=self.controller.show_register_page)
        self.file_menu.add_command(label="Login", command=self.controller.show_login_page)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Home Page content
        self.label = tk.Label(root, text="Welcome to BanK App", font=('Helvetica', 18))
        self.label.pack(pady=20)

    def show(self):
        self.root.mainloop()