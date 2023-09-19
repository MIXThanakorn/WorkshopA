print("โปรแกรมตรวจสอบผลการเรียนของนักเรียน")
print("--------------------------------------------")
def inputstu():
    students = int(input("How many students: "))
    return students

def process():
    students = inputstu()
    for i in range(1, students+1):
        stuname = input("Student name: ")
        stunumber = input("Student number: ")
        grade = int(input("Student grade: "))
        show(grade,stuname, stunumber)
    return stuname, stunumber, grade

def show(grade,stuname, stunumber):
    if grade >=2:
        print(f"{stunumber} {stuname} have {grade} สอบผ่าน")
    elif grade < 2:
        print(f"{stunumber} {stuname} have {grade} สอบไม่ผ่าน")
        
stuname,stunumber,grade = process()

        
        
