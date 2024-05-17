### Skill Build - Python - May/June 2024

### HW1

"""
Q1
1.Write a program to determine the repeated element in the given list.
(note: array will have only one single repeated element)
Ex: input_list=[2,3,4,5,2]
ouput=2
"""
print("\nQ1")
def determineRepeatedElement(inputList):
    counts = dict()
    for i in inputList:
        counts[i] = counts.get(i, 0) + 1
    return [k for k, v in counts.items() if v > 1]


testList = [1, 2, 3, 4, 3, 1, 'a', 'abc', "a", 'b', "abc"]
repeatedElements = determineRepeatedElement(testList)
print(f"Repeated Element(s): {repeatedElements}")


"""
Q2
2. write an program for searching an element in the list.
hint: implement brute force approach (linear search) , try to find using binary search and
observe the difference in performance.
"""
print("\nQ2")
import time
def linear_search(element, inputList):
    for idx, item in enumerate(inputList):
        if item == element:
            return idx
    return -1

searchItems = [1, 'b', "abc", 12]
for item in searchItems:
    print(f"Index of element {item} using Linear search: {linear_search(item, testList)}")



def binary_search(element, inputList):
    left = 0
    right = len(inputList) - 1
    inputList.sort()
    while left <= right:
        mid = (left + right) // 2
        if inputList[mid] == element:
            return mid
        elif inputList[mid] < element:
            left = mid + 1
        else:
            right = mid + 1
    return -1

for item in searchItems:
    print(f"Index of element {item} using Binary search: {linear_search(item, testList)}")

n = 1000
my_list = list(range(n))
element_to_find = 9999

start_time = time.time()
for _ in range(n):
    linear_search(element_to_find, my_list)
end_time = time.time()
linear_time = (end_time - start_time) / n

start_time = time.time()
for _ in range(n):
    binary_search(element_to_find, my_list)
end_time = time.time()
binary_time = (end_time - start_time) / n

print(f"Linear time: {linear_time}")
print(f"Binary time: {binary_time}")


"""
Q3
3. Explain the tuple and list differences ?
"""
"""
Answer:
They're both used to store a collection of objects
Tuple:      are immutable
            is defined by parentheses/round brackets, '()'
List:       are mutable
            defined by square brackets, '[]'
"""



"""
Q4
4. Create Your own iterator and generator
   write a class Sentence which takes a sentence string
   
   example: 
       sentence_obj=Sentence('this is SkillBuild session')
	   for word in sentence_obj:
			print(word)
			
	   #this should print the following output
	   # this
	   # is
	   # SkillBuild
	   # session
"""
print("\nQ4")
class Sentence():
    def __init__(self, sentence):
        self.sentence = sentence

    def print(self):
        split_sentence = self.sentence.split(" ")
        for word in split_sentence:
            print(word)

sentence_obj = Sentence('this is SkillBuild session')
sentence_obj.print()


"""
Q5
5. write a program for printing the pattern shown below for given n
   ex: 
   input: n=5
   output:
		   *
		   **
		   ***
		   ****
		   *****
"""
print("\nQ5")
def printStarTree(n):
    for i in range(1, n+1):
        print("*" * i)
        # if i != n:
        #     print("\n")

printStarTree(5)
printStarTree(10)


"""
Q6
6. Write the list comprehensions for finding the multiples of 3 for numbers starting from 100 to 1000
"""
print("\nQ6")
def findMultiples(n=3, startN=100, endN=1000):
    startI = startN // n
    if startN % n != 0:
        startI += 1
    endI = endN // n + 1
    return [n * i for i in range(startI, endI)]

print(findMultiples())
print(findMultiples(n=5))
print(findMultiples(n=6))
print(findMultiples(n=10))


"""
Q7
7.what is difference between iterators and generators
"""
"""
Iterator:   an object that can be iterated upon
            represents a stream of data
            contain a countable number of values
Generator:  a special type of function which does not return a single value
            it returns an iterator object with a sequence of values
"""




"""
Q8
8.write a program to tokenize string i.e., using split function see what is the output(data type) of spliting the sentence.
"""
print("\nQ8")
def tokenizer(sentence):
    split_sentence = sentence.split()
    print(type(split_sentence[0]))

tokenizer("Test sentence")


"""
Q9
9.swap two integers with out third variable, see how you can leverage tuples in doing it.
"""
print("\nQ9")

from enum import Enum

class SwapMethod(Enum):
    TupleUnpacking = 0
    Arithmetic = 1
    XOROperator = 2

class Variables:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def swapVariables(self, method):
        a, b = self.a, self.b
        match method:
            case SwapMethod.TupleUnpacking:
                a, b = b, a
            case SwapMethod.Arithmetic:
                a = a + b
                b = a - b
                a = a - b
            case SwapMethod.XOROperator:
                a = a ^ b
                b = a ^ b
                a = a ^ b
        return (a, b)


vars = Variables(5, 8)
print(vars.swapVariables(SwapMethod.TupleUnpacking))
print(vars.swapVariables(SwapMethod.Arithmetic))
print(vars.swapVariables(SwapMethod.XOROperator))
