# Question 3
def oneAway(str1,str2):
    # compare the length of two strings
    # help to check the "insert a character"
    if len(str1)-len(str2)>1 or len(str2)-len(str1)>1: 
        return FALSE
    elif len(str1) == len(str2):
        return oneAway_replace(str1,str2);
    elif len(str1) > len(str2):
        return oneAway_remove(str1,str2);
    else:
        return oneAway_remove(str2,str1)

    
def oneAway_replace(str1,str2):
    # check the "replace a character"
    count_replace=0
    for i in range(len(str1)):
        if not str1[i] == str2[i]:
            count_replace = count_replace+1;
            # only allow one change in replacing the character
            if count_replace > 1:
                return False;
    return True;

def oneAway_remove(str1,str2):
    # check the "remove a character"
    count_remove=0
    # set a null value for iterating through each character
    i=0
    while i<len(str2):
        if str1[i+count_remove] == str2[i]:
            i = i+1
        else:
            count_remove=+1
            if count_remove > 1:
                return False
    return True

print(oneAway("pale","ple"))
print(oneAway("pales","pale"))
print(oneAway("pale","bale"))
print(oneAway("pale","bake"))