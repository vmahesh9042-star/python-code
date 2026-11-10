marks = int(input("Enter your marks: "))
# Check grade
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Your marks:", marks)
print("Your grade:", grade)
