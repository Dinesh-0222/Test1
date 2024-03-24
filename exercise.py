student_list=[]
student_dict={}
student_info={}
print("Student Management System")
student_name=input("Enter student name: ")
student_age=int(input("Enter student age: "))
student_grade=int(input("Enter student grade: "))
student_list.append(student_name)
#print(student_list)
student_info["Age:"]=student_age
student_info["Grade:"]=student_grade
student_dict.update({student_name:student_info})
#print(student_info)
print("Student information added successfully")
#searching the student 
search_name=input("Enter the name to search or simply click Enter to skip: ")
if search_name in student_list:
          print("Name: ",search_name,"Age: ",student_age,"Grade:",student_grade)
else:
          print(search_name,"student does not exit in the list")
remove_name=input("Enter the name to remove from the list or simply click enter: ")
if remove_name in student_list:
          student_dict.pop(remove_name)
          print(remove_name,"is removed successfully from the student list")
else:
          print("Student named ",remove_name,"doest not found in the list to remove")