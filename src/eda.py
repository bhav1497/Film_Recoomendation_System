import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


preprocessed_df = pd.read_csv('data/preprocessed_movies.csv')

print("Summary Statistics of Numerical Features:")
print(preprocessed_df.describe())

numerical_features = ['budget', 'gross', 'runtime']
preprocessed_df[numerical_features].hist(bins=20, figsize=(12, 8))
plt.suptitle("Numerical Features Distribution", y=0.95, fontsize=16)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=preprocessed_df, x='genre')
plt.title("Distribution of Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

numerical_df = preprocessed_df.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 8))
sns.heatmap(numerical_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Numerical Features")
plt.show()
