#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
import numpy as np
import locale
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from tabulate import tabulate


# In[124]:


df = pd.read_csv("imdb_movies.csv")


# In[125]:


df.head()


# In[126]:


df.info()


# In[127]:


# Assuming you have a DataFrame named df
description_table = df.info()

# Convert the table to Markdown format
markdown_table = tabulate(description_table, headers='keys', tablefmt='pipe')

# Print the Markdown table
print(markdown_table)


# In[128]:


len(df)


# # Check Duplication

# In[129]:


# Check if any duplicated value in all rows
df.duplicated().sum()


# # Data Preprocessing

# ## Change data to datetime

# In[130]:


df['date_x']


# In[131]:


df['release_date'] = pd.to_datetime(df['date_x'], infer_datetime_format=True)


# ## Check Missing Value

# In[132]:


variables = []
dtypes = []
count = []
unique = []
missing = []


for item in df.columns:
    variables.append(item)
    dtypes.append(df[item].dtype)
    count.append(len(df[item]))
    unique.append(len(df[item].unique()))
    missing.append(df[item].isna().sum())

output = pd.DataFrame({
    'variable': variables, 
    'dtype': dtypes,
    'count': count,
    'unique': unique,
    'missing': missing, 
   
})    

output.sort_values("missing",ascending=False).reset_index(drop=True)
output


# In[133]:


# Assuming you have a DataFrame named df
description_table = output

# Convert the table to Markdown format
markdown_table = tabulate(description_table, headers='keys', tablefmt='pipe')

# Print the Markdown table
print(markdown_table)


# ## Check Genre missing value

# In[134]:


# remove genre has nan value 
filtered_genre = df.loc[df['genre'].isnull() == True]
filtered_genre


# In[135]:


df = df.dropna(subset=['genre'])


# ## Check Crew missing value

# In[136]:


# remove genre has nan value 
filtered_crew = df.loc[df['crew'].isnull() == True]
filtered_crew


# In[137]:


df = df.dropna(subset=['crew'])


# ## After drop missing value

# In[138]:


variables = []
dtypes = []
count = []
unique = []
missing = []


for item in df.columns:
    variables.append(item)
    dtypes.append(df[item].dtype)
    count.append(len(df[item]))
    unique.append(len(df[item].unique()))
    missing.append(df[item].isna().sum())

output = pd.DataFrame({
    'variable': variables, 
    'dtype': dtypes,
    'count': count,
    'unique': unique,
    'missing': missing, 
   
})    

output.sort_values("missing",ascending=False).reset_index(drop=True)
output


# In[139]:


# Assuming you have a DataFrame named df
description_table = output

# Convert the table to Markdown format
markdown_table = tabulate(description_table, headers='keys', tablefmt='pipe')

# Print the Markdown table
print(markdown_table)


# ## Genre using tfidfvectorizer

# In[140]:


from sklearn.feature_extraction.text import TfidfVectorizer
 
# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()


# In[141]:


# Melakukan perhitungan idf pada data cuisine
tf.fit(df['genre']) 
 
# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out() 


# In[142]:


# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(df['genre']) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape 


# In[143]:


# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama resto
 
output = pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names(),
    index=df.names
).sample(21, axis=1).sample(10, axis=0)


# In[144]:


# Assuming you have a DataFrame named df
description_table = output

# Convert the table to Markdown format
markdown_table = tabulate(description_table, headers='keys', tablefmt='pipe')

# Print the Markdown table
print(markdown_table)


# In[145]:


# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()


# ## Genre into list

# In[146]:


# Function to split and remove \xa0 from genre strings
def split_genre(genre_string):
    genre_list = [genre.strip().replace('\xa0', '') for genre in genre_string.split(',')]
    return genre_list

# Apply the function to the 'genre' column and create a new 'genre_split' column
df['genre_split'] = df['genre'].apply(split_genre)


# In[147]:


set_of_genre = set()
for genres in df['genre_split']:
    for genre in genres:
        set_of_genre.add(genre)


# In[148]:


set_of_genre


# In[149]:


# Perform one-hot encoding for genres
one_hot_encoding = pd.get_dummies(df['genre_split'].apply(pd.Series).stack()).sum(level=0)


# In[150]:


one_hot_encoding


# In[151]:


