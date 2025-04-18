import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqlconnector://root:root@localhost/ipl")
# Initialize an empty list to store DataFrames for each year
all = []

# List of identifiers for each year's points table page and the corresponding year range
number = [59, 60, 61, 62, 63, 13, 10123, 10656, 10741, 10742, 11236, 11181, 11190, 11419, 11709, 11847, 12052]
year_list = range(2008, 2025)  # Year range from 2008 to 2024

# Loop over the 'number' and 'year_list' simultaneously to scrape data for each year
for i, year in zip(number, year_list):
    # Construct the URL for the points table of the current year using the identifier 'i' and the 'year'
    uri = f"https://www.cricketwa.com/pointstable/{i}/ipl-{year}-points-table.aspx"
    
    # Send an HTTP request to fetch the page content
    page = requests.get(url=uri)
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Find the first table on the page which contains the points table data
    table = soup.find_all('table')[0]
    
    # Extract all rows from the table
    rows = table.find_all('tr')
    
    # Initialize an empty DataFrame with appropriate column names for the points table
    df = pd.DataFrame(columns=['Team', 'Matches', 'Won', 'Lost', 'Tied', 'NR', 'NRR', 'Points'])
    
    # Loop through each row and extract the data
    for row in rows:
        row_data = row.find_all('td')  # Get all table data cells in the row
        data = [cell.text.strip() for cell in row_data]  # Clean up the text by stripping extra whitespace
        
        # If data is found, append it as a new row in the DataFrame
        if len(data) > 0:
            df.loc[len(df)] = data  # Add the row to the DataFrame
    
    # Add a 'Year' column to the DataFrame for the current year
    df['Year'] = f"{year}"
    
    # Append the DataFrame for this year to the 'all' list
    all.append(df)

# Concatenate all the DataFrames in the 'all' list into a single DataFrame
data = pd.concat(all)

# Save the final DataFrame to a CSV file
df.to_sql('points_table',con=engine,if_exists='replace',index=False)
