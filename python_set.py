skills = {"Python", "SQL", "HTML", "CSS", "Python"}

print("My Skills:", skills)

# Adding a new item
skills.add("Django")
print("After adding Django:", skills)

# Removing an item
skills.remove("CSS")
print("After removing CSS:", skills)

# Checking an item
print("Is Python available?", "Python" in skills)

# Looping through a set
print("\nMy Skills List:")

for skill in skills:
    print(skill)

# Finding number of items
print("Total skills:", len(skills))
