students_score = {
    "Draco": 74, "Hermione": 100,
    "Harry": 81, "Ron": 73, "Neville": 65
}
students_grade = {}

for i in students_score:
    score = students_score[i]
    if score > 90:
        students_grade[i] = "Outstanding"
    elif score > 80:
        students_grade[i] = "Exceeds Expectations"
    elif score > 70:
        students_grade[i] = "Acceptable"
    else: 
        students_grade[i] = "Fail"

print(students_grade)

