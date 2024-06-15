#instance method
# class student:
#     def display(self,name):
#         self.name=name
#         print("name=",name)
#     def show(self,age):
#         self.age=age
#         self.display("himanshi")
#         print("age=",age)    
# obj=student()
# obj.display("himanshi")
# obj.show(20) 


#class method/ static method :-->static variable ko change krne ke liye class method ka use krte h
# @classmethod -->kisi bhi word ke smne @ lga hoga to vo decorater kehlata h , decorater value change kr deta h 
# instead of self, we use cls keyword in the parameters

# class book:
#     price=1000
#     def book_detail(self,name,author):
#         self.name=name
#         self.author=author
#     @classmethod
#     def update_price(cls,price):
#         cls.price=price
#     def show_detail(self,page):
#         self.page=page
#         print("book name=",self.name)
#         print("book author=",self.author)
#         print("book price=",book.price)
#         print("book page=",self.page)
# obj=book()
# obj.book_detail("python","neeraj")
# obj.update_price(500) 
# obj.show_detail(2000)       


#==============static method============
# class Student:
#     @staticmethod
#     def greet():
#         print("thank for visit")
#     def greet1(self):
#         print("welcome to my webpage")
# obj=Student()
# obj.greet()
# # Student.greet()   
# obj.greet1()             
# # Student.greet1() #when we write self then we call through object.