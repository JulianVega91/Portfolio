import db_setup
import db_writer
import db_reader

# SET UP

def log_in(username, password):
    return db_reader.log_in(username, password)

def database_setup():
    db_setup.create_database()
    return "\n----- Database Set Up Complete -----\n"

def database_reset():
    db_setup.erase_database()
    db_setup.create_database()
    return "\n----- Database Reset Complete -----\n"

def database_test():
    db_setup.seed_database()
    return "\n----- Database Test Data Complete -----\n"

# READ

def view_table(table):
    valid_tables = ["students", "classes", "staff", "parents", "offices"]
    table = table.lower().strip()
    message = ""
    if table in valid_tables:
        rows = db_reader.get_table(table)
        if not rows:
            message = f"\nThe Table '{table}' is Currently Empty."
        else:
            message = f"\n--- DATA FROM TABLE: {table.upper()} ---"
            for row in rows:
                message += f"\n{row}"
    else:
        message = f"{table} Not Valid, Only students, classes, staff, parents or offices are Valid"
    return message
    
def view_by_ID(table, ID):
    valid_tables = ["students", "classes", "staff", "parents", "offices"]
    table = table.lower().strip()
    ID = ID.strip()
    message = ""
    if table in valid_tables:
        rows, columns = db_reader.get_by_ID(table, ID)
        
        if not rows:
            message = f"\nNo Data Found for Id '{ID}' in Table '{table}'."
        else:
            message = f"\n--- DATA FROM TABLE: {table.upper()} ---"
            for row in rows:
                for column_name, value in zip(columns, row):
                    message += f"\n{column_name.upper()}: {value}"
    else:
        message = f"{table} not valid, only students, classes, staff, parents or offices are valid"
    return message

def view_student_schedule(student_id):
    student_id = student_id.strip()
    message = ""
    rows = db_reader.get_student_schedule(student_id)
    if not rows:
        message = f"\nNo Classes Found for Student Id: {int(student_id):04d}"
    else:
        message = f"\n--- SCHEDULE FOR STUDENT {int(student_id):04d} ---"
        for row in rows:
            message += f"\n[{row[1]}] {row[0]} - Room: {row[2]}"
    return message

def view_class_roster(class_id):
    class_id = class_id.strip()
    message = ""
    rows = db_reader.get_class_roster(class_id)
    if not rows:
        message = f"\nNo Students Found for Class Id: {int(class_id):04d}"
    else:
        message = f"\n--- STUDENTS FOR CLASS {int(class_id):04d} ---"
        for row in rows:
            message += f"\nStudent Id: {row[0]} | Student Name: {row[1]} {row[2]}"
    return message

def view_class_catalog():
    message = ""
    rows = db_reader.get_class_catalog()
    if not rows:
        message = f"\nNo Classes in the Data Base Yet"
    else:
        message = f"\n--- CLASS CATALOG ---"
        for row in rows:
            message += f"\nClass Id: {row[0]} | Class Name: {row[1]} | Class Hour: {row[2]} | Class Room: {row[3]} | Class Teacher: {row[5]} {row[6]}"
    return message

def view_student_appointments(student_id):
    student_id = student_id.strip()
    message = ""
    rows = db_reader.get_student_appointments(student_id)
    if not rows:
        message = f"\nNo Appointments Found for Student Id: {int(student_id):04d}"
    else:
        message = f"\n--- APPOINTMENTS FOR STUDENT {int(student_id):04d} ---"
        for row in rows:
            message += f"\nAppointment Id: {row[0]} | Appointment Date: {row[3]} at {row[4]} Office Name: {row[5]} | Office Room: {row[6]}"
    return message

def view_students_without_classes():
    message = ""
    rows = db_reader.get_students_without_classes()
    if not rows:
        message = f"\nAll Students are Enrolled in Classes"
    else:
        message = f"\n--- STUDENTS WITH NO CLASSES ---"
        for row in rows:
            message += f"\nStudent Id: {row[0]} | Student Name: {row[1]} {row[2]} "
    return message

def view_teacher_schedule(teacher_id):
    teacher_id = teacher_id.strip()
    message = ""
    rows = db_reader.get_teacher_schedule(teacher_id)
    if not rows:
        message = f"\nNo Classes Found for Teacher Id: {int(teacher_id):04d}"
    else:
        message = f"\n--- SCHEDULE FOR TEACHER {int(teacher_id):04d} ---"
        for row in rows:
            message += f"\nClass Id: {row[0]} | CLass Name: {row[1]} | Class Hour: {row[2]} | Class Room: {row[3]}"
    return message

def view_parent_contact(student_id):
    student_id = student_id.strip()
    parent_id = db_reader.get_parentID_by_student(student_id)
    rows, _ = db_reader.get_by_ID("parents", parent_id)
    if not rows:
        return None, f"\nParent Id: {parent_id:04d} Not Found"
    else:
        row = rows[0]
        message = f"\n--- PARENT CONTACT INFO ---\nParent Name: {row[1]} {row[2]}\nParent Phone Number: {row[3]}\nParent Email: {row[4]}\nParent Address: {row[5]}"
        return row[4], message

