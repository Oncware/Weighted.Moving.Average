import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def calculate():
    global df
    data = []
    initial_quantity = float(initial_quantity_entry.get())
    initial_price = initial_quantity * float(initial_unit_price_entry.get())
    for movement in movements:
        date, movement_type, quantity, unit_price = movement
        quantity = float(quantity)
        unit_price = float(unit_price)
        if movement_type == 'Entry':
            transaction_amount = quantity * unit_price
            current_quantity += quantity
            current_price += transaction_amount
        else:  # Exit
            transaction_amount = quantity * unit_price
            current_quantity -= quantity
            current_price -= transaction_amount
        current_unit_price = current_price / current_quantity if current_quantity > 0 else 0
        data.append([date, movement_type, quantity, unit_price, transaction_amount, current_quantity, current_unit_price, current_price])
    df = pd.DataFrame(data, columns=columns)
    df['Date'] = pd.to_datetime(df['Date'], format='%d.%m')
    df = df.sort_values(by='Date')

def show_results():
    new_window = tk.Toplevel(root)
    new_window.title("Result Table")
    sorted_df = df.sort_values(by='Date')  # Sort DataFrame by "Date" column
    tree = ttk.Treeview(new_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill='both', expand=True)
    for index, row in sorted_df.iterrows():  # Use the sorted DataFrame
        tree.insert("", "end", values=list(row))
    # Save button
    save_button = ttk.Button(new_window, text="Save Results", command=save_results)
    save_button.pack()

def save_results():
    file_name = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    df.to_csv(file_name, index=False)
    messagebox.showinfo("Success", f"Data successfully saved as {file_name}.")

def add_entry():
    date = entry_date.get()
    quantity = entry_quantity.get()
    unit_price = entry_unit_price.get()
    movements.append((date, 'Entry', quantity, unit_price))

def add_exit():
    date = exit_date.get()
    quantity = exit_quantity.get()
    unit_price = exit_unit_price.get()
    movements.append((date, 'Exit', quantity, unit_price))

columns = ["Date", "Movement Type", "Quantity (kg)", "Unit Price", "Transaction Amount", "Current Quantity (kg)", "Current Unit Price", "Current Price"]

movements = []

root = tk.Tk()
root.title("Stock Movements")

initial_quantity_entry = tk.StringVar()
initial_unit_price_entry = tk.StringVar()

entry_date = tk.StringVar()
entry_quantity = tk.StringVar()
entry_unit_price = tk.StringVar()

exit_date = tk.StringVar()
exit_quantity = tk.StringVar()
exit_unit_price = tk.StringVar()

# Initial inputs
tk.Label(root, text="Initial Quantity (kg):").grid(row=0, column=0)
tk.Entry(root, textvariable=initial_quantity_entry).grid(row=0, column=1)

tk.Label(root, text="Initial Unit Price:").grid(row=1, column=0)
tk.Entry(root, textvariable=initial_unit_price_entry).grid(row=1, column=1)

# Entry inputs
tk.Label(root, text="Entry Date (DD.MM):").grid(row=2, column=0)
tk.Entry(root, textvariable=entry_date).grid(row=2, column=1)

tk.Label(root, text="Entry Quantity (kg):").grid(row=3, column=0)
tk.Entry(root, textvariable=entry_quantity).grid(row=3, column=1)

tk.Label(root, text="Entry Unit Price:").grid(row=4, column=0)
tk.Entry(root, textvariable=entry_unit_price).grid(row=4, column=1)

tk.Button(root, text="Add Entry", command=add_entry).grid(row=5, column=1)

# Exit inputs
tk.Label(root, text="Exit Date (DD.MM):").grid(row=6, column=0)
tk.Entry(root, textvariable=exit_date).grid(row=6, column=1)

tk.Label(root, text="Exit Quantity (kg):").grid(row=7, column=0)
tk.Entry(root, textvariable=exit_quantity).grid(row=7, column=1)

tk.Label(root, text="Exit Unit Price:").grid(row=8, column=0)
tk.Entry(root, textvariable=exit_unit_price).grid(row=8, column=1)

tk.Button(root, text="Add Exit", command=add_exit).grid(row=9, column=1)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=10, column=0)

# Show results button
tk.Button(root, text="Show Results", command=show_results).grid(row=10, column=1)

root.mainloop()
