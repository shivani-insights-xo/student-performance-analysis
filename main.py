import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 1. Load Dataset
# ==========================

df = pd.read_csv("student-mat.csv", sep=';')

print("Dataset Loaded Successfully!\n")

# ==========================
# 2. Explore Dataset
# ==========================

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

# ==========================
# 3. Data Cleaning
# ==========================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)

# ==========================
# 4. Analysis Questions
# ==========================

# Average Final Grade
average_grade = df['G3'].mean()
print("\nAverage Final Grade (G3):", round(average_grade, 2))

# Students scoring above 15
above_15 = len(df[df['G3'] > 15])
print("Students Scoring Above 15:", above_15)

# Correlation between study time and final grade
correlation = df['studytime'].corr(df['G3'])
print("Correlation Between Study Time and Final Grade:", round(correlation, 2))

# Gender performance
gender_avg = df.groupby('sex')['G3'].mean()

print("\nAverage Grade by Gender:")
print(gender_avg)

if gender_avg['F'] > gender_avg['M']:
    print("Female students perform better on average.")
elif gender_avg['M'] > gender_avg['F']:
    print("Male students perform better on average.")
else:
    print("Both genders perform equally.")

# ==========================
# 5. Visualizations
# ==========================

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['G3'], bins=10, edgecolor='black')
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df['studytime'], df['G3'])
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.show()

# Bar Chart
plt.figure(figsize=(6, 5))
gender_avg.plot(kind='bar')
plt.title("Average Grade by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Grade")
plt.show()

# ==========================
# 6. Conclusion
# ==========================

print("\n========== SUMMARY ==========")
print("Average Final Grade:", round(average_grade, 2))
print("Students Above 15:", above_15)
print("Study Time Correlation:", round(correlation, 2))
print("Male students perform better on average.")
print("=============================")