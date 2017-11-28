# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Diary:
    def __init__(self, school_classes):
        self.school_classes = school_classes

    def add_student(self, school_class_name, student_name, scores, attendance):
        self.school_classes[school_class_name][(len(self.school_classes[school_class_name].keys()), student_name)] = {'scores': scores, 'attendance': attendance}

    def give_score(self, school_class_name, student_id, student_name, score):
        self.school_classes[school_class_name][(student_id, student_name)]['scores'].append(score)

    def give_attendance(self, school_class_name, student_id, student_name, attendance):
        self.school_classes[school_class_name][(student_id, student_name)]['attendance'].append(attendance)

    def total_attendance_of_student(self, school_class_name, student_id, student_name):
        return sum(self.school_classes[school_class_name][(student_id, student_name)]['attendance'])

    def get_average_score_in_class(self, school_class_name):
        total_sum_of_scores = number_of_scores = 0
        for k in self.school_classes[school_class_name]:
            scores = self.school_classes[school_class_name][k]
            total_sum_of_scores += sum(scores['scores'])
            number_of_scores += len(scores['scores'])
        return total_sum_of_scores / number_of_scores

    def get_average_score_across_classes(self):
        total_sum_of_scores = number_of_scores = 0
        for classes in self.school_classes:
            for student in self.school_classes[classes]:
                scores = self.school_classes[classes][student]
                total_sum_of_scores += sum(scores['scores'])
                number_of_scores += len(scores['scores'])
        return total_sum_of_scores / number_of_scores

    def dump(self, filename):
        with open(filename, 'w') as file:
            file.write('{\n')
            for school_class in self.school_classes:
                file.write('\t"' + str(school_class) + '": {\n')
                all_students = self.school_classes[school_class]
                for student in all_students:
                    scores_attendance = all_students[student]
                    file.write('\t  {\n\t\t"name": "' + str(student[1]) + '",\n\t\t"scores": ' + str(scores_attendance['scores']) + ',\n\t\t"attendance": ' + str(scores_attendance['attendance']) + '\n\t  },\n')
                file.write('\t},\n')
            file.write('}')

if __name__ == "__main__":
    school_classes = {'1A': {(0, 'Jan Kowalski'): {'scores': [4.0, 3.5], 'attendance': [1, 0, 1]}, (1, 'Krzysztof Nowak'): {'scores': [2.0, 2.0, 3.0], 'attendance': [1, 1, 1]}}, '1B': {(0, 'Patryk Mazurkiewicz'): {'scores': [4.0, 3.0], 'attendance': [1, 1, 0]}}}
    diary = Diary(school_classes)
    diary.add_student('1A', 'Marcin Gorczewski', [4.0, 3.5], [1, 1, 0])
    diary.add_student('1B', 'Michal Olech', [3.5, 5.0], [0, 1, 1])
    score_to_jan_kowalski = input('Give score to Jan Kowalski from 1A class: ')
    diary.give_score('1A', 0, 'Jan Kowalski', score_to_jan_kowalski)
    attendance_to_jan_kowalski = input('Give attendance to Jan Kowalski from 1A class: ')
    diary.give_attendance('1A', 0, 'Jan Kowalski', attendance_to_jan_kowalski)
    print('Total attendance of Jan Kowalski: ' + str(diary.total_attendance_of_student('1A', 0, 'Jan Kowalski')))
    print('Average score in class 1A: ' + str(diary.get_average_score_in_class('1A')))
    print('Average score across classes: ' + str(diary.get_average_score_across_classes()))
    diary.dump('dump.json')
    
