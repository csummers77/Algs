students =[
    'rob',
    'chris',
    'jim',
    'jason',
    'brian',
    'brandon',
    'zac',
    'j.r',
    'greg',
    'ron',
    'katie',
    'sean',
    'gbenga',
    'khanh',
    'connor',
    'cody',
    'mike',
    'matt'
]
# take the list 'students' randomly pair 2
# students until all students have been used
import random
# print len(students)

def get_student():
    #gets a random student!
    rand_num = random.randint(0,len(students)-1)
    current_student = students[rand_student_index]
    # we haave picked a student. remove that value from the 
    students.remove(current_student)
    return current_student

while (len(students)> 0:
    student1 = get_student()
    student2 = get_student()
    print ("%s is paried with %s." % (student1, student2))
    