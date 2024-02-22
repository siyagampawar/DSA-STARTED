def pattern(n):
    
    for i in range (n+1):
              
        if(i%2==0):
                init=1
        else:
                init=0   
                
        for j in range (i):
            print(1-init,end="")
            init = 1-init
        print("\n")

num = int(input("Enter n:"))

pattern(num)
