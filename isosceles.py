'''
Exercise: Draw an isosceles triangle

Write a function that takes in an integer and then prints out an isosceles using the hash character.
'''

def isosceles(n):
    h_count = 1
    for i in range(1,n+1):
        print(" " * (n-i) + "#" * h_count)
        h_count += 2
n = int(input("Enter the number of rows for your isosceles triangle: "))
isosceles(n)
