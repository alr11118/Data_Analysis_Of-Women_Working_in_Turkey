# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

print("What might increase the percentage of working women?")
print("This question is important because it can infulence newer solituons to lower working women rates")
print("The data shows a slight decline in the percentage of working women in Turkey untill 2008. Then the percentage of working women in Turkey increases steeply. Implying that something in 2008 caused this positive trend")
input("Press return to continue.\n")

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Choose one country
oneCountryBooleanList = lwd["country_name"] == "Turkey"
oneCountryData = lwd.loc[oneCountryBooleanList]

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(oneCountryData["year"], oneCountryData["WK_working_p"], color="red")

# add a title to the plot
plt.title("Percent of Women currently working over Time")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women currently working (%)")

# set the range for the y-axis
plt.ylim(0,100)
plt.xlim(2002,2014)

# show the plot
plt.show()
