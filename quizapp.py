import json        #Imports the JSON module to enable saving and loading the score between sessions.

questions = [      #List of Dictionaries. Each Dictionary holds the question, choices, and answer.
    {
        "question": "This is the brain of the computer and is responsible for carrying out instructions and running calculations.",
        "choices": ["A. Random Access Memory", "B. System Board", "C. Central Processing Unit", "D. Graphics Processing Unit"],
        "answer": "C"
    },
    {
        "question": "This organises data by storing similar elements and allocating contiguous memory.",
        "choices": ["A. Queues", "B. Arrays", "C. Stacks", "D. Binary Tree"],
        "answer": "B"
    },
    {
        "question": "An operating system that manages the execution of multiple processes, including tasks such as scheduling, synchronization, and communication.",
        "choices": ["A. File System Management", "B. Device Management", "C. Security Access Controls", "D. Process Management"],
        "answer": "D"
    },
    {
        "question": "Facilitates data communication between the system and external devices. it handles data transfer, manage device access, and ensures error-free communication.",
        "choices": ["A. Input/Output Manager", "B. Memory Manager", "C. Kernel", "D. File System Manager"],
        "answer": "A"
    },
    {
        "question": "A type of database that store it in defined tables with rows and columns. Excels with structured data as financial records.",
        "choices": ["A. Cloud Database", "B. Relational Database", "C. Non-relational Database", "D. Navigational Database"],
        "answer": "B"
    },
    {
        "question": "A type of database that stores it as a variety of data structures, including key-value pairs or graphs. Best for unstructured data types such as text files, audio, and video.",
        "choices": ["A. Cloud Database", "B. Relational Database", "C. Non-relational Database", "D. Navigational Database"],
        "answer": "C"
    },
    {
        "question": "A unique number assigned to every network device. Identifies the device's host network and its location on the network.",
        "choices": ["A. Routers", "B. IP Address", "C. Switches", "D. Gateways"],
        "answer": "B"
    },
    {
        "question": "They provide isolated network environments within a public cloud infrastructure.",
        "choices": ["A. Virtual Private Clouds", "B. Content Delivery Networks", "C. Service Mesh", "D. Load Balancers"],
        "answer": "A"
    },
    {
        "question": "This Category of cybersecurity focuses on keeping applications and devices free of threats",
        "choices": ["A. Network Security", "B. Operational Security", "C. Information Security", "D. Application Security"],
        "answer": "D"
    },
    {
        "question": "This is a type of software designed to gain unauthorized access or to cause damage to a computer.",
        "choices": ["A. Phishing", "B. Malware", "C. SQL Injection", "D. Social Engineering"],
        "answer": "B"
    }
]

def load_score():                                           #Loads the previous score from the JSON file.
    try:                                                    #Attempts to open and read the file. If an error occurs, it moves to except.
        with open("scores.json", "r") as f:                 #Opens scores.json in read mode.
            return json.load(f)                             #Reads the JSON file and returns its contents as a Python dictionary.
        
    except (FileNotFoundError, json.JSONDecodeError):       #Catches missing file or empty file errors.
        return {"score": 0}                                 #Returns a default score of 0 to keep the return type consistent as a dictionary

def save_score(score):                                      #Defines a function that saves the current score as a parameter to know what number to save.
    with open("scores.json", "w") as f:                     #Opens scores.json in write mode. If none exist, creates one.
        json.dump({"score": score}, f)                      #Writes the score to the file as a dictionary in JSON format.

def show_questions():                                       #Defines a function that runs the quiz and returns the final score.
    score = 0                                               #Initializes the score to 0 before any questions are answered.
    for question in questions:                              #Loops through each question dictionary in the questions list.
        print(question['question'])                 
        for choice in question['choices']:                  #Loops through each choice in the current question.
            print(choice)
        while True:                                         #Keeps asking for an answer until the user enters a valid one.
            answer = input("Enter your answer: ")           #Gets the user's answer as input.
            if answer in ["A", "B", "C", "D"]:              #Checks if the input is a valid choice.
                break                                       #Exits the validation loop if the answer is valid.
            print("Invalid Answer")             

        if answer == question['answer']:                    #Checks if the user's answer matches the correct answer.
            score += 1                                      #Add plus 1 to the score for every correct answer.
    return score                                            #Returns the final score after all questions are answered.

def show_results(score):                                    #Defines a function that displays the quiz results, accepting the current score as a parameter.
    previous_score = load_score()["score"]                  #Loads the previous score from the JSON file and extracts the number.
    print(f"Previous Score: {previous_score}/10")       
    print(f"Score: {score}/10")
    if previous_score > score:                              #If the previous score is higher than the current score.
        print("Nice Try, Keep studying")
    elif previous_score == score:                           #If both scores are equal.
        print("Keep improving!")
    else:                                                   #If the current score is higher than the previous score.
        print("Great Job!")
    save_score(score)                                       #Saves the current score to the JSON file for future comparison.

while True:                                                 #Keeps the program running until the user chooses to exit.
    choice = input("Hello, would you like to take a 10-item quiz about Information Technology and Computer Science topics?(Yes/No) ")        #Asks the user if they want to take the quiz.
    if choice == "Yes":                                     #If the user puts Yes.
        score = show_questions()                            #Runs the quiz and stores the returned final score.
        show_results(score)                                 #Displays the results by passing the final score.
        while True:                                         #Keeps asking if the user wants to retry until they choose to exit.
            again = input("Take the quiz again?(Yes/No): ")         #Asks the user if they want to take the quiz again.
            if again == "Yes":                              #If the user wants to retry.
                score = show_questions()                    #Runs the quiz again and stores the new score.
                show_results(score)                         #Displays the new results.
            elif again == "No":                             #If the user chooses to exit.
                print("Have a great day!")
                exit()                                      #Exit the program.
            else:                                           #If the input is neither Yes nor No.
                print("Invalid choice, please type a valid answer")   
    elif choice == "No":                                    #If the user doesn't want to retry.
        print("Have a great day!")      
        exit()                                              #Exit the program.
    else:                                                   #If the input is neither Yes nor No
        print("Invalid choice, please type a valid answer") 