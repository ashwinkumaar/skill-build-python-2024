"""
1.	What happens if the file is not found in the following python code ?

a = False
while not a:
                try:
                                f_n = input(“Enter file name”)
                             i_f = open(f_n, ‘r’)
              except:
                                print(“Input file not found”)

a)	No error
b)	Assertion error
c)	Input output error
d)	Name error


2.	What will be the o/p if input entered is 6

valid = False
while not valid:
                try:
                                n =int(input(“Enter a number”))
                                while n%2==0:
                                                print(“Bye”)
                              valid = True

               except ValueError:
                                print(“Invalid”)

a)	Bye(printed once)
b)	No output
c)	Invalid(printed once)
d)	Bye(printed infinite number of times)


3.	List 5 examples of exceptions.


4.	Write a python program to detect the Division by zero exception without using try except

5.	Write the above program of zero division using try except block

6.	Write a program to detect  ValueError


7.	Write a program to create a directory and the program should raise an exception if the directory already exists. If your directory doesn’t exists, it should create the directory and just raise a RuntimeError exception, i.e you should be able to catch two exceptions in one except statement – i.e FileExistsError, RuntimeError



9.	Is the following code valid ?

try:
                #Do something
except:
                #Do something
finally:
                #Do something

10.	What will be the output of the below –
def foo():
                try:
                                return 1
                finally:
                                return 2
                k = foo()
                print(k)

11.What is the difference between r+ and w+ mode for files

12. What is the difference between write and append mode?

"""
