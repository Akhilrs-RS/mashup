frontend_students = {"Akhil", "Meera", "John", "Sara"}
backend_students = {"Meera", "Rahul", "John"}

backend_students.add("Vishnu")

frontend_students.discard("Sara")   # discard avoids error if name not found

both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)

only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)

unique_students = frontend_students | backend_students
print("Total unique students:", len(unique_students))

course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

for course, count in course_counts.items():
    print(f"{course}: {count} students")

full_course_dict = {**course_counts,
                    "Fullstack": course_counts["Frontend"] + course_counts["Backend"]}

print("Updated course dictionary with Fullstack:", full_course_dict)