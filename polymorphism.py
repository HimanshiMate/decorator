'''polymorphism -->many form 
2 types --> overloading
            overriding
            
generally python donot support overloading 
multidispatch is used when two function with different parameter are present 
and we want to access both two function     '''

class A:
    def new(self,a,b):
        return a+b
    def new(self,x,y,z):
        return x+y+z
obj=A()
obj.new(5,6,7)
print(obj.new(5,6,7))

# obj.new(5,6)
# print(obj.new(5,6))

# ================================
'''by using default arugument'''
# class A:
#     def new(self,x=0,y=0,z=0):
#         return x+y+z
# obj=A()
# obj.new(5)
# print(obj.new(5))
# obj.new(5,5)
# print(obj.new(5,5))
# obj.new(5,5,5)
# print(obj.new(5,5,5))

# ====================
# from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def add(self,x,y):
#         print(x+y)
#     @dispatch(int,int,int)
#     def add(self,x,y,z):
#         print(x+y+z)  
# obj=A()
# obj.add(5,6)
# obj.add(4,5,6)  


#============
'''
overriding -->different class have  same function with same parameter that is known as method overriding '''

# class A:
#     def add(self,a,b):
#         print("output from parent class")
# class B(A):
#     def add(self,x,y):
#         print("output from child class")
#         super().add(3,6)    
# obj=B()
# obj.add(3,6)

