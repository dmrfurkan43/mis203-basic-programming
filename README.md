# MIS203 - Basic Programming

- **Name:** Furkan Demir
- **Student Number:** 2304109043
- **Department:** Management information systems
- **Course Name:** MIS203 - Basic Programming

## Week 01: Student Profile

The program asks for a name, department, age, and career goal, then prints a short student profile.

### Run the program

With Python 3 installed, open a terminal in this repository's main folder and run:

```sh
python week01/student_profile.py
```

Type an answer to each question and press Enter.

### How the code works

- `input()` asks a question and reads the answer as text.
- The variables `name`, `department`, `age`, and `career_goal` store the answers. Age stays as text because the program does not do calculations with it.
- `print()` displays the heading and each answer on its own line. The empty `print()` adds a blank line before the profile.
- To change a question or an output label, edit the text inside its quotation marks.

### AI assistance

**AI Tool Used:** OpenAI Codex

**Prompt Used:**

> Use an AI tool to help you create a simple Python program. Your program should ask the user for:
> Name
> Department
> Age
> Career Goal
> Then print a short student profile.

**What did you change?** No manual changes have been made to the AI-generated code.




## Week 02: Grade Calculator

The program asks for student names and scores, calculates letter grades, and shows the total number of students and the average score.

### Run the program

With Python 3 installed, open a terminal in this repository's main folder and run:

```sh
python week02/grade_calculator.py
```

### AI assistance

**AI Tool Used:** ChatGPT

**Prompt Used:**

> Create a Python grade calculator using while True, break, and continue. Ask for student names and scores, validate scores from 0 to 100, calculate letter grades, and show the total number of students and average score.

**What did you change?** I changed the code to match the assignment requirements. I also tested the program with valid and invalid scores.

**What does break do in your program?** Break stops the loop when the user enters q.




## Week 03 - Cinema Ticket Office

""AI Tool Used""
OpenAI ChatGPT

""Prompt Used""

> Create a simple Python cinema ticket program using input, type conversion, f-strings, loops, if/elif/else, and input validation. The program should calculate ticket prices based on age, day, and student status.

""What did you change?""

> I changed the program to calculate ticket prices for different customers. I also added input validation and a summary of the tickets sold.

## Tests
Age 30, weekend, student no → 250.00 TRY (Standard)
Age 20, weekday, student yes → 140.00 TRY (Student)
Age 65, weekday, student no → 100.00 TRY (Senior)
Why does the order of the rules matter?

The order matters because only one discount should be applied. For example, a 10-year-old student should get the Child discount, not the Student discount, because the Child rule comes first.




## Week 04 - Restaurant Order System

## Surprise Me Assignment - Restaurant Order System

### Project Description
This project is a simple restaurant order system written in Python. Users can choose food and drinks from a menu, enter quantities, and calculate the total price. The program gives a 10% discount when the subtotal is 1000 TRY or more.

### Features
- Displays a restaurant menu.
- Allows users to select items and enter quantities.
- Calculates item prices and the total amount.
- Gives a 10% discount on orders of 1000 TRY or more.
- Generates a random order number.
- Displays the order date and time.
- Shows the order summary and final price.

### Libraries Used
- `random`: Generates a random order number.
- `datetime`: Displays the order date and time.

### AI Tool Used
OpenAI ChatGPT