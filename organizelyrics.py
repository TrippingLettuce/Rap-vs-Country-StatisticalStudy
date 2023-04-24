import pandas as pd 
import numpy as np 
import IPython

#Going to find total first to get columns and orgaize by first you know 100 words or something 
#Then oragize if rapper lyric fits the columns 

#Overall for all rappers
lyric_dict_all_rap = {}
#Go through and get stats for each of 100 rappers 100 dicts
#Create dict find it, then push to new row in a totally new csv
lyric_dict_rapper = {} 

rap_df = pd.read_csv('/home/lettuce/MyCode/pandasproject/Rap-vs-Country-StatisticalStudy/raper_name copy.csv')

#itterate through each row 
for x in range(1):
#Take lyric column
    lyrics = rap_df['Lyrics'][x]
    #itterate through each lyric group in the 2d Array
    for x in range(1):
        words = lyrics.lower().split()
        for word in words: 
            if word in lyric_dict_all_rap:
                lyric_dict_all_rap[word] += 1
            else:
                lyric_dict_all_rap[word] = 1

#print(lyric_dict_all_rap) 
    #Create a dictornary Key is word Value is count 
    # IF there is a new word apphend the dictonary
    # IF word exist then add 1 to value 


# Append the key-value pair to the dictionary
#my_dict[key] = value


#Sorting the dictonary 
sorted_word_count = sorted(lyric_dict_all_rap.items(), key=lambda item: item[1], reverse=True)
#for key, value in sorted_word_count[:100]:
    #print(f"{key}: {value}")

#Put in new data frame 
#Rows 
my_index = ['Total']
for x in range(len(rap_df)):
    my_index.append(rap_df['Rap Name'][x])

#Put in new data frame
#Columns
my_columns = []             #Go to top 500 words when we have more data
for key, value in sorted_word_count[:100]:
    my_columns.append(key)

#Fill in data with Nan
nan_array = np.empty((len(my_index), len(my_columns)))
nan_array[:] = np.NaN

#Filling in Total Row
total_list = []
for key, value in sorted_word_count[:100]:
    total_list.append(value)

#Create DF
final_rap_df = pd.DataFrame(nan_array,index=my_index,columns=my_columns) 
#Add total values

final_rap_df.loc["Total"] = total_list
#IPython.display.display(final_rap_df.head())

final_rap_df.to_csv("/home/lettuce/MyCode/pandasproject/Rap-vs-Country-StatisticalStudy/final_rap.csv",index=True)


# Now that we have our total CSV we can go rapper by rapper
