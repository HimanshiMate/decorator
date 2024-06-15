# class Test:
#     def __init__(self):
#         print("constructor executed...... ")
# obj=Test()       # implicitily call (object created)
# obj.__init__()    #explicitily call (object name)  


class Test:
    def m1(self):
        print("instance method executed...... ")
obj=Test()       
obj.m1()   
print(dir(Test))


#constructor without parameter
class student:
    def __init__(self):
        print("constructor called....")
        # print(self)
        print(id(self))
       
t=student()
print(id(t))
        