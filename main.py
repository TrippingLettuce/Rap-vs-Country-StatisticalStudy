import os
import pandas as pd 
import numpy as np 
from lyricsgenius import Genius
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file


genius_key = os.getenv('GENUIS_KEY')
genius = Genius(genius_key,timeout=15)

print(genius)

rap_df = pd.read_csv('/home/lettuce/MyCode/pandasproject/Rap-vs-Country-StatisticalStudy/raper_name copy 2.csv')
print(rap_df.loc[0][0])

genius.verbose = False
genius.remove_section_headers = True
genius.excluded_terms = ["(Remix)", "(Live)"]



rap_df['Songs'] = np.nan
rap_df['Lyrics'] = np.nan

print(rap_df.head())

for x in range(11):
    
    artist_name = rap_df.loc[x][0]
    print(artist_name)
    artist = genius.search_artist(artist_name, max_songs=2, sort="popularity")

    song_list = []
    song_lyrics_list = []

    # Iterate over the songs and add them to the list
    for song in artist.songs:
        print(song.title)
        song_list.append(song.title) 

    rap_df['Songs'][x] = song_list

    for song in song_list:
        lyrics = genius.search_song(artist_name,song)
        song_lyrics_list.append(lyrics.lyrics)
    rap_df['Lyrics'][x] = song_lyrics_list


rap_df.to_csv('/home/lettuce/MyCode/pandasproject/Rap-vs-Country-StatisticalStudy/raper_name copy.csv',index=False)

print(rap_df.head())

# Take 50 top hip hop and 50 top rap combo

#TOp 100 country

#raper_df = pd.read_csv('/home/lettuce/MyCode/pandasproject/raper_name.csv')

#print(raper_df.head().to_string())