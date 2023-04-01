#!/usr/bin/env python
# coding: utf-8

# In[1]:


import opendatasets as od 


# # US Accidents (2016 - 2021)

# In[2]:


data = 'https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents'


# In[3]:


od.download(data)


# In[4]:


import os 


# In[5]:


import seaborn as sns


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


data_dir = './us-accidents'   #diractory where file downloading 


# In[8]:


os.listdir(data_dir) 


# In[9]:


import pandas as pd #for analu=ysis 


# In[10]:


df = pd.read_csv('US_Accidents_Dec21_updated.csv')#move file in diractory 


# In[11]:


df.head()


# In[12]:


df.shape


# In[13]:


len(df.columns) #for count of columns 


# In[14]:


len(df)  #for rows 


# In[15]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

newdf = df.select_dtypes(include=numerics)
len(newdf.columns)


# In[16]:


missing_percentage = df.isna().sum().sort_values(ascending=False) / len(df)


# In[17]:


df.columns


# In[18]:


missing_percentage[missing_percentage!= 0].plot(kind= 'barh')


# ## ask & answer questions 
# 1. are there more accidents in warmer or colder areas ?
# 2.which 5 state have the highest number of accident ?how about per capita .
# 3.does new york show up in the data ? if yes ,why is the count lower if this the most populated city.
# 4.among the top cities in number of accidents ,which state do they belong to the most frequently 
# 5.what time of the day are accidents most frequant in?(done)
# 6. which days of the week have the most accidents ?(done)
# 7. which month have the most accidents ?(done)
# 8.what is the trend of accidents year over year ?(decreasing/increasing)
# 9.when is accidents per unit of traffic the highest ?
# 10.which day of the december is the deadliest?
# 11.Top weather conditions when accidents mostly happen?

# ## columns we will analyze:
# 1 city 
# 2 start time 
# 3 start lat ,start lng 
# 4 temprature 
# 5 weather condition 
# 

# ## City

# In[19]:


df.columns


# In[20]:


df.City


# In[21]:


cities = df.City.unique()
cities[:100]


# In[22]:


cities_by_accident = df.City.value_counts()
cities_by_accident


# In[23]:


# top 10 cities of usa with high counts of accidents .

cities_by_accident[:10]


# In[24]:


cities_by_accident[:10].plot(kind='barh')


# In[25]:


import seaborn as sns 
sns.set_style("darkgrid")


# In[26]:


sns.displot(cities_by_accident,log_scale = True)


# '''few of the cities has the 0 or 1 accidents that means somethingh is wrong  '''

# In[27]:


cities_with_few_accidents = cities_by_accident[cities_by_accident == 1]
len(cities_with_few_accidents)


# '''1110 cities has only 1 accidents '''

# ''' our data covers 49 states of the USA.'''

# In[ ]:





# ## start_time

# In[28]:


df.Start_Time[0]   #str of date is yyyy-mm-dd and time 


# ok so right now our start_time column is string.

# In[29]:


df.Start_Time = pd.to_datetime(df.Start_Time)  #converted string/object into datestamp
df.Start_Time[0]


# 5.what time of the day are accidents most frequant in?

# In[30]:


sns.displot(df.Start_Time.dt.hour,bins = 24,kde = False )  


# - A high percentage of accidents occur between the 2pm to 5pm .
# - next highest percentage is 6am to 10 am .(probably people ia a hurry to get to work )
'''6. which days of the week have the most accidents ?'''
# In[31]:


sns.displot(df.Start_Time.dt.dayofweek,bins = 24,kde = False) 


# - on weekends no of accidents are lower

# '''Is the distribution of accidents by hour the same on weekends as on weekdays'''

# In[32]:


# 6 = sunday, we are finding about sunday
sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]
sns.displot(sundays_start_time.dt.hour,bins = 24,kde = False) 


# In[33]:


# 0 = monday ,for finding working days  
monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 0]
sns.displot(monday_start_time.dt.hour,bins = 24,kde = False) 


# In[34]:


saturday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 5]
sns.displot(saturday_start_time.dt.hour,bins = 24,kde = False) 


# - on sundays ,peek occurs between midnight (probably people returning from parties)
#    and 12 pm to 6 pm 
# - so we also see that night accident peek on saturday .   
# - on monday ,peek occurs on tiem when people going for work and returning from work .
'''7. which month have the most accidents ?'''
# In[35]:


sns.displot(df.Start_Time.dt.month,bins = 12,kde = False) 

can you explain the monthwise trend of accidents ?
'''why are there more accidents in the winter '''
# - because december is a month of thanksgiving and christmas in america .
# - According to the Office of National Statistics, road traffic accidents are much higher in December than any other month of the year
'''which day of the december is the deadliest '''
# In[36]:


