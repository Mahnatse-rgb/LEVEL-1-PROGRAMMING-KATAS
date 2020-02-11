'''
Exercise: Draw a square

Write a function, name it square. It takes in an integer and then prints out a square using the hash character.

'''

def square(x):
    x = int(input("Enter the number of rows: "))
    row = "#"*x
    for i in range(x):
       print(row)

square(2)
