def greet(name="Student"):
    print("Hello,", name)

greet()
greet("Maheshwari")

# Keyword arguments
def student_details(name, course, city):
    print("Name:", name)
    print("Course:", course)
    print("City:", city)

print("\nStudent Details:")
student_details(
    city="Tirunelveli",
    name="Maheshwari",
    course="Python Full Stack"
)

# Function with return value
def calculate_total(price, quantity=1):
    return price * quantity

total = calculate_total(500, 3)
print("\nTotal Amount:", total)
