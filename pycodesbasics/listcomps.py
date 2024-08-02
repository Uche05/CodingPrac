#Syntax for list comprehension: new = [expression for item in original_list if coniditon_is_meet]

'''List Comprehension to create a new list of doubled elements, a. from an original list, b. a preset of doubled numbers'''
#A
num= [1,2,3,4,5,6]
d_num = [num *2 for num in num]#creates list of doubles of inital list, 'num'
d_num

#B
d_num_2 = [d_num_2*2 for d_num_2 in range(1,20)]#creates a new list of doubles of the numbers from 1-19

'''List comprehension to create a filter for even numbers'''
e_num = [e_num for e_num in range(1,44) if e_num%2==0]

'''Usinng if-else statements'''
eo_list = ['even' if i%2==0 else 'odd' for i in num]

#Using re and list comprehension
import re

#Counting spaces

def count_space(s):
    return sum([1 for char in s if char.isspace()])


#using re and double loop in list comprehension
import re


def rcount_space(s):
    return len([w for char in s for w in re.findall(r'\s',char)])
