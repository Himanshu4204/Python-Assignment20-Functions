# 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.?
def list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(list([1,2,4,6,3,1,4,2,5,3,1,2,4,3]))