import pickle

employee_id= int(input("Enter Employee ID:"))
name = input("Enter Employee Name:")
salary = float(input("Enter salary:"))
skills = input("Enter skills:")

employee = {
    "id":employee_id,
    "name":name,
    "salary": salary,
    "skills": skills

}
with open ("employee.dat","wb") as file:
    pickle.dump(employee,file)

print("\nPickling completed!")


with open("employee.dat","rb") as file:
    employee = pickle.load(file)

print("Unpickling completed")
