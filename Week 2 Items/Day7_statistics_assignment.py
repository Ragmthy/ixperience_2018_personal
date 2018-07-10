# -*- coding: utf-8 -*-
"""
Statistics Assignment: Apartment Search tool

This assignment will help us solidify what we have learned so far about data 
manipulation and statistics

Using the Airbnb dataset (located in data/airbnb.csv), we are going to make a script
with the following functionalities:
*******************************************************************************
Functionality 1: Neighbourhood information
- Given a neighbourhood, the tool will provide the following information to the user
  - Total number of available listings in the neighbourhood
  - Number of rooms broken down per listing type
  - Average Room Price
  - Price quartiles

For example if we run the script like;

"python statistics_assignment.py information Belém"

The script will print out information about Belem.

*******************************************************************************
Functionality 2: Apartment Search.
This functionality will help the user to find an appropriate listing. It will ask
the user different listing requirements:
- desired price range
- desired number of rooms (a range)
- a list of desired neighbourhoods
If the user doesnt specifiy any of the requirements (pressing enter without typing anything)
We will consider that the user is indiferent

It will also ask the user if he/she prefers the results sorted by price, by average score
or by number of reviews.

Finally the script will print out the top 10 results matching the desired requirements and sorted
by the desired sorting criteria.

If there are no listings that match the criteria, the script will tell the user that no
listings match the criteria.

For example if we run

"python statistics_assignment.py search"

The script will start prompting us for the requirements and finally print out the results
*******************************************************************************

There should be a main() function that serves as an entrypoint.

When we load the script it will load the dataset and it will be used as the data source.
"""

import pandas as pd
import sys

def load_data():
    bnbs = pd.read_csv(r"C:\Users\Ragini\Desktop\iX Portugal\Data Science\Classes\Week2\Day 7\statistics\data\airbnb.csv", encoding = "Latin-1")
    return bnbs

def information(bnbs, neighbourhood):
    bnbs = load_data()
    neigh_data = bnbs[bnbs.neighborhood == neighbourhood]
    
    #num of rooms by listing
    room_type_count = neigh_data["room_type"].value_counts()
    
    #average room price
    average_price = neigh_data['price'].describe()['mean']
    
    #price quartiles
    first_quartile = neigh_data['price'].describe()['25%']

    neigh_info = neigh_data['price'].describe()
    return('Information for {}:\nTotal number of available listings: {}\nBy type\nEntire home/apt: {}\nPrivate room: {}\nShared room: {}\nAverage room price: {}\nPrice Quartiles\n25%: {}\n50%: {}\n75%: {}'.format(
        neighborhood, neigh_info['count'], room_type_count[0], room_type_count[1], room_type_count[2], round(average_price, 2), neigh_info['25%'], neigh_info['50%'], neigh_info['75%']))

def search():
    
    bnbs = load_data()
    
    #Check user's price range    
    price_min = int(input("Enter the minimum price for a bnb: "))
    price_max = int(input("Enter the maximum price for a bnb: "))
    
    price_range = price_max - price_min
    
    if price_range > 0:
        bnbs = bnbs[(bnbs.price >= price_min) & (bnbs.price <= price_max)]
    else:
        print("You have entered an invalid price numbers")
    
    #Check user's number of rooms
    min_room = float(int(input("Enter the minimum number of rooms you want in your accomodation")))
    max_room = float(int(input("Enter the maximum number of rooms you want in your accomodation")))
    
    
    #Check for accomodation
    room_df = bnbs[(bnbs.bedrooms>=min_room) & (bnbs.bedrooms<=max_room)]
        
        
    #Check user's list of desired neighbourhoods
    user_regions = input("Enter the regions you want to check accomodation in like this: Alvalade,Santa Mario Maior,Estrela).")
    if not user_regions == "":
        region_list = user_region.split(',')
        bnbs = bnbs.set_index('neighborhood', drop=False).loc[region_list]
        
    #Ask user how to organize the content
    order = int(input("Enter 1 if you want the options ordered by price, 2 by average score, 3 by reviews. --> "))
    if order == 1:
        bnbs = bnbs.sort("price", ascending = True)
    elif order == 2:
        bnbs = bnbs.sort("overall_satisfaction", ascending = False)
    elif order == 3:    
        bnbs = bnbs.sort("reviews", ascending=False)
    print(bnbs.head(10).to_string())
    
    
def parse_arguments():
    arguments = sys.argv[1:]
    region = ""
    if arguments[0] == "information":
        for name in arguments[1:-1]:
            region += name + " "
        region += arguments[-1]
        arguments[1] = region
    return arguments
    

def main(arguments):
    bnbs = load_data()
    if arguments[0] == "informaion":
        print(information(arguments[1]))
        
if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
