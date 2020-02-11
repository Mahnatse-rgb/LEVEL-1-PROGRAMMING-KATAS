'''
Write a function named hello, it needs to take in a string as an argument. The function should work like this:
eg: hello("Tshepo")
        
        should output

Hello Tshepo!
'''

def hello(name):    
        return "Hello" + " " + name + "!"

user_name = input("Enter user name: ")

print(hello(user_name))

