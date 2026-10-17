#!/usr/bin/env python
# coding: utf-8

# In[7]:


employee_data={}

def add_employee():
    while True:
        emp_id=input("Enter Employee ID (or type 'stop' to finish) : " )

        if emp_id.lower()=="stop":
            print("Stopped adding employees")
            break
        if emp_id in employee_data:
            print("Employee already exist, please enter a new Employee ID")
            continue

        name=input("Enter Employee Name")
        age=int(input("Enter Employee Age: "))
        department=input("Enter Employee Department: ")
        salary=int(input("Enter Employee salary: "))
        employee_data[emp_id]={"Name": name, "Age": age, "Department": department,"Salary":salary}
        print("Employee was successfully added")
add_employee()


# In[19]:


def view_employee():
    if not employee_data:
        print("No employees found!!")
    else:
        print("\n================= All Employees Details ================")

        for emp_id,details in employee_data.items():
            print("\n Employee ID: ", emp_id)
            print("Name", details["Name"])
            print("Age: ", details["Age"])
            print("Department: ", details["Department"])
            print("Salary: ",details["Salary"])
            print("---------------------------------")
view_employee()


# In[24]:


def search_employee():
    emp_id=input("Enter the Employee ID to search: ")

    if emp_id in employee_data:
        print("\n ----------Employee Found----------")
        print("Employee ID: ",emp_id)
        print("Name: ", employee_data[emp_id]["Name"])
        print("Age: ", employee_data[emp_id]["Age"])
        print("Department", employee_data[emp_id]["Department"])
        print("Salary", employee_data[emp_id]["Salary"])
    else:
        print("Emmployee not found")

search_employee()


# In[ ]:


def main_menu():
        print("\n===========Employee Management System ==============")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
while True:
    main_menu()
    choice= input("Enter your Choice")
    if choice.lower()=="stop":
        print("Exiting employee management system.......")
    elif choice == "1":
        add_employee()
    elif choice == "2":
        view_employee()
    elif choice =="3":
        search_employee()
    elif choice =="4":
        print("Thank you for using the Employee Management System ! ")
        break
    else:
        print("Invalid choice.Please try again!")




# In[ ]:





# In[ ]:




