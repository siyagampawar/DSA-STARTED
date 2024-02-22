def pattern(n):
    num=1
    for i in range (n+1):
        for j in range (i):
            print(num,end=" ")
            num= num+1
        print("\n")

num = int(input("Enter n:"))

pattern(num)
