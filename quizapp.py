import json

questions = [
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

def load_score():
    try:
        with open("scores.json", "r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return {"score": 0}    
    
def save_score(score):
    with open("scores.json", "w") as f:
        json.dump({"score": score}, f)

def show_questions():
    score = 0
    for question in questions:
        print(question['question'])
        for choice in question['choices']:
            print(choice)
        while True:
            answer = input("Enter your answer: ")
            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid Answer")

        if answer == question['answer']:
            score += 1
    return score

def show_results(score):
    previous_score = load_score()["score"]
    print(f"Previous Score: {previous_score}/10")
    print(f"Score: {score}/10")
    if previous_score > score:
        print("Nice Try, Keep studying")
    elif previous_score == score:
        print("Keep improving!")
    else:
        print("Great Job!")
    save_score(score)

while True:
    choice = input("Hello, would you like to take a 10-item quiz about Information Technology and Computer Science topics?(Yes/No) ")
    if choice == "Yes":
        score = show_questions()
        show_results(score)
        while True:
            again = input("Take the quiz again?(Yes/No): ")
            if again == "Yes":
                score = show_questions()
                show_results(score)
            elif again == "No":
                print("Have a great day!")
                exit()
            else:
                print("Invalid choice, please type a valid answer")
    elif choice == "No":
        print("Have a great day!")
        exit()
    else:
        print("Invalid choice, please type a valid answer")