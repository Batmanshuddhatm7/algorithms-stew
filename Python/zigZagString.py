def printZigZagConcat(str, n): 
    if n == 1: 
        print(str)      
        return
    l = len(str) 
    arr=["" for x in range(l)] 
    row = 0
    for i in range(l): 
        arr[row] += str[i] 
        if row == n - 1: 
            down = False
        elif row == 0: 
            down = True
        if down: 
            row += 1
        else: 
            row -= 1
    for i in range(n): 
        print(arr[i], end = "") 
str = "GEEKSFORGEEKS"
n = 3
printZigZagConcat(str, n) 
  
  
