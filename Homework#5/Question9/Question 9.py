# Question 9 
# Recursive function to check whether the string is the palindrome
 
def isPalindrome(str):
       
    # length of s
    l = len(str)
     
    # check edge case for length less than 2
    if l < 2:
        return True
 
    # check whether the first character and last character are equal
    elif str[0] == str[l - 1]:
        
        # pass them and go through the second and last second character recursively
        return isPalindrome(str[1: l - 1])
 
    else:
        return False
 
print(isPalindrome("kayak"))
print(isPalindrome("hello"))