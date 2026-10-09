import pickle

n=int(input("Enter how amny students data you want to :"))


students=[]

for i in range(n):
    students_id=int(input("Enter studnts ID:"))
    name=input("Enter students name:")
    age=int(input("Enter stidents age:"))
    course=input("course name:")
    marks=int(input("student marks:"))

    student= {
        "Students Id":students_id,
        "students name":name,
        "Age":age,
        "course":course,
        "marks":marks
    }   
    students.append(student)

with open("students.dat","wb") as file:
    pickle.dump(students,file)
print("\npickling completed")


with open("students.dat","rb")as file:
    students=pickle.load(file)
print("Unpickling completed")
print(students)