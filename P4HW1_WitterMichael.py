# Michael Witter
# October 27, 2026
# P4HW1 - Score List
# Collect valid scores, drop the lowest, and display the average and grade.

# Pseudocode:
# Display the student's name.
# Ask how many scores will be entered; require at least two.
# Repeat for each score:
#     Ask for a score.
#     While the score is outside 0 through 100, ask again.
#     Add the valid score to the score list.
# Find and save the lowest score, then remove it once from the list.
# Calculate the average of the remaining scores.
# Assign A, B, C, D, or F using the average.
# Display the lowest score, modified list, average, and letter grade.

print("P4HW1 - Michael Witter")
print()

number_of_scores = int(input("How many scores do you want to enter? "))
while number_of_scores < 2:
    print("Enter at least two scores so one can be dropped.")
    number_of_scores = int(input("How many scores do you want to enter? "))

scores = []
for score_number in range(1, number_of_scores + 1):
    score = float(input(f"Enter score #{score_number}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))
    scores.append(score)

lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print()
print("------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("-------------------------------")

