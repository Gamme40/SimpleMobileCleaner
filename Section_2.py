# -*- coding: utf-8 -*-
"""Section 2 of Practical Assessment for Python

Simple Mobile Number Cleaner Function

"""
__version__ = '1.0'
__author__  = 'Amith Philip'


def number_Clean(var_Num):
    """Clean and return a valid number."""
    
    # Remove the non-numeric values from the string
    num_Filter= filter(str.isdigit, var_Num)
    
    # Reform the string after filtering
    num_Clean = "".join(num_Filter)
    
    # Check for and add the leading 0 if it is missing
    if num_Clean[0] != '0':
        num_Clean = "0" + num_Clean
        
    # Check the length of the String
    error = 'The number is not valid.'
            
    if len(num_Clean) != 10:
        return error

    # Return the cleaned number
    return num_Clean

