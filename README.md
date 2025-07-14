# OIBSIP_python-programming-TASK2
# 🧮 BMI Calculator - Python Project

## 📝 Project Description

A simple yet powerful **BMI (Body Mass Index) Calculator** built with Python.

- 🧑‍💻 **For Beginners**: A command-line based BMI calculator that prompts the user for weight (in kilograms) and height (in meters), calculates the BMI, and categorizes the result (Underweight, Normal, Overweight, Obese) based on standard BMI ranges.

- 💻 **For Advanced Users**: A GUI-based BMI calculator using **Tkinter** or **PyQt**. Features include user input forms, real-time BMI calculation, graphical results, historical data storage, and statistical analysis via visual graphs.

---

## 🚀 Features

### ✅ Beginner Version
- Input weight and height via terminal
- BMI formula implementation: `BMI = weight / (height^2)`
- Classification based on BMI value
- Console output for result and category

### 🌟 Advanced Version
- GUI (Graphical User Interface) using Tkinter/PyQt
- Form validation for inputs
- BMI result display with category
- Historical data storage (e.g., JSON/SQLite)
- Graphical visualization (using `matplotlib` or similar)
- User-specific statistics and trends

---

## 🔑 Key Concepts & Challenges

1. **User Input Validation**  
   Ensure valid and realistic input values (e.g., height > 0) and error handling for wrong inputs.

2. **BMI Calculation**  
   Formula: `BMI = weight (kg) / height² (m²)`

3. **Categorization**  
   Based on WHO standards:
   - Underweight: BMI < 18.5
   - Normal: BMI 18.5 - 24.9
   - Overweight: BMI 25 - 29.9
   - Obese: BMI ≥ 30

4. **GUI Design (Advanced)**  
   Clean layout with input fields, result section, and buttons for interaction.

5. **Data Storage (Advanced)**  
   Use **JSON**, **CSV**, or **SQLite** for saving user data across sessions.

6. **Data Visualization (Advanced)**  
   Use libraries like `matplotlib` or `seaborn` to show BMI history via line or bar graphs.

7. **Error Handling (Advanced)**  
   Graceful handling of input/output errors, missing files, or invalid data formats.

8. **User Experience (Advanced)**  
   Focus on responsive design, helpful instructions, and smooth interaction.

---

## 📦 Technologies Used

- Python 3.x
- Tkinter / PyQt (GUI)
- SQLite / JSON (Data Storage)
- matplotlib / seaborn (Graphs)
- argparse or input() for CLI version

---

## 🛠 How to Run

### ▶ Beginner CLI Version:
```bash
python bmi_calculator.py
