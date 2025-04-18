import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqlconnector://root:root@localhost/ipl")

# URL of the page containing Orange Cap winners list
url = 'https://www.timesofsports.com/cricket/ipl/orange-cap-winners-list/'

# Send a request to fetch the content of the page
page = requests.get(url=url)

# Parse the page content using BeautifulSoup
soap = BeautifulSoup(page.text, 'html.parser')

# Initialize an empty DataFrame with the required columns
df = pd.DataFrame(columns=['Year', 'Winners', 'Runs', 'Team'])

# Find the table body containing the data
tbody = soap.find('tbody')

# Extract each row from the table (excluding the header row)
tr = tbody.find_all('tr')[1:18]

# Loop through each row and extract the data
for i in tr:
    row_data = i.find_all('td')  # Find all <td> tags (table data)
    data = [i.text.strip() for i in row_data]  # Clean up the text data
    length = len(df)  # Get the current length of the DataFrame
    df.loc[length] = data  # Append the row data to the DataFrame

# Convert 'Year' and 'Runs' columns to integers
df[['Year', 'Runs']] = df[['Year', 'Runs']].astype(int)

# Save the resulting DataFrame to a CSV file
df.to_sql('orangecap',con=engine,if_exists='replace',index=False)

# Display the DataFrame (optional