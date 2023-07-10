from src.student import Student

student_1 = Student("John","E65")

print(f"{student_1.name} is in {student_1.cohort}")

print(student_1.talk())

print(student_1.say_favourite_language("JavaScript"))