# -*- coding, utf-8 -*-
"""
Created on Mon Jun 25 16,32,12 2018

@author, Ragini
"""

# Week 1, Class 1 Qns to do

#Qn 1, Fizzbuzz Qns

def fizzbuzz():
    new_list = []
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            new_list.append("Fizzbuzz")
        elif i%3 == 0:
            new_list.append("Fizz")
        elif i%5 == 0:
            new_list.append("Buzz")
        else:
            new_list.append(i)
    return new_list
fizzbuzz()

#Qn 2, Integer to Roman Numerals

#Create a reference table for the roman numerals against the integers 
roman_numeral_table = [("M", 1000), ("CM", 900),  ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), 
                       ("L", 50),  ("LC", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

def int_to_roman(inp_num):
    final_num = ""
    
    #check if inp_num is negative
    if inp_num <=0:
        raise ValueError("Your number is negative")
        # ("Your number is invalid")
    
    for letter,value in roman_numeral_table:
        while value <= inp_num:
            inp_num -= value
            final_num += letter
            #print(final_num)
    return final_num
int_to_roman(37120)
    
#Qn 3, Caesar Cipher
def get_value_for_char(inp_msg):
    
    final_str = ""
    mesg = inp_msg.replace(" ", "")
    for char in mesg:
        
        char_num = ord(char)
        char_num += 13
        
        if char_num >= 123:
            residue = -(123 - char_num)
            char_num = 97 + residue    
            
        #final_list.append(chr(char_num))
        final_str += chr(char_num)
    return final_str
        
get_value_for_char("hello world")
 