december_start_time = df.Start_Time[df.Start_Time.dt.month == 12 ]
sns.displot(december_start_time.dt.day,bins = 31,kde = False) 


# - so,we can see that 23rd fec has the highest of accidents records in december month .
# - the hustle and bustle sadly bring more traffic accidents with the 23rd and 24th December being the deadliest days of the year on the roads. 
# - According to the Office of National Statistics
# - and we are also able to see that in our visual why December has record the highest of all accidents .
# - maybe much data is missing of starting year but i am pursuing with that analysis .

# '''enough qutions with start time '''

# In[37]:


df_2016 = df[df.Start_Time.dt.year == 2016]
sns.distplot(df_2016.Start_Time.dt.month, bins = 12, kde = False,  norm_hist = True )
plt.ylabel('Percentage')
plt.show()


# After looking the distrubution of each year we can understand the issue.
# Probably not enough data was collected for each year. We understand this from this: Look at years like 2016, 2019 and 2020.
# It is easy to see that data is missing for some months. This explains the lack of a regular distribution.

# In[ ]:





# ## Start latitude & longitude

# In[38]:


df.columns


# In[39]:


df.Start_Lat


# In[40]:


df.Start_Lng


# In[41]:


sns.scatterplot(x = df.Start_Lng,y=df.Start_Lat)


# When we look at the latitude and longitude of the accidents, we can see that the accidents are distributed in
# a way similar to the map of America. 
# This is not a surprising result, assuming that the accidents happened in America.

# In[42]:


import folium   #for mapping the lng and lat data .


# In[43]:


from folium.plugins import HeatMap


# In[44]:


map = folium.Map()
HeatMap(zip(list(df.Start_Lat),list(df.Start_Lng))).add_to(map)
map


# In[ ]:





# In[45]:


# seasonal analysis


# ## Weather Condition
# 

# In[46]:


df.columns


# # -- Top weather conditions when accidents mostly happen?

# In[47]:


Time_Of_accidents_weather = df.Weather_Condition.unique()   
Time_Of_accidents_weather[:20]


# In[48]:


accident_weather_condition = df.Weather_Condition.value_counts()    #ok so most of the time of accidents weather is Fair .
accident_weather_condition


# In[49]:


#top 10 Weather conditions when accidents mostly happens.
accident_weather_condition[:10]


# In[50]:


accident_weather_condition[:10].plot(kind='barh')  #so most of the time weather condition is fair .


# - so most of the time weather condition is fair

# In[ ]:





# # Main Questions
# 
# - are there more accidents in warmer or coldest area ?

# In[51]:


df.columns   #temprature in f so we have to convert it into c=celcius


# In[53]:


# change F to C        32f = 0c
df["Celsius"] = df["Temperature(F)"].apply(lambda F : (F-32) * 5/9)


# - we will call areas below 20 degree celcius the colde zone. 
# - Above 20 degrees Celsius, we will call it a warmer zone.

# In[54]:


colder = df.Celsius[df.Celsius < 20]
warmer = df.Celsius[df.Celsius > 20]


# In[55]:


len(colder)


# In[56]:


len(warmer)


# - see that there are more accidents in hot regions than in cold regions.

# # 2nd question
# - Which states has the highest number of acciedents? How about per capita?

# In[ ]:


df.State.value_counts().sort_values(ascending = False).index[0]


# In[ ]:





# In[ ]:


#3rd question
- #3.does new york show up in the data ? if yes ,why is the count lower if this the most populated city


# - so the answer of the 2nd question is California .

# In[ ]:


df.City[df.City == "New York"]


# - It looks like the data includes New York. So let's look at the number of accidents in New York

# In[ ]:


df.City[df.City == "New York"].value_counts()


# It seems there were only 7068 accidents in New York. In Miami alone (the city with the highest number of accidents) there are more than 106,000 accidents. Why New York has so few accidents despite being the most populous city needs to be investigated. This could help us in new efforts to reduce accidents in other cities.

# In[ ]:





# # Summary and Conclusion
# 

# # Insights:
#     1.Over 1110 cities reported just 1 accident, which needs further investigation.(missing of data)
#     2.Accidents intensify between 05:00 and 07:00 and between 16:00 and 18:00, 
#       which can be attributed to heavy traffic during rush hour.
#     3.Accidents are lower during weekend mornings, but increase in the afternoon,
#     potentially due to people being out and about.
#     4. The three cities with the highest number of accidents per year are Miami (>100,000), Los Angeles (>60,000), 
#     and Orlando (>50,000), while New York has a surprisingly low number of accidents despite being the most populous city.
#     5.California has the highest number of accidents and accident rates per capita among US states.
#     6.There are more accidents in hot regions compared to cold regions.
#     
#     
