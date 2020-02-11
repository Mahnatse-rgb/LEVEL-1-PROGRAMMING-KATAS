'''
Exercise: check if a number is even or odd.

Your function should take in an integer and print out the word “even” or “odd” depending on the nature of the input
'''

def even_or_odd(n):

    if n % 2 == 0:
        print ("even")
    
    else:
     print("odd")

num = int(input("Enter a number: "))
even_or_odd(num)
