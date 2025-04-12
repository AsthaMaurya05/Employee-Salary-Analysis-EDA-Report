import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # for heatmap and other plots

# Load the data
df = pd.read_csv("C:/Users/Lenovo/OneDrive/Desktop/python project/Employee_Salaries_-_2024.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Basic info
print("Total rows and columns:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nFirst 5 records:")
print(df.head())

# Missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Convert salary columns to numeric
df['Base Salary'] = pd.to_numeric(df['Base Salary'], errors='coerce')
df['2024 Overtime Pay'] = pd.to_numeric(df['2024 Overtime Pay'], errors='coerce')
df['2024 Longevity Pay'] = pd.to_numeric(df['2024 Longevity Pay'], errors='coerce')

# Drop rows with all pay data missing
df = df.dropna(subset=['Base Salary', '2024 Overtime Pay', '2024 Longevity Pay'], how='all')

# Add Total Pay column
df['Total Pay'] = df['Base Salary'].fillna(0) + df['2024 Overtime Pay'].fillna(0) + df['2024 Longevity Pay'].fillna(0)

# Summary stats
print("\nSummary statistics:")
print(df[['Base Salary', '2024 Overtime Pay', '2024 Longevity Pay', 'Total Pay']].describe())

# 1. Gender Distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, palette='pastel', hue='Gender', legend=False)
plt.title('Gender Distribution', fontsize=14)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# 2. Histogram of Base Salary
plt.figure(figsize=(8, 6))
sns.histplot(df['Base Salary'], bins=30, kde=True, color='mediumseagreen')
plt.title('Base Salary Distribution', fontsize=14)
plt.xlabel('Base Salary')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 3. Box Plot of Base Salary
plt.figure(figsize=(8, 6))
sns.boxplot(x='Base Salary', data=df, color='skyblue')
plt.title('Box Plot of Base Salary', fontsize=14)
plt.xlabel('Base Salary')
plt.tight_layout()
plt.show()

# 4. Heatmap of Salary Correlations
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Base Salary', '2024 Overtime Pay', '2024 Longevity Pay', 'Total Pay']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Salary-related Columns', fontsize=14)
plt.tight_layout()
plt.show()

# 5. Top 10 Divisions by Average Base Salary
avg_salary = df.groupby('Division')['Base Salary'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=avg_salary.values, y=avg_salary.index, palette='viridis', hue=avg_salary.index, legend=False)
plt.title('Top 10 Divisions by Average Base Salary', fontsize=14)
plt.xlabel('Average Salary')
plt.ylabel('Division')
plt.tight_layout()
plt.show()

# 6. Top 5 Departments by Average Total Pay
top_departments = df.groupby('Department Name')['Total Pay'].mean().sort_values(ascending=False).head(5)
print("\nTop 5 Departments by Average Total Pay:")
print(top_departments)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_departments.values, y=top_departments.index, palette='magma', hue=top_departments.index, legend=False)
plt.title('Top 5 Departments by Average Total Pay', fontsize=14)
plt.xlabel('Average Total Pay')
plt.ylabel('Department')
plt.tight_layout()
plt.show()



# 7. Scatter Plot: Base Salary vs Overtime Pay
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Base Salary', y='2024 Overtime Pay', data=df, color='indigo')
plt.title('Base Salary vs Overtime Pay', fontsize=14)
plt.xlabel('Base Salary')
plt.ylabel('Overtime Pay')
plt.tight_layout()
plt.show()
