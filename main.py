import os
import pandas as pd 
import numpy as np 
from lyricsgenius import Genius
from dotenv import load_dotenv
import funkyFunctions

load_dotenv()  # Load environment variables from the .env file

genius_key = os.getenv('GENUIS_KEY')
genius = Genius(genius_key,timeout=15)
genius.verbose = False
genius.remove_section_headers = True
genius.excluded_terms = ["(Remix)", "(Live)"]


csv = pd.read_csv('/home/lettuce/MyCode/pandasproject/Rap-vs-Country-StatisticalStudy/raper_name copy 2.csv')
#csv = pd.read_csv('/home/lettuce/MyCode/pandasproject/Rap-vs-Country-StatisticalStudy/raper_name copy.csv')
#csv = pd.read_csv('/home/lettuce/MyCode/pandasproject/testmaybe.csv')
csv_rap_final = pd.read_csv('/home/lettuce/MyCode/pandasproject/Rap-vs-Country-StatisticalStudy/final_rap.csv')
#Get data 
csv = funkyFunctions.getData(csv)
#Clean Data 
csv = funkyFunctions.cleanData(csv)
#Organize Data
funkyFunctions.organizeDataTotal(csv)
#Orgaize Data Artist
funkyFunctions.organizeDataArtist(csv, csv_rap_final)
#Anaylize Data




# Take 50 top hip hop and 50 top rap combo

#TOp 100 country

#raper_df = pd.read_csv('/home/lettuce/MyCode/pandasproject/raper_name.csv')

#print(raper_df.head().to_string())