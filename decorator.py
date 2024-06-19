def decorator(x):
    def wrapper():
        print("start worrk")
        x()
        print("stop work")
    return wrapper

# def original_fun():
#     print("this is original function")
# var=decorator(original_fun)
# var()

@decorator
def original_fun():
    print("this is original function")
original_fun()
