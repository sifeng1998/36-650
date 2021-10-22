# Question 1
X = [[10,8],
     [2 ,4],
     [1 ,7]]

def trans_matrix(X):
    a=len(X)
    b=len(X[0])
   
    #iterate through rows
    for i in range(b):
        result=[]
        #iterate through columns
        for j in range(a):
            result.append(X[j][i])
        print(result)

trans_matrix(X)