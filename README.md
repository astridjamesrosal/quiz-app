# Python Quiz App

A 10-Item command line quiz app about Information Technology and Computer Science built in Python

## Features
- Contains a list of dictionaries with 10 Questions
- Every Question has four choice (A, B, C, D)
- Every Question has an answer of Letters only
- Scores are stored in the JSON file
- Scores are compared. The Previous and The Current Scores

## How to Run
- Make sure Python is installed
- Clone this repository
- Run: python quizapp.py 

## What I learned
- Structuring questions as a list of dictionaries to group related data together
- Using the JSON module to save and load data between sessions
- Writing functions that return values and pass them to other functions
- Implementing score tracking and comparison logic across multiple sessions
- Handling multiple exceptions with (FileNotFoundError, json.JSONDecodeError)
