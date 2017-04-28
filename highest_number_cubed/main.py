"""This is the entry point of the program."""

def highest_number_cubed(limit):
    previous_number = 1 
    
    while True:
        current_number = previous_number + 1
        if current_number ** 3 > limit:
            return previous_number

        previous_number = current_number

#Altermative Answer
'''
    number = 0
    
    while True:
        number += 1
        if number ** 3 > limit:
            return number -1
'''

'''
Use the cubed root logic: (number ** (1/3)
'''
