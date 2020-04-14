#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from geopy import distance #caculate distances
from geopy import point #create points based of floating point lat & long and points based on string (N,S,E,W) 
df = pd.read_csv("location-data.txt")


# In[2]:


dis_list = [] #list to store the distances 
dis_index_list = [] #list to store the indexs of the distances
loc1 = (0,0)


# In[3]:


for i in range(len(df)): #loop throught data frame and compute the distances from the origin(loc1) to the specified location
    lat = df.at[i, 'Latitude'] #grab the latitude from the index i in the dataframe
    longi = df.at[i, 'Longitude'] #grab the longitude from the index i in the dataframe
    try:
        pt = point.Point(lat + ',' + longi) #create a single point from the latitudes and longitudes
        dis_list.append(distance.distance(loc1, pt)) #calculate the distance from the origin to the point and append to the list
        dis_index_list.append(i) #append the index of the distance so they will match when joined with the originial dataframe
    except ValueError: #If the latitudes or longitudes are out of range, it is dropped from the dataframe
        df.drop(index=i, inplace=True)
    
    


# In[4]:


dis_df = pd.DataFrame() #Create a dataframe of the distances
dis_df['Index'] = dis_index_list
dis_df['Distance km'] = dis_list


# In[5]:


complete_df = df.join(dis_df.set_index('Index')) #join the original dataframe on the distances dataframe


# In[6]:


complete_df.set_index("Location", inplace=True) #set the index of the new dataframe to the distances
complete_df.sort_values(by=['Distance km'], inplace=True) #order the dataframe by the distances in accsending order
complete_df.to_csv("location-distances-data.csv")#Create the new csv file


# In[7]:


s_df = pd.read_csv("location-distances-data.csv")

while(True):
    print('\tOptions')
    print('1. Make Search')
    print('2. List top 5 distances')
    print('3. List top 10 distances')
    print('4. List all Locations & Distances')
    print('5. Exit')
    try:
        choice = int(input('Enter the number of your choice: '))
    except ValueError:
        choice = 6
    if choice == 1:
        loc = input('\nEnter the name of the location: ')
        print('\n\n\n', s_df[s_df['Location'] == loc], '\n\n\n')
    elif choice == 2:
        print('\n\n\n', s_df.tail(5), '\n\n\n')
    elif choice == 3:
        print('\n\n\n', s_df.tail(10), '\n\n\n')
    elif choice == 4:
        for index, row in s_df.iterrows():
            print(row['Location'], row['Latitude'], row['Longitude'], row['Distance km'], '\n')
    elif choice == 5:
        break
    else:
        print('\nThat is an invalid option. Please try again\n')


# In[ ]:




