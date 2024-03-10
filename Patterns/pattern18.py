def pattern(n):
    
    
    for i in range (n):
        ascii=65+n
        for j in range (ascii-i-1,ascii):
            print(chr(j),end="")
        print("\n")

num = int(input("Enter n:"))

pattern(num)
