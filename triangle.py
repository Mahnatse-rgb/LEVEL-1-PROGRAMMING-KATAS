def triangle(n):
    n = int(input("Enter the number of rows: "))
    row = 0
    while row<n:
        hash = row+1
        while hash>0:
            print("#",end="")
            hash = hash-1
        row = row+1
        print()

triangle(4)  