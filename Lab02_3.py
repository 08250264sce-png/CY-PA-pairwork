ID1 = "08250264"
ID2 = "08250289"

last1 = int(ID1[-2:])
last2 = int(ID2[-2:])
unique_value = (last1 + last2) % 10
print("Unique value =", unique_value)