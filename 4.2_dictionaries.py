"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A customer's name, age, city, country and email.

# 2. Process: Store the details in a dictionary, read the name,
#    update the city, remove the age and display all fields.

# 3. Out: The name, updated city, removed age and remaining fields.

# 4. My object, my five fields, and why those:
#    A customer described by:
#    name: identify the customer.
#    age: analyse customer age groups.
#    city: identify the customer's local market.
#    country: identify the customer's national market.
#    email: contact the customer.

# Missing field test:
# customer["phone"] raises a KeyError because "phone" does not exist.
# Using get() displays a default message instead of stopping.

#Your code below:

name = input("Enter the customer's name: ")
age = input("Enter the customer's age: ")
city = input("Enter the customer's city: ")
country = input("Enter the customer's country: ")
email = input("Enter the customer's email: ")

customer = {
    "name": name,
    "age": age,
    "city": city,
    "country": country,
    "email": email
}

# Read one field
print("Customer's name:", customer["name"])

# Change one field
customer["city"] = input("Enter the customer's new city: ")
print("Updated city:", customer["city"])

# Remove one field
customer_age = customer.pop("age")
print("Customer's age was:", customer_age)

# Safely read a field that does not exist
print("Phone:", customer.get("phone", "Not provided"))

# Display every remaining field and its value
for field, value in customer.items():
    print(field, ":", value)