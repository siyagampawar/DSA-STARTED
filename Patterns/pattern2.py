def pattern(n):
    
    for i in range (n+1):
        for j in range (i):
            print("* ",end="")
        print("\n")

num = int(input("Enter n:"))

pattern(num)
