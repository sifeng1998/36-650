# Question 4
def tri_num(n):
    #check for invalid input 
    if (not isinstance(n, int)):
        return("Invalid Input")
    
    elif (n < 0):
        return("Invalid Input")       
    
    else:        
        #set the first number to be 1
        num = 1;
        #iterate through how many rows
        for i in range(0,n):
            #iterate through how many numbers in a row
            for j in range(0,i+1):
                print(num,end=' ')
                #increases number by 1 as needed in the triangle
                num = num + 1
            print("\r")

tri_num(3)
tri_num(6)
tri_num(4.5)
tri_num(-10)