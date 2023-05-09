# Write a Python program that takes a list of strings as input and outputs
# the number of times each string appears in the list, 
# using a dictionary and conditional statements.


def count_strings(list):
    frequency = {}
    for string in list:
        if string in frequency:
            frequency[string] += 1
        else:
            frequency[string] = 1
    return frequency

strings = ["orange", "banana", "apple", "kiwi"]
frequency = count_strings(strings)
print(frequency)


# Write a Python program that takes a list of numbers as input and outputs the median of the numbers 

def  median(numbers):

   for x in numbers:
      return x.median
      numbers=[20,10,12,43]

   print(median(numbers))





#  Write a Python program that takes a list of numbers as input
#  and outputs the second largest number in the list using conditional statements and a for loop.



def find_second_largest(numbers):
    sorted_list = sorted(numbers[::-1])
    return sorted_list[1]

print(find_second_largest([43, 76, 50]))



# Write a Python program that takes a year as input and determines if it is a leap year.

year=int(2021)
if year%4==0:
   print(year ,"is a leap year")
else:
   print(year, "is not a leap year")
# Write a Python program that takes a string as input and checks if it
# is a palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.

def palindrome(string):

   return string==string[::-1]
string="mum" 
result=palindrome("mum")
if result:
   print("true")
else:
   print("false")   