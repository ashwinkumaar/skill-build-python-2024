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

Answer: a.



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

Ans: Assuming that the `valid = True` is not inside the inner while block, the answer is d.
If the `valid = True` is inside the inner while block, the answer is a.


3.	List 5 examples of exceptions.
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError



4.	Write a python program to detect the Division by zero exception without using try except

"""

def find_division_by_zero(a, b):
    if b == 0:
        print("Division by zero")
        return None
    return a / b

print(find_division_by_zero(6, 0))
print(find_division_by_zero(6, 0.5))



"""

5.	Write the above program of zero division using try except block

"""

def find_division_by_zero_try_catch(a, b):
    ans = None
    try:
        ans = a / b
    except ZeroDivisionError:
        print("Division by zero")
    except:
        print("Other exception")
    finally:
        return ans

print(find_division_by_zero_try_catch(6, 0))
print(find_division_by_zero_try_catch(6, 0.5))



"""
6.	Write a program to detect  ValueError
"""

def detect_value_error(str_input):
    try:
        print(int(str_input))
    except ValueError:
        print("Value error occurred")

detect_value_error("6")
detect_value_error("abc")

"""
7.	Write a program to create a directory and the program should raise an exception if the directory already exists.
If your directory doesn’t exists, it should create the directory and just raise a RuntimeError exception,
i.e you should be able to catch two exceptions in one except statement – i.e FileExistsError, RuntimeError
"""

import os

directory_name = "my_directory"

try:
  if os.path.exists(directory_name):
    raise FileExistsError(f"The directory '{directory_name}' already exists.")
  else:
    os.mkdir(directory_name)
    raise RuntimeError(f"Directory '{directory_name}' created, raising RuntimeError.")
except (FileExistsError, RuntimeError) as e:
  print(f"Exception caught: {e}")


"""

9.	Is the following code valid ?

try:
                #Do something
except:
                #Do something
finally:
                #Do something

Ans: Yes, the structure of the provided code is valid.
In this code:

-   The try block is where we place the code that might raise an exception.
-   The except block catches any exceptions that occur in the try block. 
    If no specific exception type is specified, it catches all exceptions.
-   The finally block contains code that will always execute, regardless of whether an exception was raised or not.


10.	What will be the output of the below –
def foo():
                try:
                                return 1
                finally:
                                return 2
                k = foo()
                print(k)

Ans: When a return statement is executed in a try block, it is not immediately returned if there is a finally block. 
Instead, the finally block is executed before the function actually returns. 
If the finally block contains a return statement, it will override the return statement in the try block.
Therefore, the output of this code will be 2.


11.What is the difference between r+ and w+ mode for files

Ans: 

r+ Mode
    Read and Write Mode: The file is opened for both reading and writing.
    File Must Exist: The file must already exist. If the file does not exist, an FileNotFoundError is raised.
    No Truncation: The file's existing contents are not truncated (i.e., not erased) when the file is opened.

w+ Mode
    Read and Write Mode: The file is opened for both reading and writing.
    File Creation: If the file does not exist, it is created.
    File Truncation: If the file already exists, its contents are truncated (i.e., erased) when the file is opened.


12. What is the difference between write and append mode?

Ans:

write Mode ('w')
    Write Mode: The file is opened for writing.
    File Creation: If the file does not exist, it is created.
    File Truncation: If the file already exists, its contents are truncated (i.e., erased) when the file is opened.
    File Pointer: The file pointer is positioned at the beginning of the file.
    Overwrite: Writing to the file starts from the beginning, overwriting any existing content.

append Mode ('a')
    Append Mode: The file is opened for writing.
    File Creation: If the file does not exist, it is created.
    No Truncation: If the file already exists, its contents are not truncated.
    File Pointer: The file pointer is positioned at the end of the file.
    Append: Writing to the file starts from the end, preserving existing content and appending new data.


"""
