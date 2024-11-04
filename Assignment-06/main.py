def manage_student_database():
    # List to store student tuples, each tuple will contain (ID, Name)
    student_list = []
    # Set to keep track of names for duplicate checking
    student_names = set()
    # Counter to assign sequential IDs
    student_id = 1

    # Start collecting student names
    while True:
        # Prompt the user for a student's name
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()

        # If the user types 'stop', end the input process
        if name.lower() == 'stop':
            break

        # Check if the student's name is already in the list to prevent duplicates
        if name in student_names:
            print("This name is already in the list.")
        else:
            # Add the student's name to the set of names
            student_names.add(name)
            # Add the student's ID and name as a tuple in the list
            student_list.append((student_id, name))
            # Increment the ID for the next student
            student_id += 1

    # Display the complete list of student tuples
    print("\nComplete List of Students (Tuples):")
    print(student_list)

    # Display each student's ID and name individually
    print("\nList of Students with IDs:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")

    # Calculate the total number of students
    total_students = len(student_list)
    print(f"\nTotal number of students: {total_students}")

    # Calculate the total length of all student names combined
    total_name_length = sum(len(student[1]) for student in student_list)
    print(f"Total length of all student names combined: {total_name_length}")

    # Find the student with the longest name
    longest_name_student = max(student_list, key=lambda student: len(student[1]))
    print(f"The student with the longest name is: {longest_name_student[1]}")

    # Find the student with the shortest name
    shortest_name_student = min(student_list, key=lambda student: len(student[1]))
    print(f"The student with the shortest name is: {shortest_name_student[1]}")

# Call the function to execute the student database management program
manage_student_database()
