#6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.?
def square_list(start,end):
    squares=[]
    for i in range(start,end+1):
        squares.append(i**2)
    print(squares)
print(square_list(1,30))

    