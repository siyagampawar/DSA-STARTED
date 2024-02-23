def pattern(n):
    
      spaces = 2*((n+1)-1);
      
      for i in range (n+1):
          
          for j in range (i):
              print(j+1,end=" ")
          
          for k in range (spaces):
              print(" ",end=" ")
          
          for l in range (i,0,-1):
              print(l,end=" ")
        
          print("\n")
          
          spaces-=2;
          
num = int(input("Enter n:"))

pattern(num)
