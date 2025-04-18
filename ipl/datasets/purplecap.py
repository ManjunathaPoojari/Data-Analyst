# Import necessary libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
import pandas as pd  # For handling data in DataFrame format
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqlconnector://root:root@localhost/ipl")

# Define the URL of the page to scrape
url = 'https://www.crictracker.com/list-of-purple-cap-winners-in-ipl/'

# Make a GET request to fetch the webpage content
page = requests.get(url=url)

# Parse the HTML content of the page using BeautifulSoup
soap = BeautifulSoup(page.text, 'html.parser')

# Initialize an empty DataFrame with column names: Year, Winner, Team, Wickets
df = pd.DataFrame(columns=['Year', 'Winner', 'Team', 'Wickets'])

# Find the <tbody> tag, which contains the data in rows
tbody = soap.find('tbody')

# Get all the rows of data in the table, excluding the first header row (hence [1:18])
tr = tbody.find_all('tr')[1:18]

# Loop through each row (tr) to extract the data
for i in tr:
    # Find all the <td> elements within the row (this contains the data we need)
    row_data = i.find_all('td')
    
    # Extract and clean the text from each <td> element by stripping leading/trailing spaces
    data = [i.text.strip() for i in row_data]
    
    # Append the cleaned data to the DataFrame
    length = len(df)  # Get the current length of the DataFrame
    df.loc[length] = data  # Add the new row to the DataFrame

# Save the DataFrame to a CSV file in the specified location (ipl\purplecap.csv)
df.to_sql('purplecap',con=engine,if_exists='replace',index=False)  # Don't include the index in the CSV