# Concatenate the one-hot encoded genres with the original DataFrame
df_one_hot = pd.concat([df['names'], one_hot_encoding], axis=1)


# In[152]:


# Assuming you have a DataFrame named df
description_table = df_one_hot.head()

# Convert the table to Markdown format
markdown_table = tabulate(description_table, headers='keys', tablefmt='pipe')

# Print the Markdown table
print(markdown_table)


# In[153]:


# df.drop(columns=['genre_split','genre'], inplace=True)


# In[154]:


df


# ## Check revenue & Budget

# In[155]:


df['revenue']


# In[156]:


# Custom function to format the revenue as a dollar value
def format_value(value):
    locale.setlocale(locale.LC_ALL, '')  # Set the locale to the default system locale
    return locale.currency(value, grouping=True)

# Apply the custom function to format revenue in the DataFrame
df['revenue_formatted'] = df['revenue'].apply(format_value)
df['budget_formatted'] = df['budget_x'].apply(format_value)

df['revenue_formatted'] = df['revenue_formatted'].str.replace('[Rp,.]', '', regex=True).astype(float)
df['budget_formatted'] = df['budget_formatted'].str.replace('[Rp,.]', '', regex=True).astype(float)


# In[157]:


df


# ## origin languange

# In[158]:


# Function to split and remove \xa0 from genre strings
def split_origin(origin_string):
    origin_list = [origin.strip().replace('\xa0', '') for origin in origin_string.split(',')]
    return origin_list

# Apply the function to the 'genre' column and create a new 'genre_split' column
df['origin_lang_split'] = df['orig_lang'].apply(split_genre)


# In[159]:


set_of_origin_lang = set()
for origin_langs in df['origin_lang_split']:
    for origin_lang in origin_langs:
        set_of_origin_lang.add(origin_lang)
        
set_of_origin_lang


# In[160]:


df


# In[161]:


df_model = df[['names','score','genre_split','origin_lang_split','crew','overview','status','revenue','country','release_date']].copy()

df_model = df[['names','overview','genre','score']]


# ## overview

# In[162]:


df['overview'].iloc[0]


# ## Realease date

# In[163]:


date_range = df['release_date'].max() - df['release_date'].min()

# Convert the difference to years
years_range = date_range.days / 365.25  # 365.25 accounts for leap years

print("The range between the earliest and latest release dates is approximately {:.2f} years.".format(years_range))


# ## Score Rating

# In[164]:


df.loc[df['score'] == 0]


# # EDA

# ## Bagaimana distribusi rating film dalam dataset?

# In[165]:


# Assuming 'df' is your DataFrame containing the 'rating' column
# If your rating column is named differently, replace 'rating' with the correct column name.

# Create a histogram to visualize the distribution of ratings
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='score', bins=20, kde=False, color='skyblue')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()


# In[166]:


# Create a KDE plot to visualize the distribution of ratings
plt.figure(figsize=(8, 6))
sns.kdeplot(data=df, x='score', fill=True, color='skyblue', alpha=0.6)
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Density')
plt.show()


# ## Bagaimana distribusi pendapatan (revenue) dan budget film dalam dataset?
# 

# In[167]:


# Create subplots with two plots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(23, 8))

# Plot for Revenue
sns.histplot(data=df, x='revenue_formatted', bins=20, kde=False, color='purple', ax=ax1)
ax1.xaxis.set_major_formatter(ticker.StrMethodFormatter('Rp{x:,.0f}M'))
ax1.set_title('Distribution of Movie Revenue')
ax1.set_xlabel('Revenue')
ax1.set_ylabel('Count')

# Plot for Budget
sns.histplot(data=df, x='budget_formatted', bins=20, kde=False, color='skyblue', ax=ax2)
ax2.xaxis.set_major_formatter(ticker.StrMethodFormatter('Rp{x:,.0f}M'))
ax2.set_title('Distribution of Movie Budget')
ax2.set_xlabel('Budget')
ax2.set_ylabel('Count')

plt.tight_layout()
plt.show()


# In[168]:


# Assuming you have already defined 'df' and imported necessary libraries

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(23, 8))

# Plot for Revenue
sns.kdeplot(data=df, x='revenue_formatted',  fill=True, color='purple', alpha=0.6, ax=ax1)
ax1.xaxis.set_major_formatter(ticker.StrMethodFormatter('Rp{x:,.0f}M'))
ax1.set_title('Distribution of Movie Revenue')
ax1.set_xlabel('Revenue')
ax1.set_ylabel('Count')

