student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades ={}
'''
This is the scoring criteria:

    Scores 91 - 100: Grade = "Outstanding"

    Scores 81 - 90: Grade = "Exceeds Expectations"

    Scores 71 - 80: Grade = "Acceptable"

    Scores 70 or lower: Grade = "Fail"
'''
# TODO-2: Write your code below to add the grades to student_grades.👇
# Looping through key-value pairs using items()
for key, value in student_scores.items():
    if int(value) in range(91,100):
        grade = "Outstanding"
    elif int(value) in range(81,90):
        grade = "Exceeds Expectations"
    elif int(value) in range(71,80):
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade
# 🚨 Don't change the code below 👇
print(student_grades)