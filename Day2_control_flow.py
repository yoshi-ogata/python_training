
x = 2
y = 4

if x > y:
    print(f"{x} is greater")
else:
    print(f"{y} is greater")

# Task
# Get two person name
# Case 1:
# Yuma, Yoshi
# 173cm, 163cm
# Expected
# Yuma is taller than Yoshi by 10cm

# Case 2:
# Yuma, Yoshi
# 173cm, 185cm
# Expected
# Yoshi is taller than Yuma by 12cm

#solution1
person1 = input("Please enter name of person1?:")
person2 = input("Please enter name of person2?:")
height1 = float(input(f"Please tell the height of {person1}?:"))
height2 = float(input(f"Please tell me the height of {person2}?:"))

if height1 > height2:
    print(f"{person1} is taller than {person2} by {height1 - height2}cm.")
else:
    print(f"{person2} is taller than {person1} by {height2 - height1}cm.")    

#solution2
person1 = input("Please enter name of person1?:")
person2 = input("Please enter name of person2?:")
height1 = float(input(f"Please tell the height of {person1}?:"))
height2 = float(input(f"Please tell me the height of {person2}?:"))
diff_height = abs(height1 - height2)

if height1 > height2:
    print(f"{person1} is taller than {person2} by {diff_height}cm.")
else:
    print(f"{person2} is taller than {person1} by {diff_height}cm.")    

#solution3
person1 = input("Please enter name of person1?:")
person2 = input("Please enter name of person2?:")
height1 = float(input(f"Please tell the height of {person1}?:"))
height2 = float(input(f"Please tell me the height of {person2}?:"))
diff_height = abs(height1 - height2)

if height1 > height2:
    print(f"{person1} is taller than {person2} by {diff_height}cm.")
elif height1 = height2:
    print(f"{person1} and {person2} are of same height")
else:
    print(f"{person2} is taller than {person1} by {diff_height}cm.")    

#if and else -> only one
#elif -> many

