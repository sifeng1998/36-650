# Question 5
def pyra_func(star_input):
    #number of spaces between stars
    space_num = star_input -1
    
    #iterate through how many rows
    for i in range(0,star_input):
        #iterate through how many spaces between stars
        for j in range(0,space_num):
            print(end=' ')
        #decrease k by 1 after each loop
        space_num = space_num - 1;
        #iterate through how many star columns
        for j in range(0,i+1):
            print('* ',end='')
        print("\r")

pyra_func(5)