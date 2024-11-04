import random  # Importing the random module to generate random numbers

# Constant to define the number of rounds in the game
NUM_ROUNDS = 5

def high_low_game():
    # Welcome message
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # Initialize the player's score to 0

    # Main game loop for each round
    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")  # Display the current round number
        
        # Generate random numbers for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Display the player's number
        print(f"Your number is {player_number}")

        # Get user's guess input and ensure it's valid
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").lower()
        while guess not in ["higher", "lower"]:  # Loop until valid input
            guess = input("Please enter either 'higher' or 'lower': ").lower()

        # Determine if the player guessed correctly
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increase score for a correct guess
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Display the player's current score after each round
        print(f"Your score is now {score}\n")

    # Final messages based on player's score
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game function
high_low_game()
