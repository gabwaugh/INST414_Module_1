import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from CSV file
df = pd.read_csv('megaGymDataset.csv')

print(df.head())

# Filter the data to include only 'Cardio' workouts
df_cardio = df[df['Type'] == 'Cardio']

# Convert 'Rating' to numeric and handle missing values
df_cardio['Rating'] = pd.to_numeric(df_cardio['Rating'], errors='coerce')

# Drop rows with missing values in 'Rating' and 'Title'
df_cardio_cleaned = df_cardio.dropna(subset=['Rating', 'Title'])

# Calculate average rating by 'Title'
avg_rating_by_title = df_cardio_cleaned.groupby('Title')['Rating'].mean().reset_index()

# Sort by average rating in descending order to identify the best workouts
avg_rating_by_title = avg_rating_by_title.sort_values(by='Rating', ascending=False)

# Plotting the average ratings for each cardio workout
plt.figure(figsize=(14, 10))
sns.barplot(x='Rating', y='Title', data=avg_rating_by_title, palette='coolwarm')
plt.title('Average Rating of Cardio Workouts')
plt.xlabel('Average Rating')
plt.ylabel('Cardio Workout Name')

# Annotate the bars with rating values
for index, value in enumerate(avg_rating_by_title['Rating']):
    plt.text(value, index, f'{value:.1f}', va='center')

plt.show()

