import tkinter as tk

from view.login_page import LoginPage
from view.signup_page import SignupPage
from config.db import SQLHandler 

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SHS INVENTORY AND SALES")
        self.geometry("1000x600")
        self.resizable(False, False)

        # Container to hold all frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        # Register all pages here
        for PageClass in (LoginPage, SignupPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        """Raise the frame with the given name."""
        frame = self.frames[page_name]
        frame.tkraise()

def main():
    # run the DB handler to ensure the database is setup.
    try:
        print("🔄 Checking database setup...")
        SQLHandler()
        print("✅ Database connected and initialized.")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
