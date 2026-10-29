"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence entered by an user
# 2. Process: transformation of it depend of the what it's wrote after "print"
# 3. Out:a certain way depending on what we decided
# 4. My four transformations, and when each is useful:
# - upper(): Write a heading in capital letters.
# - lower(): Standardise text for comparisons.
# - strip(): Remove unwanted surrounding spaces.
# - replace(): Replace spaces with underscores.


# Your code below
text = input("Enter a sentence: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Spaces replaced:", text.replace(" ", "_"))