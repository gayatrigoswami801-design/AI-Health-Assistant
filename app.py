from utils import show_title

from model import predict_disease

from database import (
    add_patient,
    view_patients,
    save_history,
    view_history
)

from reminder import show_reminder

from report import generate_report

from emergency import emergency_check

from chatbot import chatbot

while True:

    show_title()

    print("\n1. Add Patient")
    print("2. View Patients")
    print("3. Predict Disease")
    print("4. Patient History")
    print("5. Medicine Reminder")
    print("6. Generate Report")
    print("7. Emergency Check")
    print("8. AI Chatbot")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    # Add Patient
    if choice == "1":

        name = input("\nEnter patient name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")

        add_patient(name, age, gender)

    # View Patients
    elif choice == "2":

        view_patients()

    # Predict Disease
    elif choice == "3":

        name = input("\nEnter patient name: ")

        fever = int(input("Fever? (1=yes,0=no): "))
        cough = int(input("Cough? (1=yes,0=no): "))
        headache = int(input("Headache? (1=yes,0=no): "))

        disease = predict_disease(
            [fever, cough, headache]
        )

        print("\nPredicted Disease:", disease)

        save_history(name, disease)

    # Patient History
    elif choice == "4":

        view_history()

    # Reminder
    elif choice == "5":

        show_reminder()

    # Report
    elif choice == "6":

        name = input("\nEnter patient name: ")
        disease = input("Enter disease: ")

        generate_report(name, disease)

    # Emergency
    elif choice == "7":

        disease = input("\nEnter disease: ")

        emergency_check(disease)

    # Chatbot
    elif choice == "8":

        chatbot()

    # Exit
    elif choice == "9":

        print("\nExiting program...")
        break

    else:

        print("\nInvalid choice.")