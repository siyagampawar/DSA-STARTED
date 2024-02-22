def pattern(n):
    
    for i in range (n):
        #space before stars
        for j in range(n-i):
            print(" ",end="")
        #stars
        for k in range(2*i+1):
            print("*",end="")
        print("\n")
        
num = int(input("Enter n:"))

pattern(num)