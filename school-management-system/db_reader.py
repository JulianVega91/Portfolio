import sqlite3

def log_in(username, password):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT user_ID, role
            FROM users
            WHERE username = ? AND password = ?
        ''', (username, password))
        return cursor.fetchone()
    except sqlite3.Error:
        return None
    finally:
        conn.close()

def get_table(table):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    try:
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        return []
    finally:
        conn.close()

def get_by_ID(table, ID):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    try:
        id_map = {
            "students": "student_ID",
            "parents": "parent_ID",
            "staff": "staff_ID",
            "classes": "class_ID",
            "offices": "office_ID",
            "appointments": "appointment_ID"
        }
        id_number = id_map[table]
        query = f"SELECT * FROM {table} WHERE {id_number} = ?"
        cursor.execute(query, (ID,))
        
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description] if rows else []
        return rows, columns
    except sqlite3.Error:
        return [], []
    finally:
        conn.close()

def get_student_schedule(ID):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT classes.name, classes.hour, classes.room
            FROM schedules
            JOIN classes ON schedules.class_ID = classes.class_ID
            WHERE schedules.student_ID = ?
            ORDER BY classes.hour
        ''', (ID,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        return []
    finally:
        conn.close()

def get_schedule_classID(student_id, hour):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT schedules.class_ID 
            FROM schedules
            JOIN classes ON schedules.class_ID = classes.class_ID
            WHERE schedules.student_ID = ? AND classes.hour = ?
        ''', (student_id, hour))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

def get_parentID_by_phone(phone_number):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT parent_ID
            FROM parents
            WHERE number = ?
        ''', (phone_number,))
        row = cursor.fetchone()
        return row[0] if row else None
    except sqlite3.Error:
        return None
    finally:
        conn.close()

def get_students_by_parent(parent_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT COUNT(*) FROM students WHERE parent_ID = ?', (parent_id,))
        result = cursor.fetchone()
        return result[0] if result else 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0
    finally:
        conn.close()

def get_parentID_by_student(student_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT parent_ID FROM students WHERE student_ID = ?', (student_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

def get_officeID_by_name(office_name):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT office_ID
            FROM offices
            WHERE name = ?
        ''', (office_name,))
        row = cursor.fetchone()
        return row[0] if row else None
    except sqlite3.Error:
        return None
    finally:
        conn.close()

def get_officeID_by_name(office_name):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT office_ID
            FROM offices
            WHERE name = ?
        ''', (office_name,))
        row = cursor.fetchone()
        return row[0] if row else None
    except sqlite3.Error:
        return None
    finally:
        conn.close()

def get_class_roster(class_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT students.student_ID, students.name, students.last_name
            FROM schedules
            JOIN students ON schedules.student_ID = students.student_ID
            WHERE schedules.class_ID = ?
        ''', (class_id,))
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()

def get_class_catalog():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT classes.*, staff.name, staff.last_name
            FROM classes
            JOIN staff ON classes.teacher_ID = staff.staff_ID 
        ''')
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()

def get_student_appointments(student_ID):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT appointments.*, offices.name, offices.room
            FROM appointments
            JOIN offices ON appointments.office_ID = offices.office_ID
            WHERE student_ID = ?
        ''', (student_ID,))
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()

def get_teacher_schedule(teacher_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT *
            FROM classes
            WHERE teacher_ID = ?
            ORDER BY hour
        ''', (teacher_id,))
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()

def get_emails_in_class(class_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT users.email
            FROM schedules
            JOIN students ON schedules.student_ID = students.student_ID
            JOIN users ON students.student_ID = users.user_ID
            WHERE class_ID = ?
        ''', (class_id,))
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()

def get_appointments_by_date(date):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT
                appointments.appointment_ID, appointments.hour, 
                students.student_ID, students.name, students.last_name,
                offices.office_ID, offices.name, offices.room
            FROM appointments
            JOIN students ON appointments.student_ID = students.student_ID
            JOIN offices ON appointments.office_ID = offices.office_ID
            WHERE appointments.date = ?
            ORDER BY appointments.hour
        ''', (date,))
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()

def get_appointments_by_student(student_id):
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT
                appointments.appointment_ID, appointments.date, appointments.hour,
                offices.office_ID, offices.name, offices.room
            FROM appointments
            JOIN offices ON appointments.office_ID = offices.office_ID
            WHERE appointments.student_ID = ?
            ORDER BY appointments.date, appointments.hour
        ''', (student_id,))
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()

def get_students_without_classes():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT students.student_ID, students.name, students.last_name
            FROM students
            LEFT JOIN schedules ON students.student_ID = schedules.student_ID
            WHERE schedules.student_ID IS NULL
            ORDER BY students.last_name, students.name
        ''', ())
        return cursor.fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()