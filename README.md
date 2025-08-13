# Quiz Application (Python + Tkinter)

A GUI-based quiz application built with Python's Tkinter library.  
The app allows students to register, take a timed quiz with randomized questions, navigate between questions, save answers, and automatically submit when time expires.

## Features
- **Student Registration Form** – Captures Name and Year with input validation.
- **Randomized Questions** – Questions are loaded from a text file in a random order.
- **Navigation** – Move between **Previous**, **Next**, and **Save & Next**.
- **Timer Functionality** – Countdown clock with auto-submit when time runs out.
- **Answer Saving** – Stores selected answers and marks completed questions.
- **Finish Early Option** – Students can submit before time ends.
- **Persistent Storage** – Saves responses to a `answer.txt` file.

## Requirment for the input Questions file
1. The input Question file should be with '.txt' extension  and should be in the following format 
2. Gapping between question of one line.
3. Onle must must be given in the end of all question like below line no. 124 is left blank even the question are ending with line no. 123.
4. A Question followed by four options must be given.
