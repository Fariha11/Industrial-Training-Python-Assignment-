# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Example 1: Writing to a Text File
with open('data/example.txt', 'w') as file:
    file.write("Hello, Python developers!\n")
    file.write("Welcome to file I/O operations.")

# Example 2: Reading from a Text File
with open('data/example.txt', 'r') as file:
    content = file.read() # readlines(), readlines()
    print(content)

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

import csv

# Example 3: Writing to a CSV File
with open('data/example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 28, "New York"])
    writer.writerow(["Bob", 22, "Los Angeles"])
    writer.writerow(["Carol", 24, "Chicago"])

# Example 4: Reading from a CSV File
with open('data/example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Section 3: JSON Data
# --------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.

import json

# Example 5: Writing JSON to a File
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('data/data.json', 'w') as file:
    json.dump(data, file)


# Example 6: Reading JSON from a File
with open('data/data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Example 7: Processing JSON Data from a File
# Suppose we have a JSON file containing multiple user records.
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"}
]
with open('data/users.json', 'w') as file:
    json.dump(users, file)

with open('data/users.json', 'r') as file:
    users = json.load(file)
    for user in users:
        print(f"{user['name']} ({user['age']}): {user['email']}")

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
# Input and output file paths

import csv
import json
import os
from datetime import datetime


csv_file = 'data/products.csv'  # Assuming the CSV file exists in 'data' folder
json_file = 'data/products.json'  # JSON output file

# Sample data to create the CSV if not existing
products_data = [
    ["ProductID", "ProductName", "Price", "Stock"],
    [101, "Laptop", 800, 50],
    [102, "Smartphone", 600, 120],
    [103, "Tablet", 400, 80]
]

# Create 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Create the CSV file with sample data
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(products_data)

# Function to convert CSV to JSON
def csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r') as csv_f, open(json_file, mode='w') as json_f:
        reader = csv.DictReader(csv_f)  # Read the CSV as a dictionary
        products = [row for row in reader]  # Convert rows to a list of dictionaries
        json.dump(products, json_f, indent=4)  # Write the list of dictionaries to JSON file

# Call the function to convert CSV to JSON
csv_to_json(csv_file, json_file)

print(f"CSV data has been successfully converted to JSON and saved as {json_file}.")


# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.
# Function to write log messages to a file with timestamp
def write_log(message, log_file='data/app_log.txt'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"{timestamp} - {message}\n"
    with open(log_file, 'a') as file:
        file.write(log_message)
    print(f"Log written: {log_message}")

# Sample usage of the log file writer
write_log("CSV to JSON conversion started.")
write_log("CSV to JSON conversion completed.")
# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
