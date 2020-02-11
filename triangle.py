'''
Exercise: Draw a right handed triangle

function takes in an integer and then prints out a right handed triangle using the hash character.

'''

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
