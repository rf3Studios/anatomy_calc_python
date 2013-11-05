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
    Missed lab results in a 2% reduction of the final grade

Grading -
    Final grade determined as follows:
        3 Tests =       20% each
        Final exam =    30%
        Participation = 10%
'''
def avg_exam_grade(exams):
    return sum(exams) / len(exams)

def weighted_exam_grade(exams):
    return avg_exam_grade(exams) * 0.6

def weighted_final_exam(final_exam):
    return final_exam * 0.3

def weighted_participation(participation):
    return participation * 0.1

def raw_grade(exams, final_exam, participation):
    return (sum(exams) + final_exam + participation) / (2 + len(exams))

def weighted_grade(exams, final_exam, participation, days_missed):
    grade = (weighted_exam_grade(exams) + weighted_final_exam(final_exam) + weighted_participation(participation))

    if days_missed > 0:
        return (grade - (grade * (days_missed * 0.02))) * 0.25
    else:
        return grade * 0.25