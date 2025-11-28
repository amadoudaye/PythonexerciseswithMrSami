def student_stats(grades):
    # Find the student with the highest grade
    highest_student = max(grades, key=grades.get)
    highest_grade = grades[highest_student]

    # Calculate the average
    average_grade = sum(grades.values()) / len(grades)

    return highest_student, highest_grade, round(average_grade, 2)
students = {"Alex": 85, "Sam": 90, "John": 78}

result = student_stats(students)
print("Highest:", result[0], result[1])
print("Average:", result[2])