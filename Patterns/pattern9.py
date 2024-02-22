def pattern(n):

        #pyramid1
    for i in range (n):
        #space before stars
        for j in range(n-i):
            print(" ",end="")
        #stars
        for k in range(2*i+1):
            print("*",end="")
        print("\n")
        
        #pyramid2
    for i in range (n-1,-1,-1):
        #space before stars
        for j in range(n-i):
            print(" ",end="")
        #stars
        for k in range(2*i+1):
            print("*",end="")
        print("\n")
        
        
num = int(input("Enter n:"))

pattern(num)