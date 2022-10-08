####################################################################################################
# This program will use a CSV data file, pandas, and matplotlib to allow a user to learn about the 
# change in popularity of different names over time, between 1960 and 2009.
####################################################################################################

import matplotlib.pyplot as plt
import pandas as pd

# create a list of the names to be included in the graph and stats
graph_names = ["Ronald", "Rodney", "Paula", "Gina", "Brandon", "Evan", "Brianna", "Emily"]

# read and store the data from the csv file
df = pd.read_csv("names_data.csv", header=0)

###### Functions ######
# display the data for 8 chosen names over time
def stats():
  for name in graph_names:
    # find the year and value data corresponding to the 8 chosen names, grouping by year
    name_values = df[df['name'] == name].groupby('year')['number']

    # display that data
    print(name, name_values.sum())
    print("\n")

# display the data for the 8 chosen names in graph form
def graph():
  for name in graph_names:
    # get the years and corresponding values for each of the 8 names
    name_values = (df[df['name'] == name].groupby('year')['number']).sum()
    
    # add the points to a line graph
    plt.plot(name_values, label=name, linestyle="--", marker="*")
  
  # format and show the graph
  plt.ylabel('Number of Newborns with Name')
  plt.xlabel('Year')
  plt.title('Popularity of Different Baby Names Over Time')
  plt.legend()
  plt.show()

# allow the user to search for data on a specific name
def search(name):
  names = []
  max_value = 0
  max_year = 0
  names.append(name)

  # filter the data to only include that for the searched name & group by year
  for n in names:
    search_values = (df[df['name'] == n].groupby('year')['number']).sum()
    print(search_values)
    
    # iterate through the rows of that array to determine the max_value for that name
    for row in search_values:
      number_index = 1
      year_index = 0
      if (int(row) > max_value):
        max_value = (row)
  
  # display results
  print("In its height of popularity in this time period, the name " + name + " was given to " + str(max_value) + " newborns.")
  print("\n")

###### Run Statements ######
end = 0
while end == 0:
  # print directions
  print("This program is designed to allow you to observe and explore statistics about the popularity of" + "\n" + "different baby names between 1960 and 2009. Here are your options:")
  print("1. Type 'stats' to see statistics on 8 different baby names over time" + "\n" + "2. Type'graph' to see a graph of the data for these 8 names" + "\n" + "3. Type 'search' to find the year when a specific name was most popular" + "\n" + "4. Type 'quit' to end the program." + "\n")
  choice = input("Your choice: ")
  print("\n")

  # evaluate user input and run the corresponding function
  if choice == "stats":
    stats()
  if choice == "graph":
    graph()
  if choice == "search":
    name = input("What name would you like to search for? ")
    search(name)


  # if the user types quit, end the iteration to stop the code run
  if choice == "quit":
    end = 1