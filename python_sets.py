skills = {"Python", "SQL", "HTML", "CSS", "Python"}
print("My Skills:", skills)
skills.add("Django")
print("After adding Django:", skills)
skills.remove("CSS")
print("After removing CSS:", skills)
print("Is Python available?", "Python" in skills)
print("\nMy Skills List:")
for skill in skills:
    print(skill)
print("Total skills:", len(skills))
