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
