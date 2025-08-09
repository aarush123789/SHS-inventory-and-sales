import tkinter as tk
from tkinter import messagebox
from services.user_services import login_user

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Login", font=("Arial", 34)).pack(pady=10)

        tk.Label(self, text="Username", font=("Times New Roman", 18)).pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password", font=("Times New Roman", 18)).pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack(pady=10)
        tk.Button(self, text="Don't have an account? Sign Up",font=("Times New Roman", 18), command=self.go_to_signup).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = login_user(username, password)
        if user:
            messagebox.showinfo("Login Success", "Welcome, " + username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def go_to_signup(self):
        self.controller.show_frame("SignupPage")
