"""
A while loop in Python is a control structure that repeatedly executes a block of code as long as a specified condition
remains true. The loop iterates continuously, evaluating the condition before each iteration. If the condition
is initially false, the loop may not execute at all.
"""

# Example 1: Basic while loop
print("Example 1:")
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4
# Explanation: This loop iterates as long as the condition (count < 5) is true.

# Example 2: Loop with user input and break
print("\nExample 2:")
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    print("You entered:", user_input)
# Explanation: This loop keeps asking the user for input until they type 'quit', at which point the loop breaks.

# Example 3: Loop with continue
print("\nExample 3:")
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)
# Output: 1 2 4 5
# Explanation: The loop continues to the next iteration when the condition (number == 3) is met.

# Example 4: Looping with condition at the end
print("\nExample 4:")
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Sum:", total)
# Explanation: This loop continuously prompts the user for numbers until they enter 0, then it calculates and displays the sum.

# Example 5: Loop with else block
print("\nExample 5:")
search_list = [1, 2, 3, 4, 5]
search_value = 6
index = 0
while index < len(search_list):
    if search_list[index] == search_value:
        print("Found at index", index)
        break
    index += 1
else:
    print(
        "Value not found in the list.")  # Explanation: The 'else' block is executed when the loop completes without hitting a 'break' statement.
