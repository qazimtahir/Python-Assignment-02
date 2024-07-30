# Initialize an empty list
values = []

print("Enter values to add to the list. Press enter without typing anything to finish.")

# Continuously prompt the user for input
while True:
    # Get input from the user
    user_input = input()

    # Check if the input is empty (user pressed enter without typing anything)
    if user_input == "":
        break

    # Add the input value to the list
    values.append(user_input)

# Print the list of values
print("The list of values is:", values)
