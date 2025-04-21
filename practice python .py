import time
import random
import sys

def run_game():
    print("Welcome to the Simple Run Game!")
    print("When you see 'RUN!' on the screen, press any key as fast as you can!")
    
    input("Press Enter to start the game...")  # Wait for user to press Enter to start the game.
    
    print("\nGet ready...")
    time.sleep(random.randint(1, 3))  # Random delay between 1 and 3 seconds
    
    print("\nRUN!")
    
    start_time = time.time()  # Record the time when "RUN!" is displayed.
    input("Press any key to run! (Press Enter or any other key)")
    end_time = time.time()  # Time when the user presses a key
    
    reaction_time = end_time - start_time  # Calculate how quickly the user pressed the key
    
    print(f"\nYour reaction time is: {reaction_time:.4f} seconds")
    
    if reaction_time < 0.5:
        print("Wow! That was super fast!")
    elif reaction_time < 1:
        print("Nice! You're quick!")
    else:
        print("Not bad, but you can do faster!")

# Start the game
run_game()
