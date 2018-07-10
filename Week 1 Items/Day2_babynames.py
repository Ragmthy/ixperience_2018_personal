# -*- coding: utf-8 -*-
"""
In this example we are going to build an application that reads the most popular names
in the US, taken from the Social Security Administration's site:

https://www.ssa.gov/oact/babynames/

This application will have the following functionalities:

- It will accept a name as an argument
- It will read a list of files (located in the folder data). Each file contains the
most popular baby names for boys and girls for a certain year (the year is in the filename)
- For the name provided as an argument, print out how many years it's been among the most popular among boys and girls
"""

#Week 2, Qn 2 (Check on the Baby Names)

#This is going to help me collect all the popular names in the files it reads
#initialise a list


#%%
  
#Week 2, Qn 2 (Pull out baby names in the text file)

from collections import Counter

def extract_pop_names():
    top_boy_names = []
    top_girl_names = []
    
    #Range function to actually start with a start year and an end year
    years = range(1900,2017)
    
    #make a for loop for year number, read the text_file for this year, pull out the first line
    for year in years:
        with open("data/names_{}.txt".format(year)) as f:
            first_line = f.readline().rstrip("\n")
            
            top_boy_names.append((first_line.split('|')[1]))
            top_girl_names.append((first_line.split('|')[2]))
           
            
    #make the names dictionary
    boy_dict = Counter(top_boy_names)
    girl_dict = Counter(top_girl_names)
    
    print(boy_dict) 
    print(girl_dict)
    
    #take in a name from the user    
    user_name = input("Enter the name you want to check  :")
    if user_name.capitalize() in boy_dict:
        return("This name was most popular {} times from 1900- 2017".format(boy_dict[user_name.capitalize()]))
    elif user_name.capitalize() in girl_dict:
        return("This name was most popular {} times from 1900- 2017".format(girl_dict[user_name.capitalize()]))
    elif user_name.capitalize() not in (boy_dict and girl_dict):
        return("This name not a part of our database")
    
extract_pop_names()
