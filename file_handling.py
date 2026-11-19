with open("student.txt", "w") as file:
    file.write("Name: Maheshwari\n")
    file.write("Course: Python Full Stack\n")
    file.write("Status: Fresher\n")

print("File created successfully!")

# Read the file
with open("student.txt", "r") as file:
    content = file.read()

print("\nStudent Details:")
print(content)

# Append new information
with open("student.txt", "a") as file:
    file.write("Location: Chennai\n")

print("New information added!")

# Read updated file
with open("student.txt", "r") as file:
    print("\nUpdated Student Details:")
    print(file.read())
