def main():
    # Sample student marks dictionary
    student_marks = {
        "John": 85,
        "Alice": 92,
        "Bob": 78,
        "Emma": 95,
        "David": 88
    }
    
    # Get student name from user
    student_name = input("Enter student name: ")
    
    # Check if student exists and display marks
    if student_name in student_marks:
        print(f"Marks for {student_name}: {student_marks[student_name]}")
    else:
        print(f"Student '{student_name}' not found in the records.")

if __name__ == "__main__":
    main()