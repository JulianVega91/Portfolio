import sqlite3

def create_database():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')
    
    # TABLE users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL CHECK(role IN ('admin', 'teacher', 'student'))
        )
    ''')

    # TABLE parents
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS parents (
            parent_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL,
            UNIQUE(name, last_name)
        )
    ''')
    
    # TABLE staff
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS staff (
            staff_ID INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            branch TEXT,
            FOREIGN KEY (staff_ID) REFERENCES users(user_ID) ON DELETE CASCADE
        )
    ''')
    
    # TABLE offices
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS offices (
            office_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            room TEXT NOT NULL UNIQUE,
            admin_ID INTEGER NOT NULL UNIQUE,
            FOREIGN KEY (admin_ID) REFERENCES staff(staff_ID)
        )
    ''')
    
    # TABLE classes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            class_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hour TEXT NOT NULL,
            room TEXT NOT NULL UNIQUE,
            teacher_ID INTEGER NOT NULL,
            FOREIGN KEY (teacher_ID) REFERENCES staff(staff_ID)
        )
    ''')
    
    # TABLE students
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_ID INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            house_ID INTEGER,
            parent_ID INTEGER,
            FOREIGN KEY (student_ID) REFERENCES users(user_ID) ON DELETE CASCADE,
            FOREIGN KEY (house_ID) REFERENCES offices(office_ID),
            FOREIGN KEY (parent_ID) REFERENCES parents(parent_ID)
        )
    ''')
    
    # TABLE schedules
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedules (
            student_ID INTEGER NOT NULL,
            class_ID INTEGER NOT NULL,
            PRIMARY KEY (student_ID, class_ID),
            FOREIGN KEY (student_ID) REFERENCES students(student_ID),
            FOREIGN KEY (class_ID) REFERENCES classes(class_ID)
        )
    ''')
    
    # TABLE appointments
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            student_ID INTEGER NOT NULL,
            office_ID INTEGER NOT NULL,
            date DATE NOT NULL,
            hour TEXT NOT NULL,
            FOREIGN KEY (student_ID) REFERENCES students(student_ID),
            FOREIGN KEY (office_ID) REFERENCES offices(office_ID),
            CHECK (strftime('%Y-%m-%d', date) IS NOT NULL)
        )
    ''')
    
    conn.commit()
    conn.close()

def erase_database():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    
    cursor.execute('PRAGMA foreign_keys = OFF;')
    cursor.execute('DROP TABLE IF EXISTS appointments;')
    cursor.execute('DROP TABLE IF EXISTS schedules;')
    cursor.execute('DROP TABLE IF EXISTS students;')
    cursor.execute('DROP TABLE IF EXISTS classes;')
    cursor.execute('DROP TABLE IF EXISTS offices;')
    cursor.execute('DROP TABLE IF EXISTS staff;')
    cursor.execute('DROP TABLE IF EXISTS parents;')
    cursor.execute('DROP TABLE IF EXISTS users;')
    
    conn.commit()
    conn.close()

