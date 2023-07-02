import random

def Guessing_game():
    guessing_num = 0
    limit = 3
    
    print(f"Guess a number between {1} and {10}")
    
    while True:
        u_g = int(input("Enter your guess: "))
        if not isinstance(u_g, int):
            raise ValueError("Invalid number")
            
        
        r_n = random.randint(1, 10)
    
        if guessing_num < limit:
            print("You have {} tries left.".format(limit - guessing_num))
            
        if u_g == r_n:
            print("You did it ;)")
            break
        
        if u_g > r_n:
            print("Lower.")
            
        if u_g < r_n:
            print("Higher.")
            
        if guessing_num >= limit:
            print("Out of tries. The number was {}.".format(r_n))
            break
        
        guessing_num += 1
        
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        Guessing_game()

Guessing_game()
