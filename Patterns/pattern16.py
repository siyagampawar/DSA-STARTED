def pattern(n):
    ascii=65
    
    for i in range (n):
        
        for j in range (i+1):
            print(chr(ascii+i),end="")
        print("\n")

num = int(input("Enter n:"))

pattern(num)
