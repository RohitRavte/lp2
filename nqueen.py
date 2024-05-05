







def isSafe(i,j):
    for p in range(n):
        if b[i][p]=='Q' or b[p][j]=='Q':
            return False
        

    
    for x in range(n):
        for y in range(n):
            if  i+j == x+y or i-j==x-y:
                if b[x][y]=='Q':
                    return False


    return True





def nqueen(noq):
    if noq==0:
        return True

    for i in range(n):
        for j in range(n):
            if b[i][j] !='Q' and isSafe(i,j):
                b[i][j]='Q'
                if nqueen(noq-1)==True:
                    
                    return True
                
                print("back tracking")
                printboard(b)
                b[i][j] =0
                

                


    return False

def printboard(b):
    for i in b:
        print(i)

flag=True

while flag==True:
    n=int(input("enter number matrix : "))

    b=[[ 0 ] * n for i in range(n)]

    if nqueen(n):
     printboard(b)
    else:
        print("can't place")
    
    ans=input("do you want to continue (y/n)")
    if (ans=='n'):
     flag=False
