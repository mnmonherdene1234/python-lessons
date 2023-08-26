def main():
    # Prompt the user to input their score and convert it to an integer
    score = int(input("Enter your score: "))

    # Using if, elif, and else statements to determine the grade based on the score
    if score >= 90:
        grade = "A"  # If the score is 90 or higher, assign the grade "A"
    elif score >= 80:
        grade = "B"  # If the score is between 80 and 89, assign the grade "B"
    elif score >= 70:
        grade = "C"  # If the score is between 70 and 79, assign the grade "C"
    elif score >= 60:
        grade = "D"  # If the score is between 60 and 69, assign the grade "D"
    else:
        grade = "F"  # If the score is below 60, assign the grade "F"

    # Display the calculated grade to the user
    print("Your grade is:", grade)


# This block ensures that the main() function is executed only if this script is run directly, not imported as a module
if __name__ == "__main__":
    main()
