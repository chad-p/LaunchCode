def course_grader(test_scores):

    average = sum(test_scores) / len(test_scores)
    smallest_grade = min(test_scores)

    if average >= 70 and smallest_grade >= 50:
        return "pass"
    else:
        return "fail"


def main():
    print(course_grader([100,75,45]))
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"


if __name__ == "__main__":
    main()
