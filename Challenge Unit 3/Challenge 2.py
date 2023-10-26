class student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
   sorted_students = sorted(student_list,
                            key = lambda student:student.cgpa,
                            reverse = True)
   return sorted_students

# example usage:
students = [
    student("hari","A124",7.8),
    student("srikanth","A125",8.1),
    student("dinesh","A126",9.1),
    student("mahldhar","A127",9.9),
]
sorted_students = sort_students(students)

# print thhe list of students
for student  in sorted_students:
  print("Name: {} , Roll Number: {} , CGPA: {}".format(student.name,
                  
student.roll_number,
                                                       student.cgpa))