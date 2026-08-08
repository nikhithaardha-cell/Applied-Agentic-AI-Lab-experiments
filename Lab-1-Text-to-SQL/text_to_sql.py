import sqlite3

# -------------------------------
# STEP 1: Create Database
# -------------------------------

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# -------------------------------
# STEP 2: Create Students Table
# -------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT,
    marks INTEGER
)
""")

# -------------------------------
# STEP 3: Insert Sample Data
# -------------------------------

cursor.execute("DELETE FROM students")

students = [
    (1, "Nikhitha", "CSE", 85),
    (2, "Sanjana", "CSE", 72),
    (3, "Hemanth", "CSE", 91),
    (4, "Rahul", "ECE", 68),
    (5, "Priya", "CSE", 88)
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    students
)

connection.commit()


# -------------------------------
# STEP 4: Text-to-SQL Function
# -------------------------------

def text_to_sql(question):

    question = question.lower()

    if "marks greater than 80" in question:
        return "SELECT * FROM students WHERE marks > 80"

    elif "all students" in question:
        return "SELECT * FROM students"

    elif "cse students" in question:
        return "SELECT * FROM students WHERE branch = 'CSE'"

    elif "marks less than 80" in question:
        return "SELECT * FROM students WHERE marks < 80"

    else:
        return None


# -------------------------------
# STEP 5: Get User Question
# -------------------------------

question = input("Enter your question: ")

# Convert question into SQL
sql_query = text_to_sql(question)


# -------------------------------
# STEP 6: Execute SQL
# -------------------------------

if sql_query:

    print("\nGenerated SQL:")
    print(sql_query)

    cursor.execute(sql_query)

    results = cursor.fetchall()

    print("\nResult:")

    for row in results:
        print(row)

else:
    print("\nSorry, I could not generate an SQL query.")


# Close database
connection.close()