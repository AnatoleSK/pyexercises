"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: The user's answer to a yes/no question.

# 2. Process: Repeat the question until the answer is valid
#    or five attempts have been used.

# 3. Out: The number of attempts and the final decision.

# 4. My stop condition, my attempt limit, my summary:
#    Stop when the answer is "yes" or "no", or after 5 attempts.
#    Accept capitals and surrounding spaces.
#    The summary shows the attempt count and the user's decision,
#    or a message if no valid answer was received.

#Your code below

attempts = 2
answer = ""

while attempts < 5 and answer != "yes" and answer != "no":
    answer = input("Do you want to continue? (yes/no): ")
    answer = answer.strip().lower()
    attempts = attempts + 1

    if answer != "yes" and answer != "no":
        print("Invalid input. Please enter 'yes' or 'no'.")

print("Number of attempts:", attempts)

if answer == "yes":
    print("You chose to continue.")
elif answer == "no":
    print("You chose not to continue.")
else:
    print("Maximum attempts reached. No valid answer received.")