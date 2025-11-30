<<<<<<< HEAD
# Expense Tracker

A simple console-based Expense Tracker application to manage personal expenses.  
Allows adding, viewing, updating, and calculating total expenses using Python and MySQL.

---

## Features

- **Add Expense** – Enter category, description, and amount.  
- **View Expenses** – See all recorded expenses in a tabular format.  
- **Update Expense** – Modify amount, category, description, or all fields.  
- **Total Expense** – Calculate and display the total of all expenses.

---

## Folder Structure

Expense-Tracker/
├─ config/
│ └─ db.py # Database connection setup
├─ modules/
│ ├─ add.py # Add expense module
│ ├─ view.py # View expenses module
│ ├─ update.py # Update expenses module
│ └─ total.py # Total expense module
└─ main.py # Main program entry point


## Prerequisites

- Python 3.x  
- MySQL Server  
- `mysql-connector-python` library

Install the library:

pip install mysql-connector-python

# Setup

Make sure MySQL server is running.

Create a database named expense_tracker:
CREATE DATABASE expense_tracker;

Create the expense table:
CREATE TABLE expense (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amt DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    description VARCHAR(255),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Update config/db.py with your MySQL credentials:
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="expense_tracker"
    )

# How to Run

Navigate to the project folder in terminal/command prompt.

Run the main program:
python main.py
Follow the on-screen menu to add, view, update, or calculate total expenses.

 # Future Enhancements

 
Filter expenses by date or category

Generate monthly reports

Add a GUI interface for better user experience
=======
# expense-tracker-python-mysql
>>>>>>> 9bc16f5749cccbb3da77422dd77d827f36d9bece
