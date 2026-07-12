from quiz_database import question_bank 
from quiz_database import options


print("***************")
print("Welcome to Qize Game!")

score = 0
def check_answer(user_guess, correct_answer):
    if user_guess.upper() == correct_answer:     
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("**************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
        
    guess=input("Enter your answer(A/B/C/D): ").upper()
    is_correct=check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print(f"The correct answer is: {question_bank[question_num]['answer']}")
    print(f"Your current score is: {score}/{question_num + 1}")

print(f"You have given {score} correct answers")
print(f"Your score is {score/len(question_bank)*100}%")  
   