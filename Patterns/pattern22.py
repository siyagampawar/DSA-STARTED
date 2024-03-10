def pattern(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            bottom = j
            right = (2*n - 2) - j
            left = (2*n - 2) - i
            print((n - min(min(top, bottom), min(left, right))), end=" ")
        print()

        
num = int(input("Enter n:"))

pattern(num)