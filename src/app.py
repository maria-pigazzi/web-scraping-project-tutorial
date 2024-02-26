import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
from bs4 import BeautifulSoup


# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
import requests
req = requests.get('https://vaz.io/tesla')
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
con = 
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function
# find table among all tables
# print the numbers in the table as dataframe
# look in beautiful soup how to do it