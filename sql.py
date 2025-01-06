import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# Create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

# Insert initial data
cursor.execute('''Insert Into STUDENT values('Krish', 'Data Science', 'A', 90)''')

# Insert more sample data
sample_data = [
    ('Ananya', 'Data Science', 'B', 85),
    ('Rohan', 'Computer Science', 'A', 92),
    ('Priya', 'Mathematics', 'C', 18),
    ('Vikram', 'Physics', 'B', 68),
    ('Neha', 'Chemistry', 'C', 91),
    ('Amit', 'Biology', 'A', 35),
    ('Sakshi', 'Economics', 'B', 89),
    ('Arjun', 'History', 'A', 46),
    ('Diya', 'Geography', 'C', 82),
    ('Ravi', 'Literature', 'B', 24)
]

# Inserting the sample data into the table
for student in sample_data:
    cursor.execute('''Insert Into STUDENT values(?,?,?,?)''', student)

# Commit the changes
connection.commit()

# Verify the data insertion
rows = cursor.execute('''Select * from STUDENT''')

for row in rows:
    print(row)

# Close the connection
connection.close()
