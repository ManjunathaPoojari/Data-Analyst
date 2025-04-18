import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqlconnector://root:root@localhost/ipl")

# Define the URL of the page with IPL captain data
url = 'https://www.espncricinfo.com/records/trophy/individual-most-matches-as-captain/indian-premier-league-117'

# Send a GET request to fetch the HTML content of the page
page = requests.get(url=url)

# Parse the page using BeautifulSoup to extract data
soap = BeautifulSoup(page.text, 'html.parser')

# Find the table headers by searching for 'thead' and the first row ('tr')
thead = soap.find('thead')
trow = thead.find('tr')

# Extract and clean up header names from the 'td' elements
headers = [i.text.strip() for i in trow.find_all('td')]

# Create an empty DataFrame with the extracted headers
df = pd.DataFrame(columns=headers)

# Find the body of the table containing data rows
tbody = soap.find('tbody')
tr = tbody.find_all('tr')

# Loop through each row of the table and extract data
for i in tr:
    row_data = i.find_all('td')  # Extract each cell in the row
    data = [i.text.strip() for i in row_data]  # Clean the text and strip extra spaces
    length = len(df)  # Get the current length of the DataFrame
    df.loc[length] = data  # Add the extracted data as a new row to the DataFrame

# Extract 'Player' and 'Team' columns from the 'Player' column using regex
df[['Player', 'Team']] = df['Player'].str.extract(r'(.+)\s+\((.+)\)')

# Split the 'Span' column into 'Start Year' and 'End Year' and convert to integer type
df[['Start Year', 'End Year']] = df['Span'].str.split('-', expand=True).astype(int)

# Split the 'Team' column into three separate team columns
df[['Team1', 'Team2', 'Team3']] = df['Team'].str.split('/', expand=True)

# Convert numeric columns into integers
df[['Start Year', 'End Year', 'Mat', 'Won', 'Lost', 'Tied', 'Draw', 'NR']] = df[['Start Year', 'End Year', 'Mat', 'Won', 'Lost', 'Tied', 'Draw', 'NR']].astype(int)

# Calculate percentage columns for 'Won', 'Lost', 'Tied', and 'NR'
df['Won%'] = round((df['Won'] / df['Mat']) * 100, 2).astype(float)
df['Lost%'] = round((df['Lost'] / df['Mat']) * 100, 2).astype(float)
df['Tied%'] = round((df['Tied'] / df['Mat']) * 100, 2).astype(float)
df['NR%'] = round((df['NR'] / df['Mat']) * 100, 2).astype(float)

# Reorganize columns and select relevant ones for the final DataFrame
df = df[['Player', 'Start Year', 'End Year', 'Mat', 'Won', 'Won%', 'Lost', 'Lost%', 'Tied', 'Tied%', 'NR', 'NR%']]

# Save the final DataFrame as a CSV file
df.to_sql('captains',con=engine,if_exists='replace',index=False)
