# School Management System

A robust and intuitive Python-based command-line application designed to manage school operations, student enrollment, and academic records. This project utilizes a relational database to ensure efficient data persistence and structured information management.

## Features
* **Student & Teacher Management:** Easily register, update, and manage student and staff profiles.
* **Course Enrollment:** Organize classes, assign teachers, and enroll students in courses.
* **Database Integration:** Powered by an SQLite database for seamless data handling and local storage.

## Technologies Used
* **Language:** Python 3
* **Database:** SQLite3
* **Libraries:** Standard Python libraries for database connection and terminal interaction.

## File Structure
* `school-management-system/`
  * `college.db` - The local SQLite database.
  * `main.py` - The primary entry point of the Python application.
  * `controller.py` - Manages the application logic and connects the interface with database actions.
  * `db_reader.py` - Handles database queries and read operations.
  * `db_writer.py` - Handles database insertions, updates, and write operations.
  * `README.md` - Project documentation.

## How to Run the Application
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Run the main file from your terminal: `python main.py`
4. You can use the restart option within the application to clear the database, allowing you to wipe the existing records and insert your own custom data.
5. Feel free to explore through the menus and options.
