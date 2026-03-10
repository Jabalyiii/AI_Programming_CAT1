import os

# A list to store all student records
all_students = []
# Define the filename for saving data
FILE_NAME = "students.txt"

def save_to_file():
    """
    Writes the current list of all students to a text file named students.txt.
    """
    try:
        with open(FILE_NAME, 'w') as f:
            # Write a header
            f.write(f"--- Student Information System Data ({len(all_students)} records) ---\n\n")
            for student in all_students:
                # Format each student record for readability in the text file
                f.write(f"Name: {student['name']}, ID: {student['student_id']}, Favorite AI Tool: {student['favorite_ai_tool']}\n")
        print(f"\n[SUCCESS] Successfully saved {len(all_students)} student records to '{FILE_NAME}'.")
    except IOError as e:
        print(f"\n[ERROR] Could not write to file {FILE_NAME}: {e}")

def add_student():
    """
    Prompts the user for student details, stores them in a dictionary,
    and appends the dictionary to the all_students list.
    """
    print("\n--- Enter Student Details ---")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    favorite_ai_tool = input("Enter favorite AI tool: ")

    # Create the student dictionary
    student_data = {
        "name": name,
        "student_id": student_id,
        "favorite_ai_tool": favorite_ai_tool
    }

    # Append to the list
    all_students.append(student_data)
    print(f"\n[INFO] Added student: {name}")

def display_students():
    """
    Prints the total number of students and their details neatly formatted.
    """
    print("\n--- Current Student Records ---")
    if not all_students:
        print("No students enrolled yet.")
    else:
        print(f"Total number of students: {len(all_students)}")
        for index, student in enumerate(all_students):
            print(f"\nRecord {index + 1}:")
            print(f"  Name: {student['name']}")
            print(f"  ID: {student['student_id']}")
            print(f"  Favorite AI Tool: {student['favorite_ai_tool']}")
    print("---------------------------------")

def main_menu():
    """
    Main loop to interact with the system.
    """
    while True:
        print("\n===== Student Information System Menu =====")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Save data to file")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            save_to_file()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("[WARNING] Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # Ensure previous students.txt is cleared/handled if necessary for a clean run
    if os.path.exists(FILE_NAME):
        print(f"Found existing '{FILE_NAME}'. New data will overwrite it when saved.")
    main_menu()
