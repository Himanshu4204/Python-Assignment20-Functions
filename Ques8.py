#8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.?
def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")
string=input("Enter a String :")
count_case(string)






