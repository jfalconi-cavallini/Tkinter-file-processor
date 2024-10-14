import tkinter as tk
import csv

def loadFile(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        return next(reader)

def buttonClicked():
    filename = entry.get()
    try:
        first_row = loadFile(filename)
        displayData(first_row)
    except FileNotFoundError:
        displayError("File not found. Please enter a valid filename.")

def displayData(first_row):
    # Create a new window
    data_window = tk.Toplevel(root)
    data_window.title("First Row Data")
    
    # Display the first row in a label
    row_label = tk.Label(data_window, text=f"First Row: {first_row}", font=("Helvetica", 14))
    row_label.pack(pady=20)
    
    # Close button for the new window
    close_button = tk.Button(data_window, text="Close", command=data_window.destroy)
    close_button.pack(pady=10)

def displayError(message):
    # Create a new window for error message
    error_window = tk.Toplevel(root)
    error_window.title("Error")

    # Display the error message in a label
    error_label = tk.Label(error_window, text=message, fg="red", font=("Helvetica", 14))
    error_label.pack(pady=20)

    # Close button for the error window
    close_button = tk.Button(error_window, text="Close", command=error_window.destroy)
    close_button.pack(pady=10)

# Set up the main window
root = tk.Tk()
root.title("Filename Processor")

# Entry field for filename
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Load button
load_button = tk.Button(root, text="Load File", command=buttonClicked)
load_button.pack(pady=10)

# Start the main event loop
root.mainloop()