def view_appointments_by_date(date):
    date = date.strip()
    message = ""
    rows = db_reader.get_appointments_by_date(date)
    if not rows:
        message = f"\nNo Classes Found for {date}"
    else:
        message = f"\n--- APPOINTMENTS FOR {date} ---"
        for row in rows:
            message += f"\nAppointment Id: {row[0]} | Appointment Hour: {row[1]} | Student Id: {row[2]} | Student Name: {row[3]} {row[4]} | Office Id: {row[5]} | Office Name: {row[6]} | Office Room: {row[7]}"
    return message

def view_appointments_by_student(student_id):
    student_id = student_id.strip()
    message = ""
    rows = db_reader.get_appointments_by_student(student_id)
    if not rows:
        message = f"\nNo Appointments Found for Student Id: {student_id}"
    else:
        message = f"\n--- APPOINTMENT HISTORY FOR STUDENT {student_id} ---"
        for row in rows:
            message += f"\nAppointment Id: {row[0]} | Date: {row[1]} at {row[2]} | Office: {row[4]} (Room: {row[5]})"
    return message

# REGISTER

def register_parent(name, last_name, phone_number, email, address):
    db_writer.register_parent(name, last_name, phone_number, email, address)
    return "\n----- Parent Registered Successfully -----\n"

def register_office(name, room, admin_id):
    db_writer.register_office(name, room, admin_id)
    return "\n----- Office Registered Successfully -----\n"

def register_staff(name, last_name, password, branch, role):
    role = role.lower().strip()
    if role not in {"admin", "teacher"}:
        return "\nRole Not Valid, Could Not Register Staff Member."
    
    staff_id = db_writer.register_user(name, last_name, password, role)
    if staff_id:
        db_writer.register_staff(staff_id, name, last_name, branch)
        return f"\n----- Staff Member Registered Successfully (ID: {staff_id}) -----\n"
    else:
        return "\nCould Not Register Staff Member Due to a User Creation Error."

def register_class(name, teacher_id, hour, room):
    db_writer.register_class(name, teacher_id, hour, room)
    return "\n----- Class Registered Successfully -----\n"

def get_house_id_by_name(house_name):
    return db_reader.get_houseID_by_name(house_name)

def get_parent_id_by_phone(parent_phone):
    return db_reader.get_parentID_by_phone(parent_phone)

def register_student(name, last_name, password, house_id, parent_id):
    student_id = db_writer.register_user(name, last_name, password, "student")
    if student_id:
        db_writer.register_student(student_id, name, last_name, house_id, parent_id)
        return f"\n----- Student Registered Successfully (ID: {student_id}) -----\n"
    return "\nCould Not Register Student Due to a User Creation Error."

def add_class(student_id, class_id):
    student_id = student_id.strip()
    class_id = class_id.strip()
    db_writer.add_class(student_id, class_id)
    return "\nClass Added to Schedule."

def create_appointment(student_id, office_id, date, hour):
    student_id = student_id.strip()
    office_id = office_id.strip()
    date = date.strip()
    hour = hour.strip()
    db_writer.create_appointment(student_id, office_id, date, hour)
    return "\nAppointment Created Successfully."

# GET

def get_parent_data(parent_id):
    parent_id = parent_id.strip()
    rows, _ = db_reader.get_by_ID('parents', parent_id)
    return rows[0] if rows else None

def get_staff_data(staff_id):
    staff_id = staff_id.strip()
    rows, _ = db_reader.get_by_ID('staff', staff_id)
    return rows[0] if rows else None

def get_office_data(office_id):
    office_id = office_id.strip()
    rows, _ = db_reader.get_by_ID('offices', office_id)
    return rows[0] if rows else None

def get_class_data(class_id):
    class_id = class_id.strip()
    rows, _ = db_reader.get_by_ID('classes', class_id)
    return rows[0] if rows else None

def get_student_data(student_id):
    student_id = student_id.strip()
    rows, _ = db_reader.get_by_ID('students', student_id)
    return rows[0] if rows else None

def get_appointment_data(appointment_id):
    appointment_id = appointment_id.strip()
    rows, _ = db_reader.get_by_ID('appointments', appointment_id)
    return rows[0] if rows else None

def get_schedule_classID(student_id, hour):
    return db_reader.get_schedule_classID(student_id, hour)

# UPDATE

def update_parent(parent_id, new_name, new_last_name, new_phone, new_email, new_address):
    parent_id = parent_id.strip()
    current_data = get_parent_data(parent_id)
    
    if current_data:
        final_name = new_name if new_name != "" else current_data[1]
        final_last_name = new_last_name if new_last_name != "" else current_data[2]
        final_phone = new_phone if new_phone != "" else current_data[3]
        final_email = new_email if new_email != "" else current_data[4]
        final_address = new_address if new_address != "" else current_data[5]
        
        db_writer.update_parent(final_name, final_last_name, final_phone, final_email, final_address, parent_id)
        return f"\nParent {parent_id} Updated Successfully."
    return f"\nParent ID {parent_id} Not Found."

