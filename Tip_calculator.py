import tkinter as tk

def calculate_tip():
    try:
        bill_amount = float(bill_entry.get())
        tip_percentage = float(tip_entry.get()) / 100
        people_count = int(people_entry.get())
        
        tip_amount = bill_amount * tip_percentage
        total_amount = bill_amount + tip_amount
        amount_per_person = total_amount / people_count
        
        result_label.config(text=f"Tip: ${tip_amount:.2f}, Total: ${total_amount:.2f}, Each person should pay: ${amount_per_person:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Tip Calculator")

# Create labels and entry fields
bill_label = tk.Label(window, text="Bill Amount:")
bill_entry = tk.Entry(window)
tip_label = tk.Label(window, text="Tip Percentage:")
tip_entry = tk.Entry(window)
people_label = tk.Label(window, text="Number of People:")
people_entry = tk.Entry(window)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_tip)

# Create result label
result_label = tk.Label(window, text="")

# Layout widgets using grid
bill_label.grid(row=0, column=0)
bill_entry.grid(row=0, column=1)
tip_label.grid(row=1, column=0)
tip_entry.grid(row=1, column=1)
people_label.grid(row=2, column=0)
people_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=1)
result_label.grid(row=4, columnspan=2)

# Start the main event loop
window.mainloop()