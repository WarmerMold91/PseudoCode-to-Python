# William
# 10/29/2026
# Converting Pseudocode to Python

import random
total_sum = 0

# Number 1: Convert a user-input into all caps, print the result.

# Get input from the user
user_phrase = input("User phrase: ")

# Convert to uppercase and print the result
print(f'Output: "{user_phrase.upper()}"')


# Number 2: Have user input two numbers, add them together and print the result.

# Have user input two numbers

print("Enter two numbers to add together.")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

# Add them together
result = num1 + num2

# Print the result
print(f"Output: {result}")


# Number 3: Get an unknown amount of numbers from the user and add them together, print out the result.

print("Enter Numbers to add together.")
while True:
    # Get the number from the user and add it to the total
    number = float(input("Number: "))
    total_sum += number
    
    # Ask if they want to continue
    another = input("Another number? (y/n): ").strip().lower()
    
    # If they enter 'n' or anything other than 'y', break the loop
    if another != 'y':
        break

print(f"Output: {total_sum}")

# Number 4: Have the user define a maximum whole number, print out a random number between 0 and their number. 
# Allow the user to play again or quit.

print("Enter a maximum number to generate a random number between 0 and that number.")
while True:
    # Get user input for the maximum number
    user_input = input("Max Number: ")
    
    # Clean input and convert to integer
    try:
        max_num = int(user_input)
        if max_num < 0:
            print("Please enter a positive whole number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue
        
    # Generate and print the random number between 0 and max_num
    random_num = random.randint(0, max_num)
    print(f"Output: {random_num}")
    
    # Ask the user if they want to play again
    play_again = input("New Number (y/n)? ").strip().lower()
    
    # Exit the loop if the user types anything other than 'y' or 'yes'
    if play_again not in ['y', 'yes']:
        break

# Number 5: Get a random number. If the number is even print “RIGHT”, if it’s odd, print “LEFT”. 
# Do this ten times. Print out how many times it was “LEFT” and how many times it was “RIGHT”.

# Initialize counters
left_count = 0
right_count = 0

# Loop 10 times
for _ in range(10):
    # Generate a random number between 1 and 100
    num = random.randint(1, 100)
    
    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} – Output: “RIGHT”")
        right_count += 1
    else:
        print(f"{num} – Output: “LEFT”")
        left_count += 1

# Print the final counts
print(f"Output: “Left: {left_count}”")
print(f"Output: “Right: {right_count}”")
