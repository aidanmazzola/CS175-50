#CS 175
#Aidan Mazzola
#Average Grade Function


def calc_average(scores):
    total = sum(scores)
    average = total / len(scores)
    
    print("Score\tNumeric Grade\tLetter Grade")
    print("-" * 40)
    
    for i, score in enumerate(scores):
        letter_grade = determine_grade(score)
        print(f"score {i + 1}:\t{score}\t{letter_grade}")
    
    print(f"Average score:\t{average}\t{determine_grade(average)}")

def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def repeat():
    while True:
        scores = []
        for i in range(5):
            score = float(input(f"Enter score {i + 1}: "))
            scores.append(score)
        
        calc_average(scores)
        
        choice = input("Enter 'yes' if you would like to do another calculation: ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    repeat()

import random

def calc_average():
    scores = []
    for i in range(5):
        score = my_random(1, 100)
        scores.append(score)
        print(f"score {i + 1}:\t{score}\t{determine_grade(score)}")
    
    average = sum(scores) / 5
    print(f"Average score:\t{average}\t{determine_grade(average)}")

def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def repeat():
    while True:
        calc_average()
        choice = input("Enter 'yes' if you would like to do another calculation: ").lower()
        if choice != 'yes':
            break

def my_random(low, high):
    return random.randint(low, high)

if __name__ == "__main__":
    repeat()


