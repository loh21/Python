a = 1
b = -1
flag = False
#attempt
def check_status(a, b, flag):
    ##Your code here
    if a > 0 or b > 0 and flag == False:
        print('false')
    elif a < 0 and b < 0 and flag == True:
        print('true')
    
check_status(a, b, flag)

#answer
def check_status(a, b, flag):
    ##Your code here
    con1 = ((a>=0 and b<0 or a<0 and b>=0) and flag == False)
    con2 = (a<0 and b<0 and flag == True)
 
    con = con1 or con2
 
    return con