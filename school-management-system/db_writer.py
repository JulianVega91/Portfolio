import sqlite3

def register_user(username, password, email, role):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO users (username, password, email, role)
            VALUES (?, ?, ?, ?)
        ''', (username, password, email, role))
        conn.commit()
        assigned_id = cursor.lastrowid
        print(f"User {username} registered. Assigned ID: {cursor.lastrowid:04d}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()
    return assigned_id

def register_parent(name, last_name, phone_number, email, address):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO parents (name, last_name, phone_number, email, address)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, last_name, phone_number, email, address))
        conn.commit()
        print(f"Parent {name} {last_name} registered. Assigned ID: {cursor.lastrowid:04d}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def register_staff(staff_id, name, last_name, branch):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO staff (staff_ID, name, last_name, branch)
            VALUES (?, ?, ?, ?)
        ''', (staff_id, name, last_name, branch))
        conn.commit()
        print(f"staff member {name} registered. Assigned ID: {cursor.lastrowid:04d}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def register_office(name, room, admin_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO offices (name, room, admin_id)
            VALUES (?, ?, ?)
        ''', (name, room, admin_id))
        conn.commit()
        print(f"Office {name} created. Assigned ID: {cursor.lastrowid:04d}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def register_class(name, hour, room, teacher_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO classes (name, hour, room, teacher_id)
            VALUES (?, ?, ?, ?)
        ''', (name, hour, room, teacher_id))
        conn.commit()
        print(f"Class {name} registered. Assigned ID: {cursor.lastrowid:04d}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def register_student(student_id, name, last_name, house_id, parent_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO students (student_ID, name, last_name, house_ID, parent_ID)
            VALUES (?, ?, ?, ?, ?)
        ''', (student_id, name, last_name, house_id, parent_id))
        conn.commit()
        print(f"Student {name} registered. Assigned ID: {cursor.lastrowid:04d}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def add_class(student_id, class_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO schedules (student_ID, class_ID)
            VALUES (?, ?)
        ''', (student_id, class_id))
        conn.commit()
        print(f"Class {class_id} registered to student {student_id}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def create_appointment(student_id, office_id, date, hour):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            INSERT INTO appointments (student_ID, office_ID, date, hour)
            VALUES (?, ?, ?, ?)
        ''', (student_id, office_id, date, hour))
        conn.commit()
        print(f"Student {student_id} registered an appointment for {date} at {hour}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_class(name, hour, room, teacher_id, class_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            UPDATE classes
            SET name = ?, hour = ?, room = ?, teacher_ID = ?
            WHERE class_ID = ?
        ''', (name, hour, room, teacher_id, class_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Class ID {class_id} updated.")
        else:
            print("Class not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_office(name, room, admin_id, office_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            UPDATE offices
            SET name = ?, room = ?, admin_ID = ?
            WHERE office_ID = ?
        ''', (name, room, admin_id, office_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Office ID {office_id} updated.")
        else:
            print("Office not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_staff(name, last_name, email, branch, staff_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            UPDATE staff
            SET name = ?, last_name = ?, email = ?, branch = ?
            WHERE staff_ID = ?
        ''', (name, last_name, email, branch, staff_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Staff ID {staff_id} updated.")
        else:
            print("Staff member not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_student(name, last_name, email, house_id, parent_id, student_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            UPDATE students
            SET name = ?, last_name = ?, email = ?, house_ID = ?, parent_ID = ?
            WHERE student_ID = ?
        ''', (name, last_name, email, house_id, parent_id, student_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Student ID {student_id} updated.")
        else:
            print("Student not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_parent(name, last_name, phone_number, email, address, parent_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            UPDATE parents
            SET name = ?, last_name = ?, phone_number = ?, email = ?, address = ?
            WHERE parent_ID = ?
        ''', (name, last_name, phone_number, email, address, parent_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Parent ID {parent_id} updated.")
        else:
            print("Parent not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_schedule(new_class_id, student_id, class_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            UPDATE schedules
            SET class_ID = ?
            WHERE student_ID = ? AND class_ID = ?
        ''', (new_class_id, student_id, class_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Schedule updated for student {student_id}.")
        else:
            print("Class not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def update_appointment(date, hour, appointment_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            UPDATE appointments
            SET date = ?, hour = ?
            WHERE appointment_ID = ?
        ''', (date, hour, appointment_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Appointment {appointment_id} updated for {date} at {hour}.")
        else:
            print("Appointment not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def delete_parent(parent_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('UPDATE students SET parent_ID = NULL WHERE parent_ID = ?', (parent_id,))
        cursor.execute('DELETE FROM parents WHERE parent_ID = ?', (parent_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"parent ID {parent_id} deleted.")
        else:
            print("Parent not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def delete_class(class_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('DELETE FROM classes WHERE class_ID = ?', (class_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Class ID {class_id} deleted.")
        else:
            print("Class not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def delete_office(office_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('DELETE FROM appointments WHERE office_ID = ?', (office_id,))
        cursor.execute('DELETE FROM offices WHERE office_ID = ?', (office_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Office ID {office_id} deleted.")
        else:
            print("Office not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def delete_staff(staff_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('UPDATE offices SET admin_ID = NULL WHERE admin_ID = ?', (staff_id,))
        cursor.execute('UPDATE classes SET teacher_ID = NULL WHERE teacher_ID = ?', (staff_id,))
        cursor.execute('DELETE FROM staff WHERE staff_ID = ?', (staff_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Staff ID {staff_id} deleted.")
        else:
            print("Staff member not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def delete_student(student_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('DELETE FROM schedules WHERE student_ID = ?', (student_id,))
        cursor.execute('DELETE FROM appointments WHERE student_ID = ?', (student_id,))
        cursor.execute('DELETE FROM students WHERE student_ID = ?', (student_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Student ID {student_id} deleted.")
        else:
            print("Student not found.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def drop_class(student_id, class_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            DELETE FROM schedules 
            WHERE student_ID = ? AND class_ID = ?
        ''', (student_id, class_id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Student {student_id} removed from class {class_id}.")
        else:
            print("Registration not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def cancel_appointment(appointment_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('PRAGMA foreign_keys = ON;')
        cursor.execute('''
            DELETE FROM appointments
            WHERE appointment_ID = ?
        ''', (appointment_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Appointment {appointment_id} removed.")
        else:
            print("Registration not found.")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()