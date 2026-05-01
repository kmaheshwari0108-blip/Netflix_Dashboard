import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\kmahe\.vscode\cli\netflix_titles.csv")           
print(df.head())

df.info()                                       #Understand the dataset
df.describe()
df.columns

print(df.isnull().sum())       # Check for missing values

print(df.fillna("Unknown", inplace=True))     # Fill missing values with "Unknown"

print(df.drop_duplicates(inplace = True))

print(df['type'].value_counts())

print(df.dtypes)

df['date_added'] = pd.to_datetime(df['date_added'], errors = 'coerce')          #Convert date column
print(df['date_added'].head())

df['year_added'] = df['date_added'].dt.year             #Create a new column for year added
print(df[['date_added','year_added']].head())

df['month_added'] = df['date_added'].dt.month           #Create a new column for month added
print(df[['date_added','month_added']].head())

df.columns = df.columns.str.strip()          #Remove leading and trailing spaces from column names
print(df.columns)

print(df.info)                             #Check the data types of the columns
print(df.head())

df.sort_values(by='year_added', inplace=True)        #Sort the dataset by year added
print(df[['title', 'year_added']].head())

print(df['type'].value_counts())        #Distribution of content types

sns.countplot(x='type', data=df)          #Visualize the distribution of content types
plt.title('Movies vs TV Shows')
plt.show()

print(df['country'].value_counts().head(10))        #Top 10 countries with the most content

df['country'].value_counts().head(10).plot(kind='bar')        #Visualize the top 10 countries
plt.title('Top 10 Countries ')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

print(df['year_added'].value_counts().sort_index())       #Distribution of content added by year

df['year_added'].value_counts().sort_index().plot(kind='line')        #Visualize the distribution of content added by year
plt.title('Content Added by Year')
plt.show()

print(df['listed_in'].value_counts().head(10))        #Top 10 genres
print(df['rating'].value_counts())        #Visualize the top 10 genres

sns.countplot(x='type' , data = df)        #Visualize the distribution of content types
plt.title('Movies vs TV Shows' , fontsize =  12)
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

top_countries = df['country'].value_counts().head(10)        #Top 10 countries with the most content
top_countries.plot(kind='bar')        #Visualize the top 10 countries
plt.title('Top 10 Countries with the Most Content' , fontsize = 12)
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

year_data = df['year_added'].value_counts().sort_index()       #Distribution of content added by year
year_data.plot(kind='line' , marker = 'o')        #Visualize the distribution of content added by year
plt.title("Netflix Content growth over the years ")
plt.xlabel('year')
plt.ylabel('Number Of Shows')
plt.show()

type_year = df.groupby(['year_added', 'type']).size().unstack()        #Distribution of content types by year
type_year.plot()
plt.title('Distribution of Content Types by Year')
plt.xlabel('Year Added')
plt.ylabel('Count') 
plt.show()

print(df['duration'].value_counts().head(10))        #Top 10 durations

sns.countplot(y = 'rating' , data = df,order = df['rating'].value_counts().index)        #Visualize the distribution of ratings
plt.title('Distribution of Ratings' , fontsize = 12)
plt.xlabel('Count')
plt.ylabel('Rating')
plt.show()