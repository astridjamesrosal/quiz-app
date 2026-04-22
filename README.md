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
- I learned structuring the questions as a list of dictionaries to group related data together. Questions, their choices, and their respective answers.
- I also used the JSON module to save and load data which are the scores between sessions
- I learned writing functions that return values and pass them to other functions
- I learned to track the scores, save them in the JSON module, and then compare the previous and the current scores.
- I also learned to handle situations where the file doesn't exist through (FileNotFoundError, json.JSONDecodeError)
- I added comments beside each line of code to not forget their respective functions.
