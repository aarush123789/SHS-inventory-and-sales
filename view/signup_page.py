import tkinter as tk
from tkinter import messagebox
from services.user_services import register_user

class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Sign Up", font=("Arial", 16)).pack(pady=10)

        self.entries = {}

        for label in ["Username", "Email", "Password", "Contact", "Address"]:
            tk.Label(self, text=label).pack()
            entry = tk.Entry(self, show="*" if label == "Password" else None)
            entry.pack()
            self.entries[label] = entry

        tk.Button(self, text="Register", command=self.register).pack(pady=10)
        tk.Button(self, text="Back to Login", command=self.go_to_login).pack()

    def register(self):
        data = {k: v.get() for k, v in self.entries.items()}
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required.")
            return

        success = register_user(
            data["Username"],
            data["Email"],
            data["Password"],
            data["Contact"],
            data["Address"]
        )

        if success:
            messagebox.showinfo("Success", "Registration successful.. Please login.")
            self.clear_form()
            self.controller.show_frame("LoginPage")
        else:
            messagebox.showerror("Error", "Username or email already exists.")

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def go_to_login(self):
        self.controller.show_frame("LoginPage")
