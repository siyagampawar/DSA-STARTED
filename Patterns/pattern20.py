def pattern(N):
    ini = 2*N - 2
    for i in range(1, N+1):
        for j in range(1, i+1):
            print("*", end="")
        for j in range(ini):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        ini -= 2
        print()
    ini = 2
    for i in range(N):
        for j in range(1, N-i):
            print("*", end="")
        for j in range(ini):
            print(" ", end="")
        for j in range(1, N-i):
            print("*", end="")
        ini += 2
        print()
    
    

num = int(input("Enter n:"))

pattern(num)
