import random
choice=['rock','paper','scissors']
print('welcome to Rock-Paper-Scissors Game!')
while True:
    user_choice= input("Enter rock,paper,or scissors:").lower()
    if user_choice not in choice:
        print("Invalid choice .Please try again.")
        continue
    computer_choice=random.choice(choice)
    print("Computer choice:",computer_choice)
    if user_choice == computer_choice:
        print("It is a tie!")
    elif(user_choice== 'rock' and computer_choice == 'scissors')  or  (user_choice== 'scissors' and computer_choice== 'paper' ) or (user_choice=='paper' and computer_choice== 'rock'):
        print("you win!🎉")
    else:
        print('you lose!😥') 
    play_again=input("play again? (yes/no):").lower()
    if play_again != "yes":
        print("Thanks for playing! ")
        break


