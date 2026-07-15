import controller

def confirm_action(message):
    confirmation = input(f"\n{message} (y/n): ").strip().lower()
    return confirmation == 'y'

def login_menu():
    print("=====================================")
    print("               LOG IN")
    print("=====================================")
    print("----- Welcome to the School Management System -----")
    
    tries = 0
    while tries < 6:
        username = input("Enter your Username or type exit: ").strip()
        if username.lower() != "exit":
            password = input("Enter your Password: ").strip()
            access = controller.log_in(username, password)
            if not access:
                print("The username or password is not valid\n")
                tries += 1
            else:
                print(f"Welcome Back {username}!")
                return access
        else: 
            return None
    return None

def show_admin_menu():
    print("\n=====================================")
    print("          ADMIN MENU")
    print("=====================================")
    print("1. Set Up the Database")
    print("2. Register Data in Database")
    print("3. Read Data from Database")
    print("4. Update Data from Database")
    print("5. Delete Data from Database")
    print("6. Reset the Database")
    print("7. Seed the Database (Testing)")
    print("8. Exit")
    print("=====================================\n")

def admin_menu():
    on = True
    while on:
        show_admin_menu()
        option = input("Select an option (1-8): ").strip()
        
        if option == "1":
            print(controller.database_setup())
            
        elif option == "2":
            register_menu()
            
        elif option == "3":
            read_menu()
        
        elif option == "4":
            update_menu()
        
        elif option == "5":
            delete_menu()
            
        elif option == "6":
            if confirm_action("Are you sure you want to RESET the database?"):
                print(controller.database_reset())
        
        elif option == "7":
            print(controller.database_test())
        
        elif option == "8":
            return None
        
        else:
            print("Invalid option. Please enter a number between 1 and 8.\n")

def show_register_menu():
    print("\n=====================================")
    print("          REGISTER DATA")
    print("=====================================")
    print("1. Register an Office / House")
    print("2. Register a Staff Member")
    print("3. Register a Class")
    print("4. Register a Student")
    print("5. Add Class to Student Schedule")
    print("6. Make an Appointment")
    print("7. Go Back")
    print("=====================================\n")

def register_menu():
    on = True
    while on:
        show_register_menu()
        option = input("Select an option (1-7): ").strip()
            
        if option == "1":
            print("\n========== ENTER OFFICE INFO ==========")
            name = input("Enter Office Name: ").strip()
            room = input("Enter Room Number (A000): ").strip()
            admin_id = input("Enter Office Admin ID: ").strip()
            print(controller.register_office(name, room, admin_id))
            
        elif option == "2":
            print("\n========== ENTER STAFF MEMBER INFO ==========")
            name = input("Enter Staff Member First Name: ").strip()
            last_name = input("Enter Staff Member Last Name: ").strip()
            password = input("Enter Staff Member User Password: ").strip()
            branch = input("Enter Staff Member Branch: ").strip()
            
            role = ""
            while role not in {"admin", "teacher"}:
                role = input("Enter Staff Member Role (admin or teacher): ").lower().strip()
                if role not in {"admin", "teacher"}:
                    print("Role Not Valid, Try Again!")
            
            print(controller.register_staff(name, last_name, password, branch, role))
            
        elif option == "3":
            print("\n========== ENTER CLASS INFO ==========")
            name = input("Enter Class Name: ").strip()
            teacher_id = input("Enter Class Teacher ID: ").strip()
            hour = input("Enter Class Hour (HH:MM): ").strip()
            room = input("Enter Class Room (A000): ").strip()
            print(controller.register_class(name, teacher_id, hour, room))
            
        elif option == "4":
            print("\n========== ENTER STUDENT INFO ==========")
            name = input("Enter Student First Name: ").strip()
            last_name = input("Enter Student Last Name: ").strip()
            password = input("Enter Student User Password: ").strip()
            
            house_id = None
            while not house_id:
                house_name = input("Enter Student House Name: ").strip()
                house_id = controller.get_house_id_by_name(house_name)
                if not house_id:
                    print("Error With House Name, Try Again!")
            
            parent_phone = input("Enter Parent Phone Number: ").strip()
            parent_id = controller.get_parent_id_by_phone(parent_phone)
            
            if not parent_id:
                print("Parent Not Found. Please register parent first.")
                print("\n========== ENTER PARENT INFO ==========")
                p_name = input("Enter Parent Name: ").strip()
                p_last_name = input("Enter Parent Last Name: ").strip()
                p_phone_number = input("Enter Parent Phone Number: ").strip()
                p_email = input("Enter Parent Email: ").strip()
                p_address = input("Enter Parent Address: ").strip()
                
                controller.register_parent(p_name, p_last_name, p_phone_number, p_email, p_address)
                parent_id = controller.get_parent_id_by_phone(parent_phone)
            
            print(controller.register_student(name, last_name, password, house_id, parent_id))
            
        elif option == "5":
            print("\n========== Enter Schedule Info ==========")
            student_id = input("Enter Student ID: ").strip()
            class_id = input("Enter Class ID: ").strip()
            print(controller.add_class(student_id, class_id))
        
        elif option == "6":
            print("\n========== Enter Appointment Info ==========")
            student_id = input("Enter Student ID: ").strip()
            office_id = input("Enter Office ID: ").strip()
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            hour = input("Enter Hour (HH:MM): ").strip()
            print(controller.create_appointment(student_id, office_id, date, hour))
            
        elif option == "7":
            on = False
        
        else:
            print("Invalid option. Please enter a number between 1 and 7.\n")

