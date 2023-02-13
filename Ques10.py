#10. Write a python program to create a function to check whether a string is an anagram or not.?
def is_anagram(a,b):
    if (sorted(a)==sorted(b)):
        print("Yes it is Anagram")
    else:
        print("No it is not Anagram")
    
a=input("Enter First Word :")
b=input("Enter Second Word :")
is_anagram(a,b)