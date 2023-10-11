class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
  
def sort_students(students_list):
        sort_students= sorted(students_list,key=lambda student:                      student.cgpa,reverse=True)
        return sort_students
students=                            [student("tamil","A123",7.8),                                        student("arasan","A124",8.9),   student("vella","A125",9.1), student("aishu","A126",9.9),]    
sorted_students=               sort_students(   students)
 

for student in sorted_students:
     print("Name{}:","RollNumber:{}","CGPA:{}".format(student.name,student.roll_number,student.cgpa))