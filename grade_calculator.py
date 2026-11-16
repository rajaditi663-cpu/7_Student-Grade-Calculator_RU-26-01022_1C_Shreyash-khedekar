def calculate_total(marks_list):
    """Calculates and returns the total sum of marks in 5 subjects."""
    return sum(marks_list)


def calculate_percentage(total_marks, num_subjects=5):
    """Calculates and returns the percentage based on total marks."""
    return total_marks / num_subjects


def determine_grade_and_status(percentage, marks_list):
    """
    Determines the grade and pass/fail status.
    Grading criteria:
      >= 85: A
      >= 70: B
      >= 55: C
      >= 40: D
      < 40:  F (Fail)
    Also ensures any subject mark below 40 triggers a Fail status.
    """
    for mark in marks_list:
        if mark < 40:
            return "F", "Fail"

    if percentage >= 85:
        return "A", "Pass"
    elif percentage >= 70:
        return "B", "Pass"
    elif percentage >= 55:
        return "C", "Pass"
    elif percentage >= 40:
        return "D", "Pass"
    else:
        return "F", "Fail"


def get_valid_marks(subject_num):
    """Validates input marks to ensure they are numbers between 0 and 100."""
    while True:
        try:
            val = float(input(f"Enter marks for subject {subject_num}: "))
            if 0 <= val <= 100:
                return val
            else:
                print("Invalid marks. Enter a number between 0 and 100.")
        except ValueError:
            print("Invalid marks. Enter a number between 0 and 100.")


def main():
    print("=== Student Grade Calculator ===")
    
    while True:
        name = input("\nEnter student's name: ").strip()
        
        marks = []
        for i in range(1, 6):
            mark = get_valid_marks(i)
            marks.append(mark)
            
        total = calculate_total(marks)
        percentage = calculate_percentage(total)
        
        grade, status = determine_grade_and_status(percentage, marks)
        
        print("\n--- Result Record ---")
        print(f"Name: {name} | Total: {total:.0f} | Percentage: {percentage:.2f}% | Grade: {grade} | Result: {status}")
        
        choice = input("\nAnother student? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nExiting Student Grade Calculator. Good luck with your lab submission!")
            break


if __name__ == "__main__":
    main()