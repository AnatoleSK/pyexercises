"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: An integer N entered by the user.
# 2. Process: Check each number from 1 to N using division by 2.
# 3. Out: Display whether each number is odd or even.
# 4. Decisions:
# - If N is 0: display an error message.
# - If N is negative: display an error message.
# - If N exceeds 100, including 5000: reject it.

# Tests:
# - 6: three odd numbers and three even numbers.
# - 0 and -4: a positive number is requested.
# - 5000: the maximum limit message is displayed.

N = int(input("Enter a number between 1 and 100: "))

if N <= 0:
    print("Please enter a positive number.")

elif N > 100:
    print("The number is too large. Maximum: 100.")

else:
    for number in range(1, N + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")