def seed_database():
    conn = sqlite3.connect('college.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')
    
    try:
        # ==== TABLE users - admins & teachers ====
        cursor.executemany('INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)', [
            ('jamescarter', 'pass1', 'james.carter@staff.college.edu', 'admin'),
            ('lindafoster', 'pass2', 'linda.foster@staff.college.edu', 'admin'),
            ('williamvance', 'pass3', 'william.vance@staff.college.edu', 'admin'),
            ('barbarahardy', 'pass4', 'barbara.hardy@staff.college.edu', 'admin'),
            ('susanreynolds', 'pass5', 'susan.reynolds@staff.college.edu', 'admin'),
            ('dennismccall', 'pass6', 'dennis.mccall@staff.college.edu', 'admin'),
            ('johnsmith', 'math456', 'john.smith@staff.college.edu', 'teacher'), 
            ('emilydavis', 'pass8', 'emily.davis@staff.college.edu', 'teacher'),
            ('jessicataylor', 'pass9', 'jessica.taylor@staff.college.edu', 'teacher'),
            ('robertmiller', 'pass10', 'robert.miller@staff.college.edu', 'teacher'),
            ('davidclark', 'pass11', 'david.clark@staff.college.edu', 'teacher'),
            ('karenwhite', 'pass12', 'karen.white@staff.college.edu', 'teacher'),
            ('thomasmiller', 'pass13', 'thomas.miller@staff.college.edu', 'admin'),
            ('georgeharris', 'pass14', 'george.harris@staff.college.edu', 'admin')
        ])

        # ==== TABLE users - students ====
        cursor.executemany('INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)', [
            ('chrisbrown', 'student789', 'chris.brown@student.college.edu', 'student'), 
            ('emmabrown', 'pass16', 'emma.brown@student.college.edu', 'student'),
            ('matthewjenkins', 'pass17', 'matthew.jenkins@student.college.edu', 'student'),
            ('ashleyjenkins', 'pass18', 'ashley.jenkins@student.college.edu', 'student'),
            ('oliviawilson', 'pass19', 'olivia.wilson@student.college.edu', 'student'),
            ('danieladams', 'pass20', 'daniel.adams@student.college.edu', 'student'),
            ('sophiaadams', 'pass21', 'sophia.adams@student.college.edu', 'student')
        ])

        # ==== TABLE staff ====
        cursor.executemany('''
            INSERT INTO staff (staff_ID, name, last_name, branch) VALUES (?, ?, ?, ?)
        ''', [
            (1, 'James', 'Carter', 'Administration'),
            (2, 'Linda', 'Foster', 'Administration'),
            (3, 'William', 'Vance', 'Administration'),
            (4, 'Barbara', 'Hardy', 'Administration'),
            (5, 'Susan', 'Reynolds', 'Administration'),  
            (6, 'Dennis', 'McCall', 'Administration'),    
            (7, 'John', 'Smith', 'Mathematics'),
            (8, 'Emily', 'Davis', 'Chemistry'),
            (9, 'Jessica', 'Taylor', 'History'),
            (10, 'Robert', 'Miller', 'English'),
            (11, 'David', 'Clark', 'Arts'),
            (12, 'Karen', 'White', 'Biology'),
            (13, 'Thomas', 'Miller', 'Maintenance'),
            (14, 'George', 'Harris', 'Maintenance'),
            (22, 'Julian', 'V', 'Administration')
        ])
        
        # ==== TABLE offices ====
        cursor.executemany('''
            INSERT INTO offices (name, room, admin_ID) VALUES (?, ?, ?)
        ''', [
            ('Bears House', 'A001', 1),   
            ('Wolves House', 'B001', 2),  
            ('Eagles House', 'C001', 3),  
            ('Hawks House', 'D001', 4),
            ('Bursar Office', 'E010', 5),         
            ('Student Work Office', 'E012', 6),   
            ('Drama Club', 'C110', 10),            
            ('Art Club', 'C112', 11)              
        ])
        
        # ==== TABLE classes ====
        cursor.executemany('''
            INSERT INTO classes (name, hour, room, teacher_ID) VALUES (?, ?, ?, ?)
        ''', [
            ('Algebra I', '08:00', 'A204', 7),         
            ('Calculus AB', '09:30', 'A206', 7),
            ('General Chemistry', '09:30', 'B315', 8), 
            ('Organic Chemistry', '13:00', 'B317', 8),
            ('AP US History', '11:00', 'D102', 9),      
            ('Creative Writing', '14:00', 'D105', 10),
            ('Introduction to Biology', '08:00', 'B201', 12)
        ])
        
        # ==== TABLE parents ====
        cursor.executemany('''
            INSERT INTO parents (name, last_name, phone_number, email, address) 
            VALUES (?, ?, ?, ?, ?)
        ''', [
            ('Michael', 'Brown', '203-555-0144', 'michael.brown@gmail.com', '542 Elm Street'),
            ('Sarah', 'Jenkins', '203-555-0188', 's.jenkins@yahoo.com', '12 Maple Avenue'),
            ('David', 'Wilson', '203-555-0233', 'david.wilson@outlook.com', '89 Oak Road'),
            ('Nancy', 'Adams', '203-555-0377', 'nancy.adams@gmail.com', '104 Cedar Lane')
        ])
        
        # ==== TABLE students ====
        cursor.executemany('''
            INSERT INTO students (student_ID, name, last_name, house_ID, parent_ID) 
            VALUES (?, ?, ?, ?, ?)
        ''', [
            (15, 'Chris', 'Brown', 1, 1),      
            (16, 'Emma', 'Brown', 3, 1),       
            (17, 'Matthew', 'Jenkins', 2, 2), 
            (18, 'Ashley', 'Jenkins', 2, 2),  
            (19, 'Olivia', 'Wilson', 4, 3),     
            (20, 'Daniel', 'Adams', 1, 4),      
            (21, 'Sophia', 'Adams', 4, 4)       
        ])
        
        # ==== TABLE schedules ====
        cursor.executemany('''
            INSERT INTO schedules (student_ID, class_ID) VALUES (?, ?)
        ''', [
            (15, 1), (15, 5),          
            (16, 3), (16, 7),          
            (17, 1), (17, 3), (17, 6),  
            (18, 2), (18, 4),          
            (19, 5),                    
            (20, 1), (20, 7),          
            (21, 5), (21, 6)           
        ])
        
        conn.commit()
        print("Seed phase complete: Campus database populated natively con nombres de usuario corregidos.")
    except sqlite3.Error as e:
        print(f"Database execution error during seeding: {e}")
    finally:
        conn.close()
