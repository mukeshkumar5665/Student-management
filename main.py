student = []


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        new_student = {}

        name = input("Enter student name: ")
        age = input("Enter age: ") 

        new_student["name"] = name
        new_student["age"] = age

        student.append(new_student)
        print("student add successfully")


    # View Students
    elif choice == "2": 
        if len(student) == 0:
            print("No Student Data Available ")
        else:
            for i, person in enumerate(student, start=1):
                print(f"{i}. {person}")



    # search student
    elif choice == "3":
        search_student = input("Enter Student Name: ").lower()
       
        for preson in student:
            if preson["name"].lower() == search_student:
                print("Studdent Found")
                print(preson)
                
                break

        else:
            print("Student Not Found")
        


    # Update student
    elif choice == "4":
        update_name = input("Enter Student Name: ").lower()

        for person in student:
            if person["name"].lower() == update_name:
                print("Student Found")
                print(person)

                new_name = input("Enter new name: ")
                new_age = input("Enter new age: ")

                person["name"] = new_name
                person["age"] = new_age

                print("Student Updated Successfully")
                break
        else:
            print("Student Not Found")



    # Delete student
    elif choice == "5":        
        delete_name = input("Enter Student Name Delete: ").lower()
        
        found = False
        for preson in student:
            if preson["name"].lower() == delete_name:
                student.remove(preson)
                found = True
                print("Studdent Deleted Successfully")
                break

        else:
            print("Student Not Found")



    # Exit 
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