# Plot for Budget
sns.kdeplot(data=df, x='budget_formatted',  fill=True, color='skyblue', alpha=0.6,  ax=ax2)
ax2.xaxis.set_major_formatter(ticker.StrMethodFormatter('Rp{x:,.0f}M'))
ax2.set_title('Distribution of Movie Budget')
ax2.set_xlabel('Budget')
ax2.set_ylabel('Count')

plt.tight_layout()

# Save the subplots as JPG
plt.savefig('movie_revenue_budget_distribution.jpg', dpi=300)  # Saving the subplots as JPG with 300 DPI (adjust as needed)

plt.show()


# ## Apakah ada korelasi antara anggaran produksi dan pendapatan film?
# 

# In[169]:


import matplotlib.pyplot as plt

# Assuming you have already defined 'df' and imported necessary libraries

plt.figure(figsize=(8, 6))
plt.scatter(df['budget_formatted'], df['revenue_formatted'], alpha=0.5, color='b')
plt.title('Scatter Plot: Production Budget vs. Revenue')
plt.xlabel('Production Budget')
plt.ylabel('Revenue')
plt.grid(True)

# Save the scatter plot as JPG
plt.savefig('production_budget_vs_revenue_scatter.jpg', dpi=300)  # Saving the scatter plot as JPG with 300 DPI (adjust as needed)

plt.show()


# In[170]:


# Split multiple genres in the 'genres' column and create a new DataFrame
genre_counts = df['genre'].str.split(',').explode().str.strip().value_counts()

# Create a bar plot to visualize the most frequent movie genres
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
plt.title('Most Frequently Occurring Movie Genres')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ## Bagaimana distribusi tahun rilis film dalam dataset?

# In[171]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming you have already defined 'df' and imported necessary libraries

