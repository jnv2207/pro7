# pro7

<img width="2400" height="720" alt="image" src="https://github.com/user-attachments/assets/3dc25597-94b1-4710-af60-4872dcf4cab6" />



A tiny Swiss Army knife for Python, built to show how modules and packages really work.

Features · Structure · Quick Start · Demo · User Guide · Assumptions · Author

</div>

## About the Project

Multi-Utility Toolkit (project: Moduler & Packager) is a Python console application that brings together standard library modules, custom modules, and a custom package behind one friendly, menu-driven interface.

Imagine a small business owner who needs to track working hours, hand out secure passwords, stamp invoices with unique IDs, and save logs to files. This toolkit does all of that from a single menu.

## Goal: demonstrate Python's modular structure: imports, packages, __init__.py, the __name__ == "__main__" paradigm, and dynamic exploration with dir().


## 😊 Features
⭐ Datetime and Time
   Show the current date and time in a friendly format
   Difference between two dates or times
   Custom formats with strftime
   Stopwatch and countdown timer
⭐Math
   Factorials, logarithms, trigonometry
   Compound interest calculator
   Area of geometric shapes
⭐Random
   Random numbers and lists
   Strong random passwords
   Random sampling from a dataset
   OTP generator and game simulations
⭐UUID
   Unique IDs for files, records and user sessions
   UUID4 demonstration (great for invoice numbers)
   File Operations (custom module)
   Create, write, read and append files
   Save logs and outputs to text files
⭐Dynamic Exploration
  Type any built-in or custom module name
  Instantly list its attributes using dir()
## Project Structure
text
multi-utility-toolkit/
├── main.py                  # Menu-driven entry point
├── toolkit/                 # Custom package
│   ├── __init__.py          # Initializes the package
│   ├── datetime_utils.py    # Date, time, stopwatch, countdown
│   ├── math_utils.py        # Math, interest, geometry, conversions
│   ├── random_utils.py      # Numbers, lists, passwords, OTPs
│   ├── uuid_utils.py        # Unique identifier helpers
│   ├── file_ops.py          # Custom file operations module
│   └── explorer.py          # dir()-based module explorer
├── assets/                  # Images used in this README

## Quick Start

# 1. Clone the repository
git clone https://github.com/<your-username>/multi-utility-toolkit.git

# 2. Enter the folder
cd multi-utility-toolkit

# 3. Run the toolkit (no external libraries needed)
python main.py

Only the Python standard library is used, so there is nothing to pip install.


## Demo

<img width="1520" height="940" alt="image" src="https://github.com/user-attachments/assets/2fa69512-59e6-4296-ace0-07d6bfa68704" />


## Datetime

Current Date and Time: 2025-01-04 10:15:30
Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days

Current Date and Time: 2025-01-04 10:15:30
Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days

## Math

Enter a number: 5
Factorial: 120
Enter principal amount: 1000
Enter rate of interest (in %): 5
Enter time (in years): 2
Compound Interest: 1102.50

## Random Password

Enter password length: 8
Generated Password: Kd8@qzP!

## UUID

Generated UUID: f47ac10b-58cc-4372-a567-0e02b2c3d479

## File Operations

Enter file name: example.txt
File created successfully!
Enter data to write: This is a sample file.
Data written successfully!
File Content:
This is a sample file.

## dir() Explorer

Enter module name to explore: math
Available Attributes in math module:
['acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', ..., 'copysign', 'cos', ...]

## User Guide
⬛Run python main.py to open the main menu.
⬛Type a number (1 to 7) and press Enter.
⬛Follow the prompts inside each sub-menu.
⬛Choose Back to Main Menu to return, or 7 to exit.

## Tips

⭐Dates use the format YYYY-MM-DD.
⭐The explorer accepts any importable module: try math, random, uuid, datetime, or toolkit.file_ops.
⭐File operations work in the current folder unless you give a path.


## Concepts Demonstrated
Built-in modules: datetime, time, math, random, uuid
Custom modules: every file inside toolkit/
Packages and __init__.py: toolkit/__init__.py
__name__ == "__main__": each module can be tested alone, and main.py runs the app
dir(): the module explorer (menu option 6)

## Error handling: safe input for numbers, dates and file names

Each module follows this pattern so it is reusable and runnable on its own:

## python
def greet():
    return "Hello from a reusable module!"

if __name__ == "__main__":
    # Runs only when this file is executed directly
    print(greet())
## ⭐Assumptions
Python 3.8 or newer is installed.
Compound Interest is reported as the final amount (A = P(1 + r/100)^t), matching the sample output (1000 at 5% for 2 years gives 1102.50).
Date differences use YYYY-MM-DD input and are shown in days.
The stopwatch and countdown run in the console and are stopped with the Enter key or Ctrl+C.
Generated passwords mix letters, digits and symbols.
Files are created and read relative to the folder where the program is run.
Project Deliverables Checklist
[x] Python source code with a menu-driven interface
[x] Custom modules and a package with __init__.py
[x] Example outputs (logs, reports, generated IDs)
[x] README and user guide
[x] Code comments throughout

##  ✨Author

Tejani Janvi CSE 3C, Computer Science Engineering 

<div align="center">

Built with Python and a lot of curiosity.

If you found this helpful, give the repo a star✨.

</div>


├── outputs/                 # Sample logs and generated files
└── README.md


