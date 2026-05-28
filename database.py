# import sqlite3Adimport sqlite3
import sqlite3
conn = sqlite3.connect("health.db")

cursor = conn.cursor()

# Patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    age INTEGER,

    gender TEXT
)
""")

# History table
cursor.execute("""
CREATE TABLE IF NOT EXISTS history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_name TEXT,

    disease TEXT
)
""")

conn.commit()

# Add patient
def add_patient(name, age, gender):

    cursor.execute("""

    INSERT INTO patients(name, age, gender)

    VALUES (?, ?, ?)

    """, (name, age, gender))

    conn.commit()

    print("\nPatient added successfully.")

# View patients
def view_patients():

    cursor.execute("SELECT * FROM patients")

    data = cursor.fetchall()

    print("\n===== PATIENT RECORDS =====")

    for row in data:

        print(row)

# Save disease history
def save_history(name, disease):

    cursor.execute("""

    INSERT INTO history(patient_name, disease)

    VALUES (?, ?)

    """, (name, disease))

    conn.commit()

# View history
def view_history():

    cursor.execute("SELECT * FROM history")

    data = cursor.fetchall()

    print("\n===== PATIENT HISTORY =====")

    for row in data:

        print(row)
