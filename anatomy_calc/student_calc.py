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
from anatomy_calc.utils import final_grade, find_letter_grade, get_letter_grade_definitions, write_grade_to_file

''' Lecture Quizzes '''
quiz_1 = 60.0
quiz_2 = 50.0
quiz_3 = 100.0
quiz_4 = 100.0
quiz_5 = 100.0
quiz_7 = 100.0
quiz_6 = 100.0
quiz_8 = 100.0
quiz_9 = 100.0
quiz_10 = 100.0
quiz_11 = 100.0

''' Lecture Exams '''
exam_1 = 50.0
exam_2 = 71.5
exam_3 = 100.0
exam_4 = 100.0

lec_final_exam = 100.0

''' Lecture Days Missed '''
lec_days_missed = 0

''' Participation '''
participation = 100.0

''' Lab Exams '''
practical_1 = 98.0
practical_2 = 100.0
practical_3 = 100.0

lab_final_exam = 100.0

''' Lab Days Missed '''
lab_days_missed = 1


lec_quizzes =[quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10, quiz_11]
lec_exams = [exam_1, exam_2, exam_3, exam_4]
lab_exams = [practical_1, practical_2, practical_3]

lec_info = {'quizzes': lec_quizzes, 'exams': lec_exams, 'final_exam': lec_final_exam, 'days_missed': lec_days_missed}
lab_info = {'exams': lab_exams, 'final_exam': lab_final_exam, 'participation': participation, 'days_missed': lab_days_missed}

if write_grade_to_file(lec_info, lab_info):
    print("File Output Successful!")
else:
    print("File Output ERROR!!!")

# Console output for testing...
print("\nFinal Grade: {0}".format(final_grade(lec_info, lab_info)))
print("Letter Grade: {0}".format(find_letter_grade(final_grade(lec_info, lab_info))))
print("{0}\n".format(get_letter_grade_definitions(find_letter_grade(final_grade(lec_info, lab_info)))))

