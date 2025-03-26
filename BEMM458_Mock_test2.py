#######################################################################################################################################################
#
# Name:
# SID:
# Exam Date:
# Module:
# Github link for this assignment:
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax,
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
import LinearRegression
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pdp
weekly_sales = [120, 85, 100, 90, 110, 95, 130]


# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.

# answer
# Given list of weekly sales
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Calculate the average sales
average_sales = sum(weekly_sales) / len(weekly_sales)
print(f"Average weekly sales: {average_sales:.2f} units\n")

# Iterate through the list and check each week's sales against the average
for week_number, sales in enumerate(weekly_sales, start=1):
    if sales > average_sales:
        print(f"Week {week_number}: Sales were above average ({sales} units).")
    elif sales < average_sales:
        print(f"Week {week_number}: Sales were below average ({sales} units).")
    else:
        print(f"Week {week_number}: Sales were exactly average ({sales} units).")

#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.

# answer
# Customer feedback string
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of 'good'
good_start = customer_feedback.find('good')
good_end = good_start + len('good') if good_start != -1 else None
good_positions = (good_start, good_end)

# Find the first and last occurrence of 'improved'
improved_start = customer_feedback.find('improved')
improved_end = improved_start + \
    len('improved') if improved_start != -1 else None
improved_positions = (improved_start, improved_end)

# Store positions as tuples in a list
positions_list = [good_positions, improved_positions]

# Print the list of tuples
print("Positions of 'good' and 'improved':", positions_list)

#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.

# answer
# Function to calculate Net Profit Margin


def net_profit_margin(profit, revenue):
    return (profit / revenue) * 100 if revenue != 0 else 0

# Function to calculate Customer Acquisition Cost (CAC)


def customer_acquisition_cost(marketing_cost, customers):
    return marketing_cost / customers if customers != 0 else 0

# Function to calculate Net Promoter Score (NPS)


def net_promoter_score(promoters, detractors, total):
    return ((promoters - detractors) / total) * 100 if total != 0 else 0

# Function to calculate Return on Investment (ROI)


def return_on_investment(gain, investment):
    return (gain / investment) * 100 if investment != 0 else 0


# Using student ID digits: 750011108
profit = 7500
revenue = 11108
marketing_cost = 1108
customers = 75
promoters = 50
detractors = 11
total_respondents = 108
gain = 7500
investment = 1108

# Print results
print("Net Profit Margin:", net_profit_margin(profit, revenue), "%")
print("Customer Acquisition Cost: £",
      customer_acquisition_cost(marketing_cost, customers))
print("Net Promoter Score:", net_promoter_score(
    promoters, detractors, total_respondents))
print("Return on Investment:", return_on_investment(gain, investment), "%")

# Net Profit Margin: 67.5 %
# Customer Acquisition Cost: £ 14.77
# Net Promoter Score: 36.11
# Return on Investment: 676.7 %

# 7500 → Net Profit

# 11108 → Revenue

# 1108 → Marketing Cost & Investment Cost

# 75 → New Customers

# 50 → Promoters

# 11 → Detractors

# 108 → Total Respondents
#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr',
                        'May'], 'Sales': [200, 220, 210, 240, 250]}

#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130

# answer

# Dataset
prices = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1,
                                                        1)  # Reshaped into 2D array
demand = np.array([200, 180, 170, 160, 150, 140, 130])

# Linear Regression Model
model = LinearRegression()
model.fit(prices, demand)  # Train the model

# Predict demand for price £26
price_to_predict = np.array([[26]])
predicted_demand = model.predict(price_to_predict)

# Print predicted demand
print(f"Predicted demand for price £26: {predicted_demand[0]:.2f} units")

# Visualization: Scatter plot and Regression line
plt.scatter(prices, demand, color='blue', label='Data Points')
plt.plot(prices, model.predict(prices), color='red', label='Regression Line')
plt.xlabel('Price (£)')
plt.ylabel('Demand (Units)')
plt.title('Linear Regression: Price vs Demand')
plt.legend()
plt.grid()
plt.show()

#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

# answer

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.

# answer
# Given list of order quantities
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to double quantities that are 10 or more
doubled_quantities = [quantity *
                      2 for quantity in quantities if quantity >= 10]
# same as
doubled_quantities = []
for quantity in quantities:
    if quantity >= 10:
        doubled_quantities.append(quantity * 2)


# Print the original and the new lists
print("Original Quantities:", quantities)
print("Doubled Quantities (10 or more):", doubled_quantities)


#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5,
           'product_C': 3, 'product_D': 2, 'product_E': 5}

# answer
# Original dictionary of ratings
ratings = {'product_A': 4, 'product_B': 5,
           'product_C': 3, 'product_D': 2, 'product_E': 5}

# Create a new dictionary with products having ratings >= 4
filtered_ratings = {product: rating for product,
                    rating in ratings.items() if rating >= 4}

# Print the new dictionary
print("Filtered Ratings:", filtered_ratings)

#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

# answer
# Original code with errors:
values = [10, 20, 30, 40, 50]
total = 0

# Calculate the sum of the values
# ERROR: The code doesn't calculate the total sum of the list 'values'. It simply initializes 'total' but never updates it.
# FIX: Use a loop or Python's built-in sum() function to calculate the total.

total = sum(values)  # Correctly summing the values

# Calculate the average
# ERROR: The average calculation is missing in the code.
# FIX: Divide 'total' by the number of elements in 'values' using len(values).

average = total / len(values)  # Correctly calculating the average

# Print the result
# ERROR: The code doesn't display the calculated average.
# FIX: Add a print statement to show the result.

print(f"The average of the list is: {average:.2f}")


#######################################################################################################################################################

print("This script is running...")