def show_read_menu():
    print("\n=====================================")
    print("              READ MENU")
    print("=====================================")
    print("1. Search a Table (View All)")
    print("2. Search an Entity by ID")
    print("3. Search Student Schedule")
    print("4. Search Class Roster")
    print("5. Search Teacher's Assigned Classes")
    print("6. Search Appointments by Date")
    print("7. Search Appointments by Student")
    print("8. View Students Without Classes")
    print("9. Go Back")
    print("=====================================\n")

def read_menu():
    on = True
    while on:
        show_read_menu()
        option = input("Select an option (1-9): ").strip()
        
        if option == "1":
            table = input("Enter Table Name (students, classes, staff, parents, offices): ").lower().strip()
            print(controller.view_table(table))
        
        elif option == "2":
            table = input("Enter Table Name (students, classes, staff, parents, offices): ").lower().strip()
            ID = input("Enter ID: ").strip()
            print(controller.view_by_ID(table, ID))
        
        elif option == "3":
            student_id = input("Enter Student ID: ").strip()
            print(controller.view_student_schedule(student_id))
        
        elif option == "4":
            class_id = input("Enter Class ID: ").strip()
            print(controller.view_class_roster(class_id))
        
        elif option == "5":
            teacher_id = input("Enter Teacher ID: ").strip()
            print(controller.view_teacher_schedule(teacher_id))
        
        elif option == "6":
            date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
            print(controller.view_appointments_by_date(date))
        
        elif option == "7":
            student_id = input("Enter Student ID: ").strip()
            print(controller.view_appointments_by_student(student_id))
        
        elif option == "8":
            print(controller.view_students_without_classes())
        
        elif option == "9":
            on = False
        
        else:
            print("Invalid option. Please enter a number between 1 and 9.\n")

def show_update_menu():
    print("\n=====================================")
    print("          UPDATE DATA")
    print("=====================================")
    print("1. Update a Parent / Guardian Info")
    print("2. Update an Office / House Info")
    print("3. Update a Staff Member Info")
    print("4. Update a Class Info")
    print("5. Update a Student Info")
    print("6. Update Student Schedule")
    print("7. Update Student Appointment")
    print("8. Go Back")
    print("=====================================\n")

