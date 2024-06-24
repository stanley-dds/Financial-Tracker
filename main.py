import tkinter as tki
from database import create_connection, create_tables
import ui

def main():
    # Connecting to db and creating tables
    conn = create_connection()
    create_tables(conn)
    conn.close()

    # Creating main window of the app
    root = tki.Tk()
    root.title("Financial Tracker")

    # Initialization of User interface
    app = ui.App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
