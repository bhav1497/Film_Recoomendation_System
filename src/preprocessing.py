import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer


movies_df = pd.read_csv('data/movies.csv')#C:/Users/Bhavana/OneDrive/Desktop/MovieRecommendationSystem/

movies_df['budget'].fillna(0, inplace=True)
movies_df['gross'].fillna(0, inplace=True)

label_encoder = LabelEncoder()
movies_df['genre'] = label_encoder.fit_transform(movies_df['genre'])
movies_df['rating'] = label_encoder.fit_transform(movies_df['rating'])
movies_df['country'] = label_encoder.fit_transform(movies_df['country'])

scaler = StandardScaler()
movies_df[['budget', 'gross', 'runtime']] = scaler.fit_transform(movies_df[['budget', 'gross', 'runtime']])

preprocessed_file_path = 'data/preprocessed_movies.csv'#C:/Users/Bhavana/OneDrive/Desktop/MovieRecommendationSystem
movies_df.to_csv(preprocessed_file_path, index=False)
print("Data preprocessing completed. Preprocessed dataset saved as 'preprocesses_movies.csv'")
