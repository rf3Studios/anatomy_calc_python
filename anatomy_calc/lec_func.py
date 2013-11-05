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

'''
Attendance -
    0 pts per class missed up to 3 classes missed
    2 pts per class missed after 3 classes missed
    7 missed classes results in automatic failure
'''
# TODO Create function to handle missed classes

def avg_exam_grade(lec_exams):
    #TODO Finish writing documentation for this function
    """ (list) -> float
    Returns the average of all exam grades passed as lec_exams
    If the second exam grade is higher than that first exam grade
    take the difference of the two grades, divide that by two and
    add the total to the first exam grade
    """
    # Create a temp list
    temp_list = []

    # Load the temp list with the lec_exams values
    for item in lec_exams:
        temp_list.append(item)

    # If the second grade is higher than the first grade
    if temp_list[1] > temp_list[0]:
        dif = temp_list[1] - temp_list[0]
        temp_list[0] += dif / 2

    return sum(temp_list) / len(temp_list)


def avg_quiz_grade(lec_quizzes):
    #TODO Finish writing documentation for this function
    """
    Returns the average of lec_quizzes after removing the lowest
    grade in the list
    @param lec_quizzes:
    @return:
    """
    # Create a temp list because I don't want to alter the original list
    temp_list = []

    for item in lec_quizzes:
        temp_list.append(item)

    # Find the index that the low value occurs
    index_of_low_val = temp_list.index(min(temp_list))

    # Remove the value
    del temp_list[index_of_low_val]

    return (sum(temp_list) / (len(temp_list) * 100)) * 100


def weighted_exam_grade(lec_exams: list) -> float:
    #TODO Finish writing documentation for this function
    """
    The formula => (sum(lec_exams) / 4) * 0.7
    """
    return avg_exam_grade(lec_exams) * 0.7


def weighted_final_exam_grade(final_exam: float) -> float:
    #TODO Finish writing documentation for this function
    return final_exam * 0.2


def weighted_quiz_grade(lec_quizzes: list) -> float:
    #TODO Finish writing documentation for this function
    """
    Returns the weighted result of lec_quizzes after removing
    the lowest grade in the list

    @param lec_quizzes: List of quizzes
    @return: float
    """
    return (avg_quiz_grade(lec_quizzes)) * 0.1


def raw_grade(lec_exams: list, final_exam: float, lec_quizzes: list) -> float:
    #TODO Finish writing documentation for this function
    """
    @todo Write documentation for this function

    @param lec_exams:
    @param final_exam:
    @param lec_quizzes:
    @return:
    """
    return (sum(lec_exams) + sum(lec_quizzes) + final_exam) / (1 + len(lec_exams) + len(lec_quizzes))


def weighted_grade(lec_exams, final_exam, lec_quizzes):
    #TODO Finish writing documentation for this function
    """
    @todo Write documentation for this function

    @param lec_exams: List of the exam grades
    @param final_exam: The final exam score
    @param lec_quizzes: List of quiz grades
    @return: A float of the processed values
    """
    return (weighted_exam_grade(lec_exams) + weighted_quiz_grade(lec_quizzes) + weighted_final_exam_grade(
        final_exam)) * 0.75