"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of quantities from exercise 4.0.

# 2. Process: Loop through the list, number each order
#    and calculate its percentage of the total quantity.

# 3. Out: One line per order showing its position,
#    quantity and percentage of the total.

# 4. What I compute for each item, and why it is worth showing:
#    I calculate each order's share of the total quantity.
#    This shows which orders represent the largest purchases.

# Check: 10 items produce exactly 10 lines.

#Your code below:
quantities = [4, 5, 6, 7, 8, 9, 10, 11, 2, 1]

total = sum(quantities)

for position, quantity in enumerate(quantities, start=1):
    share = round(quantity / total * 100, 2)
    print("Order:", position, "Quantity:", quantity,
          "Share of total (%):", share)
