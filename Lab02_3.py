ID1 = "08250264"
ID2 = "08250289"

last1 = int(ID1[-2:])
last2 = int(ID2[-2:])
unique_value = (last1 + last2) % 10
print("Unique value =", unique_value)

students = {}

while True:
    name = input("Enter student name (or 'exit' to stop): ").strip()

    if name.lower() == "exit":
        break
    
    if name == "":
        print("Warning: Name cannot be empty. Skipping...")
        continue
    students[name] = 0
print("Student List:")
for name in students:
    print("_", name)

for name in students:
    print(f"Quize for {name}:")
    score = 0

ans1 = int(input(f"Q1: {unique_value} + 2 ="))
if ans1 == unique_value + 2:
    score += 1

ans2 = int(input(f"Q2: {unique_value} * 3="))
if ans2 == unique_value *3:
    score += 1

ans3 = int(input(f"Q3: {unique_value} +5="))
if ans3 == unique_value +5:
    score += 1
students[name] = score

print("Results:")
for name, score in students.items():
    print(f"{name}'s Score:", score)

    if score ==0:
        print("Warning: Score is 0")

    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Average"
    else:
        performance = "Poor"

    print("Performance:", performance)

if score >= 2:
    print("Certificate: Eligible")
else:
    print("Certificate: Not Eligible")

print("Stars:")
for i in range(score):
    print("*")

