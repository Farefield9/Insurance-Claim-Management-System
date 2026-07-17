import tkinter as tk
from tkinter import messagebox
from db import get_connection
import dashboard


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Warning",
            "Please enter username and password"
        )
        return

    conn = get_connection()

    if conn:
        cursor = conn.cursor()

        query = """
        SELECT * FROM users 
        WHERE username=%s AND password=%s
        """

        cursor.execute(query, (username, password))

        result = cursor.fetchone()

        conn.close()

        if result:
            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            root.destroy()

            dashboard.open_dashboard()

        else:
            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Insurance Claim System - Login")
root.geometry("400x300")
root.resizable(False, False)


title = tk.Label(
    root,
    text="Insurance Claim Management System",
    font=("Arial", 14, "bold")
)

title.pack(pady=20)


username_label = tk.Label(
    root,
    text="Username"
)

username_label.pack()


username_entry = tk.Entry(
    root,
    width=30
)

username_entry.pack(pady=5)


password_label = tk.Label(
    root,
    text="Password"
)

password_label.pack()


password_entry = tk.Entry(
    root,
    width=30,
    show="*"
)

password_entry.pack(pady=5)



login_button = tk.Button(
    root,
    text="Login",
    width=15,
    command=login
)

login_button.pack(pady=20)


root.mainloop()