def update_menu():
    on = True
    while on:
        show_update_menu()
        option = input("Select an option (1-8): ").strip()
        
        if option == "1":
            print("\n========== Update Parent Info ==========")
            parent_id = input("Enter Parent ID: ").strip()
            current = controller.get_parent_data(parent_id)
            if current:
                new_name = input(f"Enter New Name (or Blank to Keep '{current[1]}'): ").strip()
                new_last_name = input(f"Enter New Last Name (or Blank to Keep '{current[2]}'): ").strip()
                new_phone = input(f"Enter New Phone Number (or Blank to Keep '{current[3]}'): ").strip()
                new_email = input(f"Enter New Email (or Blank to Keep '{current[4]}'): ").strip()
                new_address = input(f"Enter New Address (or Blank to Keep '{current[5]}'): ").strip()
                print(controller.update_parent(parent_id, new_name, new_last_name, new_phone, new_email, new_address))
            else:
                print(f"\nParent ID {parent_id} Not Found.")
            
        elif option == "2":
            print("\n========== Update Office Info ==========")
            office_id = input("Enter Office ID: ").strip()
            current = controller.get_office_data(office_id)
            if current:
                new_name = input(f"Enter New Name (or Blank to Keep '{current[1]}'): ").strip()
                new_room = input(f"Enter New Room Number (or Blank to Keep '{current[2]}'): ").strip()
                new_admin_id = input(f"Enter New Admin ID (or Blank to Keep '{current[3]}'): ").strip()
                print(controller.update_office(office_id, new_name, new_room, new_admin_id))
            else:
                print(f"\nOffice ID {office_id} Not Found.")
            
        elif option == "3":
            print("\n========== Update Staff Info ==========")
            staff_id = input("Enter Staff ID: ").strip()
            current = controller.get_staff_data(staff_id)
            if current:
                new_name = input(f"Enter New Name (or Blank to Keep '{current[1]}'): ").strip()
                new_last_name = input(f"Enter New Last Name (or Blank to Keep '{current[2]}'): ").strip()
                new_email = input(f"Enter New Email (or Blank to Keep '{current[3]}'): ").strip()
                new_branch = input(f"Enter New Branch (or Blank to Keep '{current[4]}'): ").strip()
                print(controller.update_staff(staff_id, new_name, new_last_name, new_email, new_branch))
            else:
                print(f"\nStaff ID {staff_id} Not Found.")
            
        elif option == "4":
            print("\n========== Update Class Info ==========")
            class_id = input("Enter Class ID: ").strip()
            current = controller.get_class_data(class_id)
            if current:
                new_name = input(f"Enter New Name (or Blank to Keep '{current[1]}'): ").strip()
                new_hour = input(f"Enter New Hour (or Blank to Keep '{current[2]}'): ").strip()
                new_room = input(f"Enter New Room Number (or Blank to Keep '{current[3]}'): ").strip()
                new_teacher_id = input(f"Enter New Teacher ID (or Blank to Keep '{current[4]}'): ").strip()
                print(controller.update_class(class_id, new_name, new_hour, new_room, new_teacher_id))
            else:
                print(f"\nClass ID {class_id} Not Found.")
            
        elif option == "5":
            print("\n========== Update Student Info ==========")
            student_id = input("Enter Student ID: ").strip()
            current = controller.get_student_data(student_id)
            if current:
                new_name = input(f"Enter New Name (or Blank to Keep '{current[1]}'): ").strip()
                new_last_name = input(f"Enter New Last Name (or Blank to Keep '{current[2]}'): ").strip()
                new_email = input(f"Enter New Email (or Blank to Keep '{current[4]}'): ").strip()
                new_house_id = input(f"Enter New House ID (or Blank to Keep '{current[5]}'): ").strip()
                new_parent_id = input(f"Enter New Parent ID (or Blank to Keep '{current[6]}'): ").strip()
                print(controller.update_student(student_id, new_name, new_last_name, new_email, new_house_id, new_parent_id))
            else:
                print(f"\nStudent ID {student_id} Not Found.")
            
        elif option == "6":
            print("\n========== Update Schedule Info ==========")
            student_id = input("Enter Student ID: ").strip()
            schedule_visual = controller.view_student_schedule(student_id)
            print(schedule_visual)
            if "No Classes Found" not in schedule_visual:
                print("\n---------------------------------------------")
                hour = input("Enter the Hour to Change (HH:MM): ").strip()
                class_id = controller.get_schedule_classID(student_id, hour)
                new_class_id = input("Enter New Class ID: ").strip()
                print(controller.update_schedule(new_class_id, student_id, class_id))
            
        elif option == "7":
            print("\n========== Update Appointment Info ==========")
            appointment_id = input("Enter Appointment ID: ").strip()
            current = controller.get_appointment_data(appointment_id)
            if current:
                new_date = input(f"Enter New Date (YYYY-MM-DD) (or Blank to Keep '{current[3]}'): ").strip()
                new_hour = input(f"Enter New Hour (HH:MM) (or Blank to Keep '{current[4]}'): ").strip()
                print(controller.update_appointment(appointment_id, new_date, new_hour))
            else:
                print(f"\nAppointment ID {appointment_id} Not Found.")
        
        elif option == "8":
            on = False
        
        else:
            print("Invalid option. Please enter a number between 1 and 8.\n")

