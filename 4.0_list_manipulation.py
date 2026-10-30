"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: 8 numbers defineds by number_N = x
# 2. Process: print the list , then sort and remove the last
# 3. Out:result of our prompts
# 4. What my list is about, and what I computed from it: random numbers about it 


# Your code below
# 1. In: A list of quantities of shares purchased in ten orders.

# 2. Process: Display the list, select the fourth quantity,
#    sort the list and calculate the total.

# 3. Out: The whole list, the fourth quantity, the sorted list
#    and the total number of shares purchased.

# 4. What my list is about, and what I computed from it:
#    My list represents quantities of shares purchased.
#    The total measures the overall number of shares bought.

# Manual check on the first three quantities:
# 4 + 5 + 6 = 15.

quantities = [4, 5, 6, 7, 8, 9, 10, 11, 2, 1]

print("Whole list:", quantities)
print("Fourth quantity:", quantities[3])

print("Check on three quantities:", sum(quantities[:3]))
print("Total shares purchased:", sum(quantities))

quantities.sort()
print("Sorted list:", quantities)