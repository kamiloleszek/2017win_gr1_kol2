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

class SchoolCourse:
	def __init__(self, name, students_list):
		self.name = name
		self.attended_students = students_list

class Student:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses = []

	def add_course(self, course):
		self.courses.append(course)
		

class Diary:
	def __init__(self, school_class):
		self.school_class = school_class

class SchoolClass:
	def __init__(self, name, list_of_students):
		self.class_name = name
		self.students_list = list_of_students
	
	def show_all_students():
		return self.students_list



if __name__ == "__main__":
	
	jan_kowalski = Student("Jan", "Kowalski")
	adam_babacki = Student("Adam", "Babacki")
	piotr_cabacki = Student("Piotr", "Cabacki")
	krzysztof_nowak = Student("Krzysztof", "Nowak")
	katarzyna_bak = Student("Katarzyna", "Bak")
	monika_wojcik = Student("Monika", "Wojcik")

	maths = SchoolCourse("Maths", [jan_kowalski, piotr_cabacki])
	physics = SchoolCourse("Physics", [krzysztof_nowak, piotr_cabacki])
	chemistry = SchoolCourse("Chemistry", [katarzyna_bak, monika_wojcik])
	history = SchoolCourse("History", [adam_babacki, jan_kowalski, monika_wojcik, piotr_cabacki])

	A_students = [jan_kowalski, adam_babacki, piotr_cabacki]
	B_students = [krzysztof_nowak, katarzyna_bak, monika_wojcik]

	highschool_class_A = SchoolClass("1A", A_students)
	highschool_class_B = SchoolClass("1B", B_students)
	
	highschool_diary_A = Diary(highschool_class_A)
	highschool_diary_B = Diary(highschool_class_B)

	
