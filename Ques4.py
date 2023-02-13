#4. Write a python program to create a function that checks whether a passed string is palindrome or not.?
def is_palindrome(string):
    string=''.join( e for e in string if e.isalnum()).lower()
    if string==string[::-1]:
        return "String is palindrome"
    else:
        return "String is not palindrome"

string=input("Enter a String :")
print(is_palindrome(string))