def show_delete_menu():
    print("\n=====================================")
    print("          DELETE DATA")
    print("=====================================")
    print("1. Delete an Office / House")
    print("2. Delete a Staff Member")
    print("3. Delete a Class")
    print("4. Delete a Student")
    print("5. Drop a Class")
    print("6. Cancel an Appointment")
    print("7. Go Back")
    print("=====================================\n")

def delete_menu():
    on = True
    while on:
        show_delete_menu()
        option = input("Select an option (1-7): ").strip()
            
        if option == "1":
            print("\n========== Delete Office Info ==========")
            office_id = input("Enter Office ID: ").strip()
            if confirm_action(f"Are you sure you want to eliminate office {office_id}?"):
                print(controller.delete_office(office_id))
            
        elif option == "2":
            print("\n========== Delete Staff Info ==========")
            staff_id = input("Enter Staff Member ID: ").strip()
            if confirm_action(f"Are you sure you want to eliminate staff {staff_id}?"):
                print(controller.delete_staff(staff_id))
            
        elif option == "3":
            print("\n========== Delete Class Info ==========")
            class_id = input("Enter Class ID: ").strip()
            if confirm_action(f"Are you sure you want to eliminate class {class_id}?"):
                print(controller.delete_class(class_id))
            
        elif option == "4":
            print("\n========== Delete Student Info ==========")
            student_id = input("Enter Student ID: ").strip()
            if confirm_action(f"Are you sure you want to eliminate student {student_id}?"):
                parent_id = controller.get_parentID_by_student(student_id)
                # Obtenemos los estudiantes ANTES de borrar al estudiante actual
                count = controller.get_students_by_parent(parent_id)
                
                print(controller.delete_student(student_id))
                
                # Al eliminar este estudiante, calculamos si el padre queda huérfano de alumnos
                if count <= 1:
                    if confirm_action(f"Parent / Guardian {parent_id} now has 0 students, Do you want to eliminate him?"):
                        print(controller.delete_parent(parent_id))
            
        elif option == "5":
            print("\n========== Delete Schedule Info ==========")
            student_id = input("Enter Student ID: ").strip()
            schedule_visual = controller.view_student_schedule(student_id)
            print(schedule_visual)
            if "No Classes Found" not in schedule_visual:
                print("\n---------------------------------------------")
                hour = input("Enter the Hour to Delete (HH:MM): ").strip()
                class_id = controller.get_schedule_classID(student_id, hour)
                print(controller.drop_class(student_id, class_id))
            
        elif option == "6":
            print("\n========== Cancel Appointment ==========")
            appointment_id = input("Enter Appointment ID: ").strip()
            if confirm_action(f"Are you sure you want to eliminate appointment {appointment_id}?"):
                print(controller.cancel_appointment(appointment_id))
        
        elif option == "7":
            on = False
        
        else:
            print("Invalid option. Please enter a number between 1 and 7.\n")

def show_student_menu():
    print("\n=====================================")
    print("          STUDENT PORTAL")
    print("=====================================")
    print("1. See & Edit Personal Info")
    print("2. View Class Catalog")
    print("3. Enroll in a Class")
    print("4. Drop a Class")
    print("5. View My Schedule")
    print("6. Make an Appointment")
    print("7. View My Appointments")
    print("8. Cancel My Appointments")
    print("9. Go Back")
    print("=====================================\n")

