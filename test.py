import tkinter as tk
import time
def update_window():
    # Update the label text or perform other UI updates here
    time_label.config(text="Updating...")

    # Call update_idletasks to force the updates to be displayed
    root.update_idletasks()
    # Schedule the next update after 1 second
    root.after(1000, update_window)

# Create the root window
root = tk.Tk()
root.geometry('200x100')

# Create a label
time_label = tk.Label(root, text="Initial text")
time_label.pack()

# Start the periodic update
root.after(10000, update_window)

# Start the main event loop
root.mainloop()