import numpy as np

correct_number=np.random.randint(0,101)
print(correct_number)
condition_met=0
while condition_met==0:
    user_guess=int(input("Guess a number..."))
    if user_guess==correct_number:
        print("You got it!")
        condition_met=condition_met+1
    if user_guess<=correct_number:
        print("You guessed too low!")
    if user_guess>=correct_number:
        print("Your guess was too high!")
