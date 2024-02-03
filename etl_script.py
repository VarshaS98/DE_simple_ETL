# Import necessary libraries
import requests              # Library for making HTTP requests
import pandas as pd          # Library for data manipulation and analysis
from sqlalchemy import create_engine  # Library for interacting with databases using SQL

# Define the extract function to fetch data from the Universities API
def extract() -> dict:
    """ This API extracts data from
    http://universities.hipolabs.com
    """
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    
    # Make an HTTP GET request to the API and retrieve data in JSON format
    data = requests.get(API_URL).json()
    
    # Return the extracted data
    return data

# Define the transform function to process and filter the data
def transform(data: dict) -> pd.DataFrame:
    """ Transforms the dataset into the desired structure and filters"""
    
    # Convert the extracted JSON data into a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Print the total number of universities from the API
    print(f"Total Number of universities from API {len(data)}")
    
    # Filter the DataFrame to include only universities in California
    df = df[df["name"].str.contains("California")]
    
    # Print the number of universities in California
    print(f"Number of universities in California {len(df)}")
    
    # Modify 'domains' and 'web_pages' columns to contain comma-separated strings
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
    
    # Reset the DataFrame index
    df = df.reset_index(drop=True)
    
    # Return a subset of columns: 'domains', 'country', 'web_pages', and 'name'
    return df[["domains", "country", "web_pages", "name"]]

# Define the load function to store data in an SQLite database
def load(df: pd.DataFrame) -> None:
    """ Loads data into a sqllite database"""
    
    # Create an SQLite engine and connect to the database file 'my_lite_store.db'
    disk_engine = create_engine('sqlite:///my_lite_store.db')
    
    # Load the DataFrame into the 'cal_uni' table in the SQLite database
    # If the table already exists, replace it
    df.to_sql('cal_uni', disk_engine, if_exists='replace')

# Execute the ETL process
data = extract()  # Extract data from the API
df = transform(data)  # Transform the extracted data
load(df)  # Load the transformed data into an SQLite database