df['release_year'] = pd.to_datetime(df['release_date']).dt.year

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='release_year', bins=30, kde=False, color='skyblue')
plt.title('Distribution of Movie Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the histogram as JPG
plt.savefig('movie_release_years_distribution.jpg', dpi=300)  # Saving the histogram as JPG with 300 DPI (adjust as needed)

plt.show()


# ## Apakah ada tren peningkatan atau penurunan jumlah film dari waktu ke waktu?

# In[172]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assuming you have already defined 'df' and imported necessary libraries

movie_count_by_year = df['release_year'].value_counts().sort_index()

# Create bins of 10 years
bins = range(df['release_year'].min(), df['release_year'].max() + 11, 10)

# Group movie counts into bins of 10 years and sum the counts in each bin
movie_count_by_bin = df.groupby(pd.cut(df['release_year'], bins=bins)).size()

plt.figure(figsize=(10, 6))
sns.lineplot(x=movie_count_by_bin.index.astype(str), y=movie_count_by_bin.values, marker='o', color='skyblue')
plt.title('Movie Count Trend Over Time (Grouped by 10 Years)')
plt.xlabel('Release Year')
plt.ylabel('Movie Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Add data point labels (dot values) to the line plot
for i, count in enumerate(movie_count_by_bin.values):
    plt.text(i, count, str(count), ha='center', va='bottom', color='black', fontweight='bold')

# Save the line plot as JPG
plt.savefig('movie_count_trend_over_time.jpg', dpi=300)  # Saving the line plot as JPG with 300 DPI (adjust as needed)

plt.show()


# In[173]:


# Group the data by release year and count the number of movies for each year
movie_count_by_year = df['release_year'].value_counts().sort_index()

# Create bins of 5 years
bins = range(df['release_year'].min(), df['release_year'].max() + 6, 5)

# Group movie counts into bins of 5 years and sum the counts in each bin
movie_count_by_bin = df.groupby(pd.cut(df['release_year'], bins=bins)).size()

# Create a line plot to visualize the movie count trend over time with 5-year bins
plt.figure(figsize=(10, 6))
sns.lineplot(x=movie_count_by_bin.index.astype(str), y=movie_count_by_bin.values, marker='o', color='skyblue')
plt.title('Movie Count Trend Over Time (Grouped by 5 Years)')
plt.xlabel('Release Year')
plt.ylabel('Movie Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Add data point labels (dot values) to the line plot
for i, count in enumerate(movie_count_by_bin.values):
    plt.text(i, count, str(count), ha='center', va='bottom', color='black', fontweight='bold')

plt.show()


# In[174]:


df = df.reset_index()
df


# # Modeling

# In[175]:


import matplotlib.pyplot as plt
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA


# In[176]:


# X = np.array(df_model.overview)

# text_data = X
# model = SentenceTransformer('distilbert-base-nli-mean-tokens')
# embeddings = model.encode(text_data, show_progress_bar=True)


# In[177]:


# Assuming you already have the 'embeddings' array
# Save the embeddings to a file
# np.save('embeddings.npy', embeddings)

# Load the embeddings back from the file when needed
embeddings = np.load('embeddings.npy')

# embed_data = embeddings


# In[178]:


rating_score = np.array(df_model.score)

# Concatenate additional features with embeddings
additional_features = np.column_stack((rating_score, one_hot_encoding))  # Adjust this based on your features
additional_features


# ## Using one hot encoding

# In[179]:


combined_features = np.concatenate((embeddings, additional_features), axis=1)

n_comp = 5
pca = PCA(n_components=n_comp)
pca.fit(combined_features)
pca_data = pd.DataFrame(pca.transform(combined_features))
pca_data.head()


# In[180]:


cos_sim_data_1 = pd.DataFrame(cosine_similarity(pca_data))
cos_sim_data_1


# In[181]:


def give_recommendations_1(index,print_recommendation = False,print_recommendation_plots= False,print_genres =False):
    index_recomm =cos_sim_data_1.loc[index].sort_values(ascending=False).index.tolist()[1:11]
#     movies_recomm =  df_model['names'].loc[index_recomm].values
#     score_recomm =  df_model['score'].loc[index_recomm].values
#     result = {'Movies':movies_recomm,'Index':index_recomm, 'Score': score_recomm}
#     if print_recommendation==True:
#         print('The watched movie is this one: %s \n'%(df_model['names'].loc[index]))
#         k=1
#         for movie in movies_recomm:
#             print('The number %i recommended movie is this one: %s \n'%(k,movie))
#             k=k+1
#     if print_recommendation_plots==True:
#         print('The plot of the watched movie is this one:\n %s \n'%(df_model['overview'].loc[index]))
#         k=1
#         for q in range(len(movies_recomm)):
#             plot_q = data['Overview'].loc[index_recomm[q]]
#             print('The plot of the number %i recommended movie is this one:\n %s \n'%(k,plot_q))
#             k=k+1
#     if print_genres==True:
#         print('The genres of the watched movie is this one:\n %s \n'%(df_model['genre'].loc[index]))
#         k=1
#         for q in range(len(movies_recomm)):
#             plot_q = data['Genre'].loc[index_recomm[q]]
#             print('The plot of the number %i recommended movie is this one:\n %s \n'%(k,plot_q))
#             k=k+1
    return df.loc[index_recomm]


# ## Using tfid Vectorizer

# In[182]:


tfidf_matrix_t = pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names()
)


# In[183]:


additional_features = np.column_stack((rating_score, tfidf_matrix_t))  # Adjust this based on your features
additional_features


# In[184]:


combined_features = np.concatenate((embeddings, additional_features), axis=1)

n_comp = 5
pca = PCA(n_components=n_comp)
pca.fit(combined_features)
pca_data = pd.DataFrame(pca.transform(combined_features))
pca_data.head()


# In[185]:


cos_sim_data_2 = pd.DataFrame(cosine_similarity(pca_data))
cos_sim_data_2


# In[186]:


def give_recommendations_2(index,print_recommendation = False,print_recommendation_plots= False,print_genres =False):
    index_recomm =cos_sim_data_2.loc[index].sort_values(ascending=False).index.tolist()[1:11]
#     print(index_recomm)
#     movies_recomm =  df_model['names'].loc[index_recomm].values
#     score_recomm =  df_model['score'].loc[index_recomm].values
#     result = {'Movies':movies_recomm,'Index':index_recomm, 'Score': score_recomm}
#     if print_recommendation==True:
#         print('The watched movie is this one: %s \n'%(df_model['names'].loc[index]))
#         k=1
#         for movie in movies_recomm:
#             print('The number %i recommended movie is this one: %s \n'%(k,movie))
#             k = k+1
#     if print_recommendation_plots==True:
#         print('The plot of the watched movie is this one:\n %s \n'%(df_model['overview'].loc[index]))
#         k=1
#         for q in range(len(movies_recomm)):
#             plot_q = data['Overview'].loc[index_recomm[q]]
#             print('The plot of the number %i recommended movie is this one:\n %s \n'%(k,plot_q))
#             k=k+1
#     if print_genres==True:
#         print('The genres of the watched movie is this one:\n %s \n'%(df_model['genre'].loc[index]))
#         k=1
#         for q in range(len(movies_recomm)):
#             plot_q = data['Genre'].loc[index_recomm[q]]
#             print('The plot of the number %i recommended movie is this one:\n %s \n'%(k,plot_q))
#             k=k+1
    return df.loc[index_recomm]


# In[187]:


df_recommendations_1 = pd.DataFrame()
df_recommendations_1 = df_recommendations_1.append(give_recommendations_1(228, True))
df_recommendations_1


# In[194]:


from tabulate import tabulate

# Assuming you have a DataFrame named df
description_table = df_recommendations_2[['names','genre','score']]

# Convert the table to Markdown format
markdown_table = tabulate(description_table, headers='keys', tablefmt='pipe')

# Print the Markdown table
print(markdown_table)


# In[188]:


df_recommendations_2 = pd.DataFrame()
df_recommendations_2 = df_recommendations_2.append(give_recommendations_2(228, True))


# In[189]:


df_recommendations_2


# ## Evaluation

# In[195]:


testing_data = ["Avengers: Endgame", "Avengers: Infinity War", "Captain America: The First Avenger", "The Big 4"]
recall_average = 0
precision_average = 0
akurasi_average = 0
for test_data in testing_data:
    index = df.index[df['names'] == test_data].tolist()
    df_test = df.loc[index]
    genre_test = df_test['genre_split'].iloc[0]
    
    df_recommendations_1 = pd.DataFrame()
    df_recommendations_1 = df_recommendations_1.append(give_recommendations_1(230, True))
    
    label = []
    for genre_list in df_recommendations_1['genre_split']:
        if len(set(genre_test).intersection(genre_list)) != 0:
            label.append(1)
        else:
            label.append(0)
    df_recommendations_1['recommendation'] = label
    
    TP = len(df_recommendations_1.loc[df_recommendations_1['recommendation'] == 1])
    TN = len(df_recommendations_1.loc[df_recommendations_1['recommendation'] == 0])
    FP = 0
    FN = 0
    
    recall = TP/(TP+FN)
    recall_average+=recall
    precision = TP/(TP+FP)
    precision_average+=precision
    akurasi = (TP + TN ) / (TP+FP+FN+TN)
    akurasi_average +=akurasi
    
print("recal average :",recall_average/len(testing_data))
print("precision average :",precision_average/len(testing_data))
print("akurasi average :",akurasi_average/len(testing_data))


# In[191]:


testing_data = ["Avengers: Endgame", "Avengers: Infinity War", "Captain America: The First Avenger", "The Big 4"]
recall_average = 0
precision_average = 0
akurasi_average = 0
for test_data in testing_data:
    index = df.index[df['names'] == test_data].tolist()
    df_test = df.loc[index]
    genre_test = df_test['genre_split'].iloc[0]
    
    df_recommendations_2 = pd.DataFrame()
    df_recommendations_2 = df_recommendations_1.append(give_recommendations_2(230, True))
    
    label = []
    for genre_list in df_recommendations_2['genre_split']:
        if len(set(genre_test).intersection(genre_list)) != 0:
            label.append(1)
        else:
            label.append(0)
    df_recommendations_2['recommendation'] = label
    
    TP = len(df_recommendations_2.loc[df_recommendations_2['recommendation'] == 1])
    TN = len(df_recommendations_2.loc[df_recommendations_2['recommendation'] == 0])
    FP = 0
    FN = 0
    
    recall = TP/(TP+FN)
    recall_average+=recall
    precision = TP/(TP+FP)
    precision_average+=precision
    akurasi = (TP + TN ) / (TP+FP+FN+TN)
    akurasi_average +=akurasi
    
print("recal average :",recall_average/len(testing_data))
print("precision average :",precision_average/len(testing_data))
print("akurasi average :",akurasi_average/len(testing_data))


# In[ ]:




