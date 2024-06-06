

# Session 2 - Testing Assignment


#================================================
# 1. Write unit test cases for below function convert_temperature()
#
# Expected test cases:
#   def test_invalid(self):
#       """
#       There's no such temperature as -280 C, so convert_temperature should
#       raise a ValueError.
#       """
#
#   def test_valid(self):
#       """ A series of valid temperature conversions to test. """
#
#   def test_no_conversion(self):
#       """
#       Ensure that if the from-units and to-units are the same the
#       temperature is returned exactly as it was passed and not converted
#       to and from Kelvin, which may cause loss of precision.
#       """
#
#   def test_bad_units(self):
#       """ Check that ValueError is raised if invalid units are passed. """
#================================================

def convert_temperature(value, from_unit, to_unit):
    """ Convert a temperature between the units Fahrenheit, Celsius and Kelvin (identified by the characters 'F', 'C' and 'K' respectively).
    Return the temperature value from from_unit to to_unit. """

    # Dictionary of conversion functions from different units *to* K
    toK = {'K': lambda val: val,
           'C': lambda val: val + 273.15,
           'F': lambda val: (val + 459.67)*5/9,
           }
    # Dictionary of conversion functions *from* K to different units
    fromK = {'K': lambda val: val,
             'C': lambda val: val - 273.15,
             'F': lambda val: val*9/5 - 459.67,
             }

    # First convert the temperature from from_unit to K
    try:
        T = toK[from_unit](value)
    except KeyError:
        raise ValueError('Unrecognised temperature unit: {}'.format(from_unit))

    if T < 0:
        raise ValueError('Invalid temperature: {} {} is less than 0 K'
                         .format(value, from_unit))

    if from_unit == to_unit:
        # No conversion needed!
        return value

    # Now convert it from K to to_unit and return its value
    try:
        return fromK[to_unit](T)
    except KeyError:
        raise ValueError('Unrecognised temperature unit: {}'.format(to_unit))


#================================================
# 2. Write unit test case for below python-twitter api using mock library
#
# Let's assume you have a script that interacts with an external API and makes calls to that API whenever a certain function is called.
# In this example, we are going to use the Twitter API to implement a Python script which will post to the Twitter profile page.
# We don't want to post messages on Twitter every time we test the script
#
# Please install python twitter library
# pip install python-twitter
#================================================

import twitter

# define authentication credentials
consumer_key        = 'iYD2sKY4NC8teRb9BUM8UguRa'
consumer_secret     = 'uW3tHdH6UAqlxA7yxmcr8FSMSzQIBIpcC4NNS7jrvkxREdJ15m'
access_token_key    = '314746354-Ucq36TRDnfGAxpOVtnK1qZxMfRKzFHFhyRqzNpTx7wZ1qHS0qycy0aNjoMDpKhcfzuLm6uAbhB2LilxZzST8w'
access_token_secret = '7wZ1qHS0qycy0aNjoMDpKhcfzuLm6uAbhB2LilxZzST8w'


def post_tweet(api, tweet):
    # post tweet
    status = api.PostUpdate(tweet)
    return status


def main():
    api = twitter.Api(consumer_key        = consumer_key,
                      consumer_secret     = consumer_secret,
                      access_token_key    = access_token_key,
                      access_token_secret = access_token_secret)

    message = input("Enter your tweet :")

    post_tweet(api, message)



# 3. Problem Statement
#    Let's say we want student to call a builtin function in order to solve a problem.
#    We may want to change the behaviour of the builtin function while testing student's code.
#
#    Let's say the question is to read a file, file_exercise_3.txt , from disk and parse it.
#    The file contains "first_name | last_name | birthdate" in each line.
#
#    Students will implement a function named parse() and this will return a list of first names.
#    An example way to solve this problem is given below
#
#  ToDo:
#  In the test file, mock the builtin open() function to test different behaviours.
#
#  - test_parse_single_line
#       -> Assert readlines() is called only once
#       -> Assert output if file contains only one line
#
# - test_parse_multiple_line
#       -> Assert readlines() is called only once
#       -> Assert output if file contains multiple lines
#================================================


#================================================
4. Problem Statement: Write unit test case for get_full_name() by mocking get_first_name() & get_last_name() function calls
#================================================

class Customer:
    def get_full_name(self):
        # This is the function to be edited by the students
        return self.get_first_name() + " " + self.get_last_name()

    def get_first_name(self):
        # This is provided by the instructor
        return "Arya"

    def get_last_name(self):
        # This is provided by the instructor
        return "Stark"

#================================================


# Session 4 - RegEx Assignment

# 1. Write a Python program to check that a string contains
#    only a certain set of characters (in this case a-z, A-Z and 0-9).
#    e.g. Sample2021 - should return true | Sample_Data@2021 - should return false



# 2. Write a Python program to find sequences of lowercase
#    letters joined with a underscore.
#    e.g. aaa_bbb - should return true | aaa_BBB - should return false | aaa_123 - should return false


# 3. Write a Python program to remove leading zeros from
#    an IP address
#    e.g. input - 216.08.094.196
#         output - 216.8.94.196



# 4.Write a Python program to find and print numbers
#   and their position of a given string.
#   input string - "The following example creates an List with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#   expected output -
#       50
#       Index position: 57
#       4
#       Index position: 70



# 5. Write a Python program to remove all whitespaces from a string.
#    e.g input string - ' Python    Exercises '
#    expected output  - ' PythonExercises'


