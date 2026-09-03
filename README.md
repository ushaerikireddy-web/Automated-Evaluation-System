# Student Information and Marks Evaluation System

A simple Python console-based application that collects student information and marks, calculates total and average marks, and evaluates the student's result and grade.

## Project Description

The **Student Information and Marks Evaluation System** is a beginner-friendly Python project developed to practice fundamental Python programming concepts.

The application allows the user to:

* Enter student personal information
* Enter marks for five subjects
* Calculate total marks
* Calculate average marks
* Determine Pass or Fail
* Assign a grade based on average marks
* Enter information for multiple students

## Features

### Student Personal Information

The program collects:

* Name
* Age
* Mobile Number
* Email ID
* Department
* Roll Number
* City

The information is collected using Python's `input()` function.

### Subject Marks

The application accepts marks for five subjects:

* Python
* Java
* Database
* Data Science
* Web Development

The marks are stored as floating-point values.

### Marks Calculation

The program calculates:

**Total Marks**

```text
Total Marks = Python + Java + Database + Data Science + Web Development
```

**Average Marks**

```text
Average Marks = Total Marks / 5
```

These calculations are implemented in the program.

## Grading System

The program evaluates whether the student has achieved at least 35 marks in every subject.

| Average Marks   | Grade        |
| --------------- | ------------ |
| 75 and above    | Distinction  |
| 60 <= Avg < 74  | First Class  |
| 50 <= Avg < 59  | Second Class |
| 35 <= Avg < 50  | Pass         |

If the student does not achieve the required marks in all subjects, the result is **Fail** and the grade is **Fail**.

## Technologies Used

* Python
* Python Functions
* Conditional Statements
* While Loop
* User Input
* Arithmetic Operators
* F-Strings

## Program Flow

```text
Start
  |
  v
Enter Student Information
  |
  v
Enter Marks for 5 Subjects
  |
  v
Calculate Total Marks
  |
  v
Calculate Average Marks
  |
  v
Check Subject Marks
  |
  +------ Student Passed ------+
  |                            |
  v                            v
Calculate Grade              Fail
  |                            |
  +-------------+--------------+
                |
                v
       Display Student Details
                |
                v
        Enter Another Student?
           /            \
         Yes             No
          |               |
          v               v
       Repeat            End
```

## Menu Options

The program provides a menu that allows the user to either enter student information again or stop the program.

```text
Choose below options

1 --> Enter Student Information
2 --> There is no more students to enter details

Enter An option :
```

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/ushaerikireddy-web/Automated-Evaluation-System.git
```

### Step 2: Open the Project Folder

```bash
cd Automated-Evaluation-System
```

### Step 3: Run the Python File

```bash
python student_information.py
```

> (  Replace `student_information.py` with the actual name of your Python file. )

## Example

```text
*** Student Personal Information ***

Enter the student's Name : Usha
Enter the student's Age : 22
Enter the student's Mobile_Number : 9876543210
Enter the student's Email_Id : example@gmail.com
Enter student's Department : CSE
Enter student's Roll_Number : 101
Enter student's City : Hyderabad

*** Student Marks ***

Enter Python Marks : 85
Enter Java Marks: 78
Enter Data Base Marks : 82
Enter Data Science : 90
Enter Web Development : 88
```

The program then displays the student's personal information, subject marks, total marks, average marks, result, and grade.

## Python Concepts Practiced

This project helped practice:

* Functions
* `input()`
* Type conversion using `int()` and `float()`
* `if`, `elif`, and `else`
* `while` loop
* Arithmetic operations
* Comparison operators
* Logical operators
* F-string formatting
* `__name__ == "__main__"`

## Output : 
# case - 1 :

<img width="920" height="686" alt="image" src="https://github.com/user-attachments/assets/55369389-5bf1-4989-b604-2ebba782117e" />

# case - 2 :

<img width="911" height="701" alt="image" src="https://github.com/user-attachments/assets/f081e79f-3c9c-482d-8dce-1847708a9154" />



## Future Enhancements

The project can be improved by adding:

* Student data storage using files
* MySQL database integration
* Search student by Roll Number
* Update student information
* Delete student records
* Input validation
* Automatic report card generation
* GUI using Tkinter
* Web-based interface using Django or Flask

## Author

**Usha Erikireddy**

GitHub: **ushaerikireddy-web**

## Conclusion

This project demonstrates how basic Python programming concepts can be combined to create a simple student evaluation application. It is suitable as a beginner Python project and can be extended into a complete student management system.
