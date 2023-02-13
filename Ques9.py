#9. Write a python program to create a function to check whether a string is a pangram or not.?
import string

alphabet=set(string.ascii_lowercase)

def ispangram(string):
    return set(string.lower()) >= alphabet

string=input("Enter a String or Sentence :")
if(ispangram(string)==True):
    print("Yes")
else:
    print("No")

