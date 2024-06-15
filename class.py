'''
syntax-->class(keyword) class_name:
                 "doc_string"
               variable --> instance,local,static/class variable
               method -->  instance,local,static
'''
# class can be called as constructor and without construct
#========================= class without constructor==========================
# class Student:
#     stu_qualification="M.Tech"
#     def Stu_detail(name,age):
#         print("Stu_Name=",name)
#         print("Stu_Age=",age)
#         print("Stu_Qualification=",Student.stu_qualification)
# obj=Student
# obj.Stu_detail("Himanshi",20) 

# when we use parenthesis afteer the class then constructor automatically called
class Student:
    stu_qualification="M.Tech"
    def Stu_detail(name,age):
        print("Stu_Name=",name)
        print("Stu_Age=",age)
        print("Stu_Qualification=",Student.stu_qualification)
obj=Student()
obj.Stu_detail("Himanshi",20)  

#==================with constructor===============
'''
constructor is a special kind of method which is automatically called while making object we do not have to call it
(__init__)underscore before any word this thing is known as dander, magic, special function
'''
# class Student:
#     stu_qualification="M.Tech"
#     def __init__(self):
#         print("constructor called")
# obj=Student()
# print(obj)

# variable which start with self parameter instance variable 