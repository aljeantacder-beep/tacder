

print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

math = float(input("Enter Math grade: "))
science = float(input("Enter Science grade: "))
english = float(input("Enter English grade: "))
filipino = float(input("Enter Filipino grade: "))
programming = float(input("Enter Programming grade: "))

average = (math + science + english + filipino + programming) / 5

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Average Grade:", round(average, 2))

if average >= 90:
    print("Remarks: Excellent")
    print("Letter Grade: A")
elif average >= 85:
    print("Remarks: Very Good")
    print("Letter Grade: B")
elif average >= 80:
    print("Remarks: Good")
    print("Letter Grade: C")
elif average >= 75:
    print("Remarks: Passed")
    print("Letter Grade: D")
else:
    print("Remarks: Failed")
    print("Letter Grade: F")

print("==========================")
