'''
inheritance:- inherit the property of one class into another class.
3 type :- single inheritance 
          multilevel inheritance
          multiple inheritance
'''

#===========================single inheritance=============================
'''
single inheritance:-which have one parent class and one child class,child class access the parent class
syntax:-
class parent_class_name:
     body of the  class

class child_class_name(parent_class_name):
      body of the  class
'''
# class A:
#     name="himanshi"
#     def m1(self):
#         return "this is m1 method"
# class B(A):
#     def m2(self):
#         print("name=",A.name)
#         print("M1=",self.m1())
# obj=B()
# obj.m2()


#===========================multilevel inheritance ===============================
'''syntax-->
class parent_class_name:
	    body of class
class child_class_name1(parent_class_name):
       body of class
class child_class_name2(child_class_name1):
       body of class       
'''
# class A:
#     name="himanshi"
#     def m1(self):
#         return "this is m1 method"
# class B(A):
#     age=20
#     def m2(self):
#         print("name=",A.name)
#         print("M1=",self.m1())
# class C(B):
#     def m3(self):
#         print("age=",B.age)
#         self.m2()
# obj=C()
# obj.m3()    

#====================multiple inheritance====================
'''multiple inheritance-->child class inherite the one or more patrent class
syntax:-
Class parent_class_name1:
       Body of the class

Class  parent_class_name2:
     Body of the class

Class child_class_name(parent_class_name1, parent_class_name2):
     Body of the class
'''
# class parent1:
#     def m1(self):
#         print("parent 1 method")
# class parent2:
#     def m1(self):
#         print("parent 2 method")
# # class child(parent1, parent2):
# #     def m2(self):
# #         self.m1()
# class child(parent2, parent1):
#     def m2(self):
#         self.m1()
# obj=child()
# obj.m2()      


# class parent1:
#     def m1(self):
#         print("parent 1 method")
# class parent2:
#     def m2(self):
#         print("parent 2 method")
# # class child(parent1, parent2):
# #     def m2(self):
# #         self.m1()
# class child(parent2, parent1):
#     def m3(self):
#         self.m1()
#         self.m2()
# obj=child()
# obj.m3()  


#super method-->parent ka variable and  child ka variable same ho par hme parent ka variable acess krna h tb hm super method ka use krte h.
class A:
    def m1(self):
        print("m1 called from A")
class  B(A):
    def m1(self):
        print("m1 called from B")
        super().m1()
obj=B()
obj.m1()                