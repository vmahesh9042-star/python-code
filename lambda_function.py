def add_numbers(a, b):
    return a + b

print("Normal Function:", add_numbers(10, 20))


# Lambda function
add = lambda a, b: a + b

print("Lambda Addition:", add(10, 20))


# Lambda with multiplication
multiply = lambda a, b: a * b

print("Multiplication:", multiply(5, 4))


# Lambda with condition
check_number = lambda n: "Even" if n % 2 == 0 else "Odd"

print("Number 10 is:", check_number(10))
print("Number 7 is:", check_number(7))
