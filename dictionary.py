student = {
    "name": "Maheshwari",
    "course": "Python Full Stack",
    "city": "Tirunelveli"
}
print("Student Name:", student["name"])
print("Course:", student["course"])
print("City:", student["city"])
student["city"] = "Chennai"
student["status"] = "Fresher"
print("\nUpdated Student Details:")
for key, value in student.items():
    print(key, ":", value)
