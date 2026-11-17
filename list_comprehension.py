numbers = []

for i in range(1, 6):
    numbers.append(i)

print("Normal List:", numbers)


# List comprehension
squares = [i * i for i in range(1, 6)]

print("Squares:", squares)


# Even numbers
even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print("Even Numbers:", even_numbers)


# Convert names into uppercase
names = ["maheshwari", "arun", "priya"]

upper_names = [name.upper() for name in names]

print("Uppercase Names:", upper_names)
