#instance variable-->object ke sath value bhi vary krti h 
# class ke andr instance variable to access krne ke liye self ka use krte h,self value ke 
# reference ko hold krta h  

# class ke bhr instance variable ko acess krne ke liye object ka use krte h 

#static-object doesnot depend on variable .value hr jagah same rahegi
#local variable-->jo apne scope me hi define ho
# self is a reference variable of current class 
'''
class Student:
    quali="B.Tech"
    def __init__(self,name):
        self.name=name   #instance variable
    def display(self):
        age=45
        print("name=",self.name)
        print("age=",age)
        print("quali=",Student.quali)    
obj=Student("himanshi")
obj.display()   
'''
'''
how we declare instance variable:-
1.through constructor
2.through instance method
3.through object
'''
'''
class Student:
    def display(self,name):
        self.name=name
    def show(self):    
        print("name=",self.name)   
obj=Student()
obj.display("himanshi")
obj.show()   
'''
# class Student:
#     def __init__(self,name):
#         self.name=name       #through constructor
#     def display(self,age):
#         self.age=age     #through instance method
#     def show(self):    
#         print("name=",self.name) 
#         print("age=",self.age)
#         print("quali=",self.quali)  
# obj=Student("himanshi")
# obj.display(37)
# obj.quali="M.Tech"   #through object
# obj.show() 


#========================================static variable declaration and access
'''class Student:
    quali = "M.Tech"   # static variable declare inside the class   
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.school = "SHSS"  # static variable declare inside the constructor
    def display(self):
        Student.gread = "P.hd"   # static variable declare inside the instence variable
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Quali =",Student.quali)  # static variable access inside the class through class name
        print("School = ",Student.school) # static variable access inside the class through class name
        print("Gread = ",Student.gread) # static variable access inside the class through class name
        print("Achivment = ",Student.achivment)   # static variable access inside the class through class name

obj = Student("Neeraj",37)
Student.achivment="Gate-qualified"   # static variable declare outside of the class
print("Access through class_Name = ",Student.quali) # static variable access outside the class through class name
print("Access through object = ",obj.quali) # static variable access outside the class through object
obj.display()
print("Access through class_Name = ",Student.gread) # static variable access outside the class through class name
print("Access through class_Name = ",Student.school)# static variable access outside the class through class name
print("Access through class_Name = ",Student.achivment)# static variable access outside the class through class name
# obj.display()
'''
# local variable
class student:
    def display(self):
        global a
        a=10
        print("value of a1=",a)
    def show(self):
        print("value of a2=",a) 
    def new():
        print("value of a3=",a)       
obj=student()
obj.display()
obj.show()
student.new()        
