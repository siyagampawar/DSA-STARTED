def pattern(n):
    for i in range (n):
        for j in range(n):
            print("* ",end="")
        print("\n")
            
num = int(input("Enter n:"))

pattern(num)



