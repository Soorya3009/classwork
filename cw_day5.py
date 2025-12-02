# you are creating a basic system to manage students enrolled in various courses.
# Create two sets: one for students enrolled in "Python" and one for "Data Science".
# Add a new student to the Python set.
# Remove one student from the Data Science set.
# Find and display the names of students who are enrolled in both courses.
# Find students who are only in the Python course but not in Data Science.
# Display the combined list of all students in either course (no duplicates).
# Create a dictionary with course names as keys and number of students as values.
# Using a loop, print the course name and number of students in the format:
# Course: Python, Students: 3
# Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled (to simulate expected growth)



python_students = {"Aarav", "Diya", "Kiran"}
data_science_students = {"Diya", "Meera", "Rohan"}


python_students.add("Sanjay")


data_science_students.remove("Meera")

both_courses = python_students.intersection(data_science_students)
print("Students in both courses:", both_courses)


only_python = python_students.difference(data_science_students)
print("Only in Python:", only_python)


all_students = python_students.union(data_science_students)
print("All students (no duplicates):", all_students)

course_dict = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}


for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")


expected_growth = {course: count * 2 for course, count in course_dict.items()}
print("Expected growth:", expected_growth)