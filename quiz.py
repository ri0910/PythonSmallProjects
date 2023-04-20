quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },"question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },"question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },"question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

for key,value in quiz.items():
    print("Question : " , value["question"])
    ans = input("Answer : ").lower()
    if ans == value["answer"].lower():
        print("Answer is correct!")
        score += 1
        print("Current score is ", score)
        print("")
        print("")
    else:
        print("Answer is not correct!")
        print("Current score is ", score)
        print("")
        print("")

print("Total score is ", str(score))
print(f"Percentage is {str(int(score/7*100))}%")