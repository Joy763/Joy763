marks = int(input("Enter your marks: "))

if marks>=80: grade = "A+"
elif marks>=75: grade = "A"
elif marks>=70: grade = "A-"
elif marks>=65: grade = "B+"
elif marks>=60: grade = "B"
elif marks>=55: grade = "B-"
elif marks>=50: grade = "C+"
else: grade = "F"

print("Your Grade is ", grade)