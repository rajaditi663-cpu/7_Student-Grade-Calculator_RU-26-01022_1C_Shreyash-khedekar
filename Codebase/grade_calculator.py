def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, num_subjects=5):
    return (total / (num_subjects * 100)) * 100


def get_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def get_result(percentage):
    if percentage >= 40:
        return "Pass"
    return "Fail"


def get_mark(subject_no):
    while True:
        user_input = input(f"Enter marks for subject {subject_no}: ").strip()
        try:
            mark = float(user_input)
            if 0 <= mark <= 100:
                return mark
        except ValueError:
            pass
        print("Invalid marks. Enter a number between 0 and 100")


def main():
    num_subjects = 5

    while True:
        name = input("\nEnter student name: ").strip()
        marks = []

        for i in range(1, num_subjects + 1):
            marks.append(get_mark(i))

        total = calculate_total(marks)
        percentage = calculate_percentage(total, num_subjects)
        grade = get_grade(percentage)
        result = get_result(percentage)

        total_display = int(total) if total.is_integer() else round(total, 2)
        print(
            f"{name} | Total: {total_display} | "
            f"Percentage: {percentage:.2f}% | Grade: {grade} | Result: {result}"
        )

        again = input("\nEnter another student? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
