import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqlconnector://root:root@localhost/ipl")

# Define the URL to scrape data from
url = 'https://www.espncricinfo.com/records/trophy/batting-list-hundreds/indian-premier-league-117'

# Send a GET request to the URL
page = requests.get(url=url)

# Parse the HTML content using BeautifulSoup
soap = BeautifulSoup(page.text, 'html.parser')

# Extract headers from the table
thead = soap.find('thead')
trow = thead.find('tr')
headers = [i.text.strip() for i in trow.find_all('td')]

# Initialize a DataFrame with the extracted headers
df = pd.DataFrame(columns=headers)

# Extract data rows from the table body
tbody = soap.find('tbody')
tr = tbody.find_all('tr')
for i in tr:
    row_data = i.find_all('td')
    data = [i.text.strip() for i in row_data]
    length = len(df)
    df.loc[length] = data

# Extract player and team details from the 'Player' column
df[['Player', 'Team']] = df['Player'].str.extract(r'(.+)\s+\((.+)\)')

# Drop the redundant 'team' column
df = df.drop('team', axis=1)

# Reorganize the columns for clarity
df = df[['Player', 'Runs', 'HS', 'Balls', '4s', '6s', 'SR', 'Team', 'Opposition', 'Ground', 'Match Date']]

# Clean the 'HS' column to remove the '*' symbol
df['HS'] = df['HS'].str.replace('*', '')

# Convert the 'SR' column to float type for proper calculations
df[['SR']] = df[['SR']].astype(float)

# Convert the 'Match Date' column to datetime format for easier manipulation
df['Match Date'] = pd.to_datetime(df['Match Date'])

# Convert relevant columns to integers for proper analysis
df[['Runs', 'HS', 'Balls', '4s', '6s']] = df[['Runs', 'HS', 'Balls', '4s', '6s']].astype(int)

# Save the cleaned data to a CSV file
df.to_sql('list_of_100s',con=engine,if_exists='replace',index=False)
