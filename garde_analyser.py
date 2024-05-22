students = {
    "Alice":[75,76,92,63],
    "George":[82,65,72,50],
    "Masha":[90,34,45,75],
    "Christopher":[73,56,32,93]
}



def average(students):
    for student in students.values():
        avg_mark = sum(student) / len(student) 
        print(avg_mark)

average(students)




