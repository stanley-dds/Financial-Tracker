import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from database import create_connection

class App:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Financial Tracker")
        self.label.pack()

        self.add_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack()

        self.view_button = tk.Button(self.root, text="View Transactions", command=self.view_transactions)
        self.view_button.pack()

    def add_transaction(self):
        # Window for adding transactions
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Transaction")

        tk.Label(self.add_window, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
        self.date_entry = tk.Entry(self.add_window)
        self.date_entry.grid(row=0, column=1)

        tk.Label(self.add_window, text="Category:").grid(row=1, column=0)
        self.category_entry = tk.Entry(self.add_window)
        self.category_entry.grid(row=1, column=1)

        tk.Label(self.add_window, text="Amount:").grid(row=2, column=0)
        self.amount_entry = tk.Entry(self.add_window)
        self.amount_entry.grid(row=2, column=1)

        tk.Label(self.add_window, text="Type (Income/Expense):").grid(row=3, column=0)
        self.type_entry = tk.Entry(self.add_window) 
        self.type_entry.grid(row=3, column=1)

        self.save_button = tk.Button(self.add_window, text="Save", command=self.save_transaction)
        self.save_button.grid(row=4, columnspan=2)

    def save_transaction(self):
        # Saving transactions into our database
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        type_ = self.type_entry.get()

        conn = create_connection()
        with conn:
            conn.execute('''
                INSERT INTO transactions (date, category, amount, type)
                VALUES (?, ?, ?, ?)
            ''', (date, category, amount, type_))

        messagebox.showinfo("Success", "Transaction added successfully!")
        self.add_window.destroy()

    def view_transactions(self):
        # Window for browsing transactions
        self.view_window = tk.Toplevel(self.root)
        self.view_window.title("View Transactions")

        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT date, category, amount, type FROM transactions")
        rows = cur.fetchall()

        tree = ttk.Treeview(self.view_window, columns=("Date", "Category", "Amount", "Type"), show='headings')
        tree.heading("Date", text="Date")
        tree.heading("Category", text="Category")
        tree.heading("Amount", text="Amount")
        tree.heading("Type", text="Type")

        for row in rows:
            tree.insert("", tk.END, values=row)

        tree.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
