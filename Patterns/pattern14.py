def pattern(n):
    
    
    for i in range (n):
        ascii=65
        for j in range (i+1):
            print(chr(ascii+j),end="")
        print("\n")

num = int(input("Enter n:"))

pattern(num)
