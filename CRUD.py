
from connect import connect_to_mysql
import mysql.connector


# Create the three connected tables.
def create_tables():
    connection = connect_to_mysql()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        # Table 1: Store student information.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE
            )
        """)

        # Table 2: Store course information.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                course_name VARCHAR(100) NOT NULL UNIQUE
            )
        """)

        # Table 3: Connect students and courses.
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT NOT NULL,
                course_id INT NOT NULL,

                FOREIGN KEY (student_id)
                    REFERENCES students(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (course_id)
                    REFERENCES courses(id)
                    ON DELETE CASCADE,

                UNIQUE (student_id, course_id)
            )
        """)

        connection.commit()
        print("Three connected tables are ready!")

    except mysql.connector.Error as error:
        print(f"Error creating tables: {error}")

    finally:
        cursor.close()
        connection.close()


# Add a new student.
def create_student():
    name = input("Enter student name: ").strip()
    email = input("Enter student email: ").strip()

    if not name or not email:
        print("Name and email are required.")
        return

    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, email) VALUES (%s, %s)",
            (name, email)
        )
        connection.commit()
        print(f"Student added! ID: {cursor.lastrowid}")

    except mysql.connector.Error as error:
        print(f"Could not add student: {error}")

    finally:
        cursor.close()
        connection.close()


# Add a new course.
def create_course():
    course_name = input("Enter course name: ").strip()

    if not course_name:
        print("Course name is required.")
        return

    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO courses (course_name) VALUES (%s)",
            (course_name,)
        )
        connection.commit()
        print(f"Course added! ID: {cursor.lastrowid}")

    except mysql.connector.Error as error:
        print(f"Could not add course: {error}")

    finally:
        cursor.close()
        connection.close()


# Display students and courses with their IDs.
def view_students_and_courses():
    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        print("\n--- STUDENTS ---")
        cursor.execute("SELECT id, name, email FROM students")

        for student in cursor.fetchall():
            print(student)

        print("\n--- COURSES ---")
        cursor.execute("SELECT id, course_name FROM courses")

        for course in cursor.fetchall():
            print(course)

    except mysql.connector.Error as error:
        print(f"Could not display records: {error}")

    finally:
        cursor.close()
        connection.close()


# Enroll a student in a course.
def enroll_student():
    view_students_and_courses()

    try:
        student_id = int(input("\nEnter student ID: "))
        course_id = int(input("Enter course ID: "))
    except ValueError:
        print("IDs must be numbers.")
        return

    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO enrollments (student_id, course_id)
            VALUES (%s, %s)
            """,
            (student_id, course_id)
        )

        connection.commit()
        print("Student enrolled successfully!")

    except mysql.connector.Error as error:
        print(f"Enrollment failed: {error}")

    finally:
        cursor.close()
        connection.close()


# Read all enrollment records from the three tables.
def read_enrollments():
    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                enrollments.id,
                students.name,
                students.email,
                courses.course_name
            FROM enrollments
            JOIN students
                ON enrollments.student_id = students.id
            JOIN courses
                ON enrollments.course_id = courses.id
            ORDER BY enrollments.id
        """)

        records = cursor.fetchall()

        if not records:
            print("No enrollment records found.")
            return

        print("\nID | Student | Email | Course")
        print("-" * 70)

        for record in records:
            print(
                f"{record[0]} | {record[1]} | "
                f"{record[2]} | {record[3]}"
            )

    except mysql.connector.Error as error:
        print(f"Could not read enrollments: {error}")

    finally:
        cursor.close()
        connection.close()


# Update the course of an existing enrollment.
def update_enrollment():
    read_enrollments()

    try:
        enrollment_id = int(
            input("\nEnter enrollment ID to update: ")
        )
        new_course_id = int(
            input("Enter new course ID: ")
        )
    except ValueError:
        print("IDs must be numbers.")
        return

    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            UPDATE enrollments
            SET course_id = %s
            WHERE id = %s
        """, (new_course_id, enrollment_id))

        connection.commit()

        if cursor.rowcount > 0:
            print("Enrollment updated successfully!")
        else:
            print("Enrollment not found or no changes made.")

    except mysql.connector.Error as error:
        print(f"Could not update enrollment: {error}")

    finally:
        cursor.close()
        connection.close()


# Delete an enrollment using its ID.
def delete_enrollment():
    read_enrollments()

    try:
        enrollment_id = int(
            input("\nEnter enrollment ID to delete: ")
        )
    except ValueError:
        print("Enrollment ID must be a number.")
        return

    connection = connect_to_mysql()
    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM enrollments WHERE id = %s",
            (enrollment_id,)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Enrollment deleted successfully!")
        else:
            print("Enrollment ID not found.")

    except mysql.connector.Error as error:
        print(f"Could not delete enrollment: {error}")

    finally:
        cursor.close()
        connection.close()


# Main CRUD menu.
def run_menu():
    create_tables()

    while True:
        print("\n===== SCHOOL DATABASE CRUD =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. View Students and Courses")
        print("4. Enroll Student in Course")
        print("5. View All Enrollments")
        print("6. Update Enrollment")
        print("7. Delete Enrollment")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_student()

        elif choice == "2":
            create_course()

        elif choice == "3":
            view_students_and_courses()

        elif choice == "4":
            enroll_student()

        elif choice == "5":
            read_enrollments()

        elif choice == "6":
            update_enrollment()

        elif choice == "7":
            delete_enrollment()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1-8.")


if __name__ == "__main__":
    run_menu()

