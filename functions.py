students = []


def signup_student():
    student_name = input('Nombre del estudiante: ')
    student_name_list = student_name.split(',')

    if student_name_list[0] == "Cesar":
        print('No guardo este estudiante')
        return

    student = {
        "first_name": student_name_list[0],
        "last_name": student_name_list[1]
    }

    return (student, student_name)


student, string_student = signup_student()
print(student, string_student)