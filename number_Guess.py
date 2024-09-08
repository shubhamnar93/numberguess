import random
MY_NUMBER= random.randint(1,100)
chose_dificulty=input("type easy or hard for easy or hard difficulty: ")
if chose_dificulty=="hard":
    number_of_attempt=5
else:
    number_of_attempt=10
def checking(guess):
    global MY_NUMBER
    if guess>MY_NUMBER:
        print("too high")
        return
    elif guess<MY_NUMBER:
        print("too low")
        return 
while 0<number_of_attempt:
    print("guess again")
    print(f"you have {number_of_attempt} attempts remaining")
    guess=int(input("Make a guess: "))
    checking(guess)
    number_of_attempt-=1
    if guess==MY_NUMBER:
        print("you win\nyou guessed it right")
        number_of_attempt=0
if guess!=MY_NUMBER:
    print("you lose")