def update_staff(staff_id, new_name, new_last_name, new_email, new_branch):
    staff_id = staff_id.strip()
    current_data = get_staff_data(staff_id)
    
    if current_data:
        final_name = new_name if new_name != "" else current_data[1]
        final_last_name = new_last_name if new_last_name != "" else current_data[2]
        final_email = new_email if new_email != "" else current_data[3]
        final_branch = new_branch if new_branch != "" else current_data[4]
        
        db_writer.update_staff(final_name, final_last_name, final_email, final_branch, staff_id)
        return f"\nStaff Member {staff_id} Updated Successfully."
    return f"\nStaff ID {staff_id} Not Found."

def update_office(office_id, new_name, new_room, new_admin_id):
    office_id = office_id.strip()
    current_data = get_office_data(office_id)
    
    if current_data:
        final_name = new_name if new_name != "" else current_data[1]
        final_room = new_room if new_room != "" else current_data[2]
        final_admin_id = new_admin_id if new_admin_id != "" else current_data[3]
        
        db_writer.update_office(final_name, final_room, final_admin_id, office_id)
        return f"\nOffice {office_id} Updated Successfully."
    return f"\nOffice ID {office_id} Not Found."

def update_class(class_id, new_name, new_hour, new_room, new_teacher_id):
    class_id = class_id.strip()
    current_data = get_class_data(class_id)
    
    if current_data:
        final_name = new_name if new_name != "" else current_data[1]
        final_hour = new_hour if new_hour != "" else current_data[2]
        final_room = new_room if new_room != "" else current_data[3]
        final_teacher_id = new_teacher_id if new_teacher_id != "" else current_data[4]
        
        db_writer.update_class(final_name, final_hour, final_room, final_teacher_id, class_id)
        return f"\nClass {class_id} Updated Successfully."
    return f"\nClass ID {class_id} Not Found."

def update_student(student_id, new_name, new_last_name, new_email, new_house_id, new_parent_id):
    student_id = student_id.strip()
    current_data = get_student_data(student_id)
    
    if current_data:
        final_name = new_name if new_name != "" else current_data[1]
        final_last_name = new_last_name if new_last_name != "" else current_data[2]
        final_email = new_email if new_email != "" else current_data[4]
        final_house_id = new_house_id if new_house_id != "" else current_data[5]
        final_parent_id = new_parent_id if new_parent_id != "" else current_data[6]
        
        db_writer.update_student(final_name, final_last_name, final_email, final_house_id, final_parent_id, student_id)
        return f"\nStudent {student_id} Updated Successfully."
    return f"\nStudent ID {student_id} Not Found."

def update_schedule(new_class_id, student_id, class_id):
    db_writer.update_schedule(new_class_id, student_id, class_id)
    return "\nSchedule Updated Successfully."

def update_appointment(appointment_id, new_date, new_hour):
    appointment_id = appointment_id.strip()
    current_data = get_appointment_data(appointment_id)
    
    if current_data:
        final_date = new_date if new_date != "" else current_data[3]
        final_hour = new_hour if new_hour != "" else current_data[4]
        
        db_writer.update_appointment(final_date, final_hour, appointment_id)
        return f"\nAppointment {appointment_id} Updated Successfully."
    return f"\nAppointment ID {appointment_id} Not Found."

# DELETE

def delete_office(office_id):
    office_id = office_id.strip()
    db_writer.delete_office(office_id)
    return f"\nOffice {office_id} Deleted successfully."

def delete_staff(staff_id):
    staff_id = staff_id.strip()
    db_writer.delete_staff(staff_id)
    return f"\nStaff Member {staff_id} Deleted successfully."

def delete_class(class_id):
    class_id = class_id.strip()
    db_writer.delete_class(class_id)
    return f"\nClass {class_id} Deleted successfully."

def get_parentID_by_student(student_id):
    return db_reader.get_parentID_by_student(student_id)

def get_students_by_parent(parent_id):
    return db_reader.get_students_by_parent(parent_id)

def delete_student(student_id):
    db_writer.delete_student(student_id)
    return f"\nStudent {student_id} Deleted successfully."

def delete_parent(parent_id):
    db_writer.delete_parent(parent_id)
    return f"\nParent {parent_id} Deleted successfully."

def drop_class(student_id, class_id):
    db_writer.drop_class(student_id, class_id)
    return f"\nClass dropped successfully."

def cancel_appointment(appointment_id):
    appointment_id = appointment_id.strip()
    db_writer.cancel_appointment(appointment_id)
    return f"\nAppointment {appointment_id} Cancelled successfully."

# MORE

def send_email(class_id):
    class_id = class_id.strip()
    message = ""
    rows = db_reader.get_emails_in_class(class_id)
    if not rows:
        message = f"\nNo Emails Found in Class Id: {int(class_id):04d}"
    else:
        for row in rows:
            message += f"\nEmail Sent to {row[0]}"
    return message