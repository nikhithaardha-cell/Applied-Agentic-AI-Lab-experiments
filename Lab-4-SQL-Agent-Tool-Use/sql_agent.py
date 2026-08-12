import sqlite3

DATABASE = "college.db"


# ==========================================
# TOOL 1: LIST DATABASE TABLES
# ==========================================
def list_tables():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    tables = [row[0] for row in cursor.fetchall()]

    connection.close()

    return tables


# ==========================================
# TOOL 2: DESCRIBE STUDENTS TABLE
# ==========================================
def describe_students():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("PRAGMA table_info(students)")

    columns = cursor.fetchall()

    connection.close()

    return columns


# ==========================================
# TOOL 3: EXECUTE SQL QUERY
# ==========================================
def execute_sql(query):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        connection.close()

        return results

    except sqlite3.Error as error:
        connection.close()

        return "SQL Error: " + str(error)


# ==========================================
# CREATE DATABASE AND STUDENT TABLE
# ==========================================
def create_database():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            marks INTEGER
        )
    """)

    # Check whether students already exist
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    # Insert sample data only once
    if count == 0:

        students = [
            (1, "Nikhitha", "Cyber Security", 88),
            (2, "Sanjana", "Computer Science", 92),
            (3, "Hemanth", "Cyber Security", 85),
            (4, "Rahul", "Artificial Intelligence", 90),
            (5, "Priya", "Computer Science", 78)
        ]

        cursor.executemany("""
            INSERT INTO students
            (id, name, department, marks)
            VALUES (?, ?, ?, ?)
        """, students)

    connection.commit()
    connection.close()


# ==========================================
# REACT SQL AGENT
# ==========================================
def sql_agent(question):

    question_lower = question.lower().strip()

    print("\n===================================")
    print("        REACT SQL AGENT")
    print("===================================")

    # --------------------------------------
    # THOUGHT 1
    # --------------------------------------
    print("\nTHOUGHT:")
    print("I need to understand the question and identify the required database tool.")

    # --------------------------------------
    # ACTION 1
    # --------------------------------------
    print("\nACTION:")
    print("list_tables()")

    tables = list_tables()

    # --------------------------------------
    # OBSERVATION 1
    # --------------------------------------
    print("\nOBSERVATION:")
    print("Available tables:", tables)

    if "students" not in tables:
        print("\nFINAL ANSWER:")
        print("The students table is not available.")
        return

    # --------------------------------------
    # THOUGHT 2
    # --------------------------------------
    print("\nTHOUGHT:")
    print("I need to inspect the students table before executing the query.")

    # --------------------------------------
    # ACTION 2
    # --------------------------------------
    print("\nACTION:")
    print("describe_students()")

    columns = describe_students()

    # --------------------------------------
    # OBSERVATION 2
    # --------------------------------------
    print("\nOBSERVATION:")
    print("Students table columns:")

    for column in columns:
        print(
            " -",
            column[1],
            "(" + column[2] + ")"
        )

    # ======================================
    # SELECT SQL QUERY
    # ======================================

    query = None

    # Show all students
    if (
        "all students" in question_lower
        or "show students" in question_lower
        or "list students" in question_lower
    ):
        query = "SELECT * FROM students;"

    # Show student names
    elif (
        "student names" in question_lower
        or "names of students" in question_lower
        or question_lower == "names"
    ):
        query = "SELECT name FROM students;"

    # Cyber Security students
    elif "cyber security" in question_lower:
        query = """
        SELECT *
        FROM students
        WHERE department = 'Cyber Security';
        """

    # Computer Science students
    elif "computer science" in question_lower:
        query = """
        SELECT *
        FROM students
        WHERE department = 'Computer Science';
        """

    # Highest marks
    elif (
        "highest" in question_lower
        or "top student" in question_lower
        or "highest marks" in question_lower
    ):
        query = """
        SELECT *
        FROM students
        ORDER BY marks DESC
        LIMIT 1;
        """

    # Average marks
    elif "average" in question_lower:
        query = """
        SELECT AVG(marks)
        FROM students;
        """

    # Count students
    elif (
        "how many students" in question_lower
        or "count students" in question_lower
    ):
        query = """
        SELECT COUNT(*)
        FROM students;
        """

    # Minimum marks
    elif "lowest marks" in question_lower:
        query = """
        SELECT *
        FROM students
        ORDER BY marks ASC
        LIMIT 1;
        """

    # --------------------------------------
    # Unsupported question
    # --------------------------------------
    if query is None:

        print("\nTHOUGHT:")
        print("I could not identify a suitable SQL operation.")

        print("\nFINAL ANSWER:")
        print(
            "Sorry, I can currently answer questions about "
            "students, departments, names, marks, and averages."
        )

        return

    # --------------------------------------
    # ACTION 3
    # --------------------------------------
    print("\nACTION:")
    print("execute_sql()")

    print("\nSQL QUERY:")
    print(query.strip())

    # --------------------------------------
    # OBSERVATION 3
    # --------------------------------------
    results = execute_sql(query)

    print("\nOBSERVATION:")

    if isinstance(results, str):
        print(results)
        return

    if len(results) == 0:
        print("No matching records found.")

    else:
        for row in results:
            print(row)

    # --------------------------------------
    # FINAL ANSWER
    # --------------------------------------
    print("\nFINAL ANSWER:")

    if len(results) == 0:
        print("No matching student records were found.")

    elif "average" in question_lower:
        print("The average marks are:", results[0][0])

    elif "highest" in question_lower or "top student" in question_lower:
        print(
            "The student with the highest marks is:",
            results[0]
        )

    elif "lowest" in question_lower:
        print(
            "The student with the lowest marks is:",
            results[0]
        )

    elif (
        "how many students" in question_lower
        or "count students" in question_lower
    ):
        print(
            "The total number of students is:",
            results[0][0]
        )

    else:
        print("The requested database information is displayed above.")


# ==========================================
# MAIN PROGRAM
# ==========================================
if __name__ == "__main__":

    # Create database automatically
    create_database()

    print("===================================")
    print(" SQL AGENT WITH TOOL USE")
    print(" ReAct-Based Database Agent")
    print("===================================")

    print("\nAvailable database tools:")
    print("1. list_tables()")
    print("2. describe_students()")
    print("3. execute_sql()")

    question = input("\nEnter your question: ")

    sql_agent(question)