def student_menu(student_id):
    on = True
    while on:
        show_student_menu()
        option = input("Select an option (1-9): ").strip()
            
        if option == "1":
            current = controller.get_student_data(student_id)
            if current:
                new_name = input(f"Enter New Name (or Blank to Keep '{current[1]}'): ").strip()
                new_last_name = input(f"Enter New Last Name (or Blank to Keep '{current[2]}'): ").strip()
                new_email = input(f"Enter New Email (or Blank to Keep '{current[4]}'): ").strip()
                new_house_id = input(f"Enter New House ID (or Blank to Keep '{current[5]}'): ").strip()
                new_parent_id = input(f"Enter New Parent ID (or Blank to Keep '{current[6]}'): ").strip()
                print(controller.update_student(student_id, new_name, new_last_name, new_email, new_house_id, new_parent_id))
            
        elif option == "2":
            print(controller.view_class_catalog())
            
        elif option == "3":
            print("\n========== Enter Schedule Info ==========")
            class_id = input("Enter Class ID: ").strip()
            print(controller.add_class(student_id, class_id))
            
        elif option == "4":
            schedule_visual = controller.view_student_schedule(student_id)
            print(schedule_visual)
            if "No Classes Found" not in schedule_visual:
                print("\n---------------------------------------------")
                hour = input("Enter the Hour to Delete (HH:MM): ").strip()
                class_id = controller.get_schedule_classID(student_id, hour)
                print(controller.drop_class(student_id, class_id))
            
        elif option == "5":
            print(controller.view_student_schedule(student_id))
            
        elif option == "6":
            print("\n========== Enter Appointment Info ==========")
            office_id = input("Enter Office ID: ").strip()
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            hour = input("Enter Hour (HH:MM): ").strip()
            print(controller.create_appointment(student_id, office_id, date, hour))
        
        elif option == "7":
            print(controller.view_student_appointments(student_id))
        
        elif option == "8":
            print("\n========== Cancel Appointment ==========")
            appointment_id = input("Enter Appointment ID: ").strip()
            if confirm_action(f"Are you sure you want to eliminate appointment {appointment_id}?"):
                print(controller.cancel_appointment(appointment_id))
        
        elif option == "9":
            on = False
        
        else:
            print("Invalid option. Please enter a number between 1 and 9.\n")

def show_teacher_menu():
    print("\n=====================================")
    print("          TEACHER PORTAL")
    print("=====================================")
    print("1. View My Assigned Classes")
    print("2. View Class Roster")
    print("3. Search Student Profile")
    print("4. See & Edit Personal Info")
    print("5. Email All Students in a Class")
    print("6. Contact Student's Parent")
    print("7. Go Back")
    print("=====================================\n")

def teacher_menu(teacher_id):
    on = True
    while on:
        show_teacher_menu()
        option = input("Select an option (1-7): ").strip()
            
        if option == "1":
            print(controller.view_teacher_schedule(teacher_id))
            
        elif option == "2":
            class_id = input("Enter Class ID: ").strip()
            print(controller.view_class_roster(class_id))
            
        elif option == "3":
            student_id = input("Enter Student ID: ").strip()
            print(controller.view_by_ID("students", student_id))
            
        elif option == "4":
            current = controller.get_staff_data(teacher_id)
            if current:
                new_name = input(f"Enter New Name (or Blank to Keep '{current[1]}'): ").strip()
                new_last_name = input(f"Enter New Last Name (or Blank to Keep '{current[2]}'): ").strip()
                new_email = input(f"Enter New Email (or Blank to Keep '{current[3]}'): ").strip()
                new_branch = input(f"Enter New Branch (or Blank to Keep '{current[4]}'): ").strip()
                print(controller.update_staff(teacher_id, new_name, new_last_name, new_email, new_branch))
            
        elif option == "5":
            class_id = input("Enter Class ID: ").strip()
            print(controller.send_email(class_id))
            
        elif option == "6":
            student_id = input("Enter Student ID: ").strip()
            email, parent_info = controller.view_parent_contact(student_id)
            print(parent_info)
            if email:
                if confirm_action(f"Do you want to send an email to {email}?"):
                    print(f"\nEmail sent to {email}")
        
        elif option == "7":
            on = False
        
        else:
            print("Invalid option. Please enter a number between 1 and 7.\n")

def main():
    access = login_menu()
    while access:
        user_id = access[0]
        role = access[1]
        print(f"\nLogged in as: {role.upper()}")
        
        if role == "admin":
            access = admin_menu()
            
        elif role == "teacher":
            teacher_menu(user_id)
            access = login_menu()
        
        elif role == "student":
            student_menu(user_id)
            access = login_menu()
        
        else:
            print("No way this error is possible\n")
            
    print("Thanks for using the School Management System. Goodbye!")

if __name__ == "__main__":
    main()
