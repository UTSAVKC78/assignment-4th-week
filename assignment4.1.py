def calculate_grade(score):
    if score < 0 or score > 100:
        return "error: Score is out of range (0-100)"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score = float(input("enter the score between 0 and 100: "))
    grade = calculate_grade(score)
    print(f"grade: {grade}")
except valueError:
    print("error: invalid input. Please enter a numeric value between 0 and 100.")
