#7. Write a python program to access a function inside a function.?
def outer_function():
    def inner_function():

        print("This is the Inner Function")
    print("This is the Outer Function")

   
    inner_function()
outer_function()