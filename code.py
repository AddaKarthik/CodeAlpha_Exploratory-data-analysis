import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv('books.csv')

#Clean price column
df['Price'] = df['Price'].str.replace('£', '').astype(float)

#Preview dataset
print("📊 First 5 rows of data:")
print(df.head())

print("\n🧾 Dataset Info:")
print(df.info())

print("\n📈 Summary Statistics:")
print(df.describe())

#Unique Ratings
print("\n⭐ Ratings Value Counts:")
print(df['Rating'].value_counts())

# Convert rating text to numeric
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Num'] = df['Rating'].map(rating_map)

#Availability Count
print("\n📦 Availability:")
print(df['Availability'].value_counts())

#Check for missing values
print("\n❓ Missing Values:")
print(df.isnull().sum())

#Visualizations
#1. Price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Price'], bins=30, color='skyblue', kde=True)
plt.title('Price Distribution of Books')
plt.xlabel('Price (£)')
plt.ylabel('Number of Books')
plt.grid(True)
plt.show()

#2. Rating distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Rating_Num', hue='Rating_Num', palette='viridis', legend=False)
plt.title('Book Ratings Count')
plt.xlabel('Rating (1 to 5)')
plt.ylabel('Number of Books')
plt.show()

#3. Availability
plt.figure(figsize=(6, 3))
df['Availability'].value_counts().plot(kind='barh', color='orange')
plt.title('Book Availability')
plt.xlabel('Count')
plt.show()

#4. Price by Rating
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Rating_Num', y='Price', hue='Rating_Num', palette='pastel', dodge=False, legend=False)
plt.title('Book Price vs Rating')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.show()