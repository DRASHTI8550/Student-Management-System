students = []

def details():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")

    students.append([name, age, city])
    print("Student Added Successfully!")

def view():
    if not students:
        print("No students found.")
    else:
        for i, s in enumerate(students, start=1):
            print(f"{i}. Name: {s[0]}, Age: {s[1]}, City: {s[2]}")

def update():
    view()

    student_no = int(input("Enter student number to update: "))

    if 1 <= student_no <= len(students):
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. City")                                         

        choice = int(input("Enter your choice: "))

        if choice == 1:
            students[student_no-1][0] = input("Enter new name: ")

        elif choice == 2:
            students[student_no-1][1] = int(input("Enter new age: "))

        elif choice == 3:
            students[student_no-1][2] = input("Enter new city: ")

        else:
            print("Invalid choice.")
            return

        print("Student updated successfully!")

    else:
        print("Invalid student number.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Exit")

    option = int(input("Enter choice: "))

    if option == 1:
        n = int(input("How many students? "))
        for i in range(n):
            details()

    elif option == 2:
        view()

    elif option == 3:
        update()

    elif option == 4:
        print("Thank You!")
        break

    else:
        print("Invalid choice.")

