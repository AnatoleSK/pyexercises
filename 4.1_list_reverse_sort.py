"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of quantities from exercise 4.0.

# 2. Process: Display the list in four orders without changing it.

# 3. Out: Four orders, a comparison and the original list at the end.

# 4. My four orders, and which ones modify the original:
#    Original, ascending, descending and reversed.
#    None modifies the original.
#    sorted() and slicing create new lists.
#    sort() and reverse() would modify the list in place.


# Your code below


quantities = [4, 5, 6, 7, 8, 9, 10, 11, 2, 1]
original_copy = quantities.copy()

print("Original order:", quantities)
print("Ascending order:", sorted(quantities))
print("Descending order:", sorted(quantities, reverse=True))
print("Reversed order:", quantities[::-1])

print("Original unchanged:", quantities == original_copy)
print("Original list:", quantities)
