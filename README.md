# Tip Calculator with Split Bill

This is a simple tip calculator application built using Python's Tkinter library. It allows users to calculate the tip amount, total bill, and split the bill among multiple people.

## Features

* Calculates the tip amount based on the bill amount and tip percentage.
* Calculates the total bill amount (bill + tip).
* Splits the total bill evenly among a specified number of people.
* Provides error handling for invalid input.
* Simple and user-friendly GUI.

## How to Use

1.  **Prerequisites:**
    * Python 3.x installed on your system.
2.  **Run the application:**
    * Save the Python code to a file (e.g., `tip_calculator.py`).
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the file.
    * Run the command: `python tip_calculator.py`
3.  **Using the GUI:**
    * Enter the bill amount in the "Bill Amount" field.
    * Enter the tip percentage in the "Tip Percentage" field.
    * Enter the number of people splitting the bill in the "Number of People" field.
    * Click the "Calculate" button.
    * The calculated tip, total bill, and amount per person will be displayed below the button.
    * If you enter invalid inputs, an error message will display.

## Code Description

The code uses the Tkinter library to create a graphical user interface. The `calculate_tip()` function performs the calculations based on the user's input. The GUI includes labels, entry fields, and a button to trigger the calculation. Input validation is implemented to handle non-numeric inputs.

## Code Structure

```python
import tkinter as tk

def calculate_tip():
    # Calculation logic here

# Create the main window
window = tk.Tk()

# Create labels and entry fields
# Create calculate button
# Create result label

# Layout widgets using grid
# Start the main event loop
window.mainloop()
