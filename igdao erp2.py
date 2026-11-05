#3 Igdao
class Student:
    def  __init__(self,student_id, name ,course, year_level):
        self.student_id = student_id
        self.id = id
        self.name = name
        self.course = course
        self.year = self.year
        self.level = year_level

    
    def add_subject(self,subject):
        if subject in self.subjects:
            print(f"Subject {subject} already exist.")
        else:
            self.subjects[subject] = None

    def record_grade(self,subject,grade):
        if subject not in self.subjects:
            print(f"Subject {subject} has not been added yet.")
            return
        if not(0 <= grade <= 100):
            print("Grade must be between 0 and 100.")
            return
        self.subjects[subject] = grade

    def calculate_average(self):
        grades = []

        for grade in self.subjects.values():
            if grade is not None:
                grades.append(grade)

        if not grades:
            return None

        average = sum(grades) / len(grades)
        return average


    def highest_grade(self):
        grades = []

        for grade in self.subjects.values():
            if grade is not None:
                grades.append(grade)

        if not grades:
            return None

        return max(grades)

    def lowest_grade(self):
        grades = []

        for grade in self.subjects.values():
            if grade is not None:
                grades.append(grade)

        if not grades:
            return None

        return min(grades)

    def get_status(self):
        average = self.calculate_average()

        if average is None:
            return "No grades recorded"

        return "Passed" if average >= 75 else "Failed"

    def display_report(self):
        print("==========================")
        print("     STUDENT GRADE REPORT")
        print("==========================")

        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year Level: {self.year_level}")

        print("\nSubjects:")
        print("==========================")

        for subject,grade in self.subjects.items():
            if grade is None:
                print(f"{subject} : No Grade")
            else:
                print(f"{subject} : {grade}")

        print("==========================")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Highest: {self.highest_grade()}")
        print(f"Lowest: {self.lowest_grade()}")
        print(f"Status: {self.get_status()}")



    s1 = Student