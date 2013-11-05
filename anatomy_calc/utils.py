"""
The MIT License (MIT)

Copyright (c)2013 Rich Friedel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import anatomy_calc.lec_func as lecture
import anatomy_calc.lab_func as lab

def final_grade(lec_grades: dict, lab_grades: dict) -> float:
    """
        lec_exams -> list of lecture exam grades
        final_lec_exam -> float of final lecture exam grade
        lec_quizzes -> list of lecture quiz grades
        lab_exams -> list of lab exam grades
        final_lab_exam -> float of final lab exam grade
        participation -> float of lab participation grade

        Overall grade is determined by both lecture and lab
            lecture = 75%
            lab = 25%

        Calculating Grade -
            (((Test1% + Test2% + Test3% + Test4%) / 4) * 0.7 + ((Quiz Total / Total Possible) * 100) * 0.1 + (Exam%) * 0.2) * 0.75
            +
            (((Practical1 + Practical2 + Practical3) / 3) * 0.6) + (Final Practical% * 0.3) + ((Participation) * 0.1)) * 0.25
    """

    lec_wtd_grade = lecture.weighted_grade(lec_grades['exams'], lec_grades['final_exam'], lec_grades['quizzes'])
    lab_wtd_grade = lab.weighted_grade(lab_grades['exams'], lab_grades['final_exam'], lab_grades['participation'], lab_grades['days_missed'])

    return lec_wtd_grade + lab_wtd_grade


def find_letter_grade(grade: float) -> str:
    """
    Grading Scale -
        89.50 - 100     = A \n
        88.50 - 89.49   = B+ \n
        79.50 - 88.49   = B \n
        78.50 - 79.49   = C+ \n
        69.50 - 78.49   = C \n
        68.50 - 69.49   = D+ \n
        59.50 - 68.49   = D \n
        00.00 - 59.50   = F \n

    @type grade: float
    @param grade: float
    @return: str
    """
    # Check to make sure that the incoming grade is a float and if it isn't
    # check to see if it is an int. If it is an int, reformat it as a float
    # if it isn't either an int or a float, return an error
    if type(grade) != float:
        if type(grade) == int:
            grade_to_convert = float(grade)
        else:
            raise TypeError(
                "Input was: " + str(type(grade)) + " --> input must be either <class 'float'> OR <class 'int'>!")
    else:
        grade_to_convert = grade

    if grade_to_convert >= 89.5:
        return "A"
    elif grade_to_convert >= 88.5 < 89.5:
        return "B+"
    elif grade_to_convert >= 79.5 < 88.5:
        return "B"
    elif grade_to_convert >= 78.5 < 79.5:
        return "C+"
    elif grade_to_convert >= 69.5 < 78.5:
        return "C"
    elif grade_to_convert >= 68.5 < 69.5:
        return "D+"
    elif grade_to_convert >= 59.5 < 68.5:
        return "D"
    else:
        return "F"

def get_letter_grade_definitions(letter_grade: str) -> str:
    """
    Returns the definition of the letter grade that is passed into the function

    Grading Scale -
        89.50 - 100     = A \n
        88.50 - 89.49   = B+ \n
        79.50 - 88.49   = B \n
        78.50 - 79.49   = C+ \n
        69.50 - 78.49   = C \n
        68.50 - 69.49   = D+ \n
        59.50 - 68.49   = D \n
        00.00 - 59.50   = F \n

    @param letter_grade:
    @return:
    """
    letter = letter_grade.lower()

    if letter == "a":
        return "A is between 89.50 - 100"
    elif letter == "b+":
        return "B+ is between 88.50 - 89.49"
    elif letter == "b":
        return "B is between 79.50 - 88.49"
    elif letter == "c+":
        return "C+ is between 78.50 - 79.49"
    elif letter == "c":
        return "C is between 69.50 - 78.49"
    elif letter == "d+":
        return "D+ is between 68.50 - 69.49"
    elif letter == "d":
        return "D is between 59.50 - 68.49"
    else:
        return "F is anything lower than 59.50"

def write_grade_to_file(lec_info: dict, lab_info: dict) -> bool:
    """
    Writes all the grades and totals out to a formatted text file

    @param lec_info:
    @param lab_info:
    @return: True on success
    """
    with open("grades.txt", "w") as f:
        # Computed Grades
        f.write("===== COMPUTED GRADES =====\n")

        # Lecture Grades
        f.write("\n--- Lecture Grades ---\n")

        # Raw Lecture Grades
        raw_lec_grade = lecture.raw_grade(lec_info['exams'], lec_info['final_exam'], lec_info['quizzes'])
        f.write("Raw grades are calculated by simply inputting the numbers and averaging them.\n\n")
        f.write("Your calculated RAW grade for Lecture is: ")
        f.write("{0}\n".format(raw_lec_grade))
        f.write("Your calculated RAW letter grade for Lecture is: ")
        f.write(find_letter_grade(raw_lec_grade) + "\n")
        f.write("{0}\n\n".format(get_letter_grade_definitions(find_letter_grade(raw_lec_grade))))

        # Weighted Lecture Grade
        weighted_lec_grade = lecture.weighted_grade(lec_info['exams'], lec_info['final_exam'], lec_info['quizzes'])
        f.write("Weighted grades are calculated using the formula provided by the professor.\n")
        f.write(
            "The first grade is 75% of the whole grade and the second grade is what it would correlate to as a whole grade.\n\n")
        f.write("Your calculated WEIGHTED grade for Lecture is: ")
        f.write("{0}\n".format(weighted_lec_grade))
        f.write("The WEIGHTED equivalent is: ")
        f.write("{0}\n".format(weighted_lec_grade / 0.75))
        f.write("The WEIGHTED letter equivalent is: ")
        f.write("{0}\n".format(find_letter_grade(weighted_lec_grade / 0.75)))
        f.write("{0}\n\n".format(get_letter_grade_definitions(find_letter_grade(weighted_lec_grade / 0.75))))

        # Lab Grades
        f.write("\n--- Lab Grades ---\n")

        # Raw Lab Grades
        raw_lab_grade = lab.raw_grade(lab_info['exams'], lab_info['final_exam'], lab_info['participation'])
        f.write("Raw grades are calculated by simply inputting the numbers and averaging them.\n\n")
        f.write("Your calculated RAW grade for Lab is: ")
        f.write("{0}\n".format(raw_lab_grade))
        f.write("Your calculated RAW letter grade for Lab is: ")
        f.write("{0}\n".format(find_letter_grade(raw_lab_grade)))
        f.write("{0}\n\n".format(get_letter_grade_definitions(find_letter_grade(raw_lab_grade))))

        # Weighted Lab Grades Output
        weighted_lab_grade = lab.weighted_grade(lab_info['exams'], lab_info['final_exam'], lab_info['participation'], lab_info['days_missed'])
        f.write("Weighted grades are calculated using the formula provided by the professor.\n")
        f.write(
            "The first grade is 25% of the whole grade and the second grade is what it would correlate to as a whole grade.\n\n")

        if lab_info['days_missed'] == 1:
            day_str = "day"
        elif lab_info["days_missed"] > 1 or lab_info["days_missed"] == 0:
            day_str = "days"

        f.write("You missed {0} {1} of lab resulting in a {2}% ({3}pts) decrease in the final overall lab grade.".format(lab_info['days_missed'], day_str, lab_info['days_missed'] * 0.02, weighted_lab_grade * (lab_info['days_missed'] * 0.02)))
        f.write("\nYour calculated WEIGHTED grade for Lab is: ")
        f.write("{0}\n".format(weighted_lab_grade))
        f.write("The WEIGHTED equivalent is: ")
        f.write("{0}\n".format(str(weighted_lab_grade / 0.25)))
        f.write("The WEIGHTED letter equivalent is: ")
        f.write("{0}\n".format(find_letter_grade(weighted_lab_grade / 0.25)))
        f.write(get_letter_grade_definitions(find_letter_grade(weighted_lab_grade / 0.25)) + "\n\n")

        # Final Grades Output
        f_grade = final_grade(lec_info, lab_info)

        f.write("|" + "=" * 50 + "\n")
        f.write("| Your Final Weighted Grade Is: {0}\n".format(f_grade))
        f.write("| Your Final Letter Grade Is: {0}\n".format(find_letter_grade(f_grade)))
        f.write("| {0}\n".format(get_letter_grade_definitions(find_letter_grade(f_grade))))
        f.write("|" + "=" * 50 + "\n\n")

        # Grades output...
        f.write("===== Actual and Estimated Grades =====\n\n")

        # Lecture Header
        f.write("*" * 15)
        f.write("\n*** LECTURE ***\n")
        f.write("*" * 15)

        # Lecture quizzes
        i = 1
        f.write("\n--- Quizzes ---\n")
        for lec_qz in lec_info["quizzes"]:
            f.write("Quiz {0} - {1}\n".format(i, lec_qz))
            i += 1

        # Lecture Exams
        f.write("\n\n--- Exams ---\n")
        i = 1
        for lec_exam in lec_info["exams"]:
            f.write("Exam {0}: {1}\n".format(i, lec_exam))
            i += 1

        # Lecture Final Exam
        f.write("\n\n--- Final Exam ---\n")
        f.write("Final Exam: {0}\n".format(lec_info["final_exam"]))

        # Lecture Days Missed
        f.write("\n--- Days Missed ---\n")
        f.write("Days Missed: {0}\n\n".format(lec_info["days_missed"]))

        # Lab Header
        f.write("*" * 15)
        f.write("\n***** LAB *****\n")
        f.write("*" * 15)

        # Lab Exams
        f.write("\n--- Exams ---\n")
        i = 1
        for lab_exam in lab_info["exams"]:
            f.write("Exam {0}: {1}\n".format(i, lab_exam))
            i += 1

        # Lab Final Exam
        f.write("\n--- Final Exam ---\n")
        f.write("Final Exam: {0}\n".format(lab_info["final_exam"]))

        # Lab Participation
        f.write("\n--- Participation ---\n")
        f.write("Participation: {0}\n".format(lab_info["participation"]))

        # Lab Days Missed
        f.write("\n--- Days Missed ---\n")
        f.write("Days Missed: {0}\n\n".format(lab_info["days_missed"]))

    return f.closed