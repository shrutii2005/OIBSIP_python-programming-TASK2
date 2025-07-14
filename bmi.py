# ADVANCED GUI BMI Calculator

import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt

data_file = "bmi_data.json"

def save_data(weight, height, bmi):
    entry = {"weight": weight, "height": height, "bmi": bmi}
    data = []
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            data = json.load(file)
    data.append(entry)
    with open(data_file, "w") as file:
        json.dump(data, file, indent=2)

def show_graph():
    if not os.path.exists(data_file):
        messagebox.showinfo("Info", "No data available to display.")
        return
    with open(data_file, "r") as file:
        data = json.load(file)
    bmis = [entry['bmi'] for entry in data]
    plt.plot(range(1, len(bmis)+1), bmis, marker='o')
    plt.title("BMI Over Time")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height <= 0:
            raise ValueError
        bmi = round(weight / (height ** 2), 2)
        result_label.config(text=f"Your BMI is: {bmi}")
        category = classify_bmi(bmi)
        category_label.config(text=f"Category: {category}")
        save_data(weight, height, bmi)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers.")

# GUI setup
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("300x300")

tk.Label(app, text="Enter your weight (kg):").pack()
weight_entry = tk.Entry(app)
weight_entry.pack()

tk.Label(app, text="Enter your height (m):").pack()
height_entry = tk.Entry(app)
height_entry.pack()

tk.Button(app, text="Calculate BMI", command=calculate).pack(pady=10)
result_label = tk.Label(app, text="")
result_label.pack()
category_label = tk.Label(app, text="")
category_label.pack()

tk.Button(app, text="Show BMI Graph", command=show_graph).pack(pady=5)

app.mainloop()
