name = input("Enter the student name:")

marks1 = float(input("Enter marks of subject1:"))
marks2 = float(input("Enter marks of subject2:"))
marks3 = float(input("Enter marks of subject3:"))
marks4 = float(input("Enter marks of subject4:"))

average = (marks1 + marks2 + marks3 + marks4)/4

print("Name:", name)
print("Average marks:", average)
if average>=90:
    grade = 'A'
elif average>=80:
    grade = 'B'
elif average>=70:
    grade = 'C'
elif average>=60:
    grade = 'D'
elif average>=50:
    grade = 'E'
else:
    grade = 'F'

print("Grade: ", grade)
