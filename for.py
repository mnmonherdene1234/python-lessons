# Example 1: Basic for loop
print("Example 1:")
for i in range(5):
    print(i)
# Output: 0 1 2 3 4
# Explanation: This loop iterates over the values 0 through 4 and prints each value.

# Example 2: Looping through a list
print("\nExample 2:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
# Output: I like apple
#         I like banana
#         I like cherry
# Explanation: The loop iterates through each item in the list "fruits" and prints a message for each item.

# Example 3: Looping with index and item using enumerate()
print("\nExample 3:")
for index, fruit in enumerate(fruits):
    print("Fruit", index + 1, ":", fruit)
# Output: Fruit 1 : apple
#         Fruit 2 : banana
#         Fruit 3 : cherry
# Explanation: The enumerate() function adds an index to each item in the list, starting from 0.

# Example 4: Nested loops
print("\nExample 4:")
for i in range(3):
    for j in range(2):
        print(i, j)
# Output: 0 0
#         0 1
#         1 0
#         1 1
#         2 0
#         2 1
# Explanation: This demonstrates a nested loop, where the inner loop runs completely for each iteration of the outer loop.

# Example 5: Looping with a step using range()
print("\nExample 5:")
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8
# Explanation: The range() function can take a third argument, specifying the step between values.

# Example 6: Looping over characters in a string
print("\nExample 6:")
word = "Python"
for char in word:
    print(
        char)  # Output: P y t h o n  # Explanation: The loop iterates over each character in the string "word" and prints each character.
