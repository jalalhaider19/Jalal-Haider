##Part 1
##Data Generation 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Number of samples
num_samples = 1000

# Generate normally distributed data for age, height, weight, and income
ages = np.random.normal(35, 10, size=num_samples).astype(int)
# Ensure ages are within a realistic range (e.g., 18 to 70)
ages = np.clip(ages, 18, 70)

height = np.random.normal(170, 15, size=num_samples).astype(int)
# Ensure heights are within a realistic range (e.g., 140 to 210)
height = np.clip(height, 140, 210)

weight = np.random.normal(70, 10, size=num_samples).astype(int)
# Ensure weights are within a realistic range (e.g., 40 to 150)
weight = np.clip(weight, 40, 150)

income = np.random.normal(50000, 15000, size=num_samples).astype(int)
# Ensure incomes are within a realistic range (e.g., 0 to 200000)
income = np.clip(income, 0, 200000)

# Generate categorical feature
gender = np.random.choice(['Male', 'Female'], size=num_samples, p=[0.5, 0.5])

# Create a DataFrame with the new features
data_new = pd.DataFrame({
    'Age': ages,
    'Height': height,
    'Weight': weight,
    'Gender': gender,
    'Income': income
})

# Display the first few rows of the new dataset
print(data_new.head())

## Part 6 
## Hypothesis testing 

income_male = data_new[data_new['Gender'] == 'Male']['Income']
income_female = data_new[data_new['Gender'] == 'Female']['Income']

t_stat, p_value = ttest_ind(income_male, income_female)

# Display the t-statistic and p-value
print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")

# Interpretation of the results
if p_value < 0.05:
    print("There is a significant difference in Income between Male and Female.")
else:
    print("There is no significant difference in Income between Male and Female.")


## Part 2 
## Descriptive Statistics
# Calculate mean, median, standard deviation, and variance for Age, Height, Weight, and Income
statistics = pd.DataFrame({
    'Mean': data_new[['Age', 'Height', 'Weight', 'Income']].mean(),
    'Median': data_new[['Age', 'Height', 'Weight', 'Income']].median(),
    'Standard Deviation': data_new[['Age', 'Height', 'Weight', 'Income']].std(),
    'Variance': data_new[['Age', 'Height', 'Weight', 'Income']].var()
})


# Calculate the mode for Gender
gender_mode = data_new['Gender'].mode()[0]

# Display the statistics
print(statistics)
print(f"Mode for Gender: {gender_mode}")

## Part 3 
## Data Visualization 
# Plot histograms for Age, Height, Weight, and Income

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.hist(data_new['Age'], bins=30, color='skyblue', edgecolor='black')

plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.hist(data_new['Height'], bins=30, color='lightgreen', edgecolor='black')
plt.title('Histogram of Height')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 3)
plt.hist(data_new['Weight'], bins=30, color='lightcoral', edgecolor='black')
plt.title('Histogram of Weight')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 4)
plt.hist(data_new['Income'], bins=30, color='lightsalmon', edgecolor='black')
plt.title('Histogram of Income')
plt.xlabel('Income')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

## Using KDE Plots 
sns.set(style="whitegrid")

# Create KDE plots for Age, Height, Weight, and Income
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.kdeplot(data=data_new['Age'], fill=True, color="skyblue")
plt.title('KDE Plot of Age')
plt.xlabel('Age')
plt.ylabel('Density')

plt.subplot(2, 2, 2)
sns.kdeplot(data=data_new['Height'], fill=True, color="lightgreen")
plt.title('KDE Plot of Height')
plt.xlabel('Height (cm)')
plt.ylabel('Density')

plt.subplot(2, 2, 3)
sns.kdeplot(data=data_new['Weight'], fill=True, color="lightcoral")
plt.title('KDE Plot of Weight')
plt.xlabel('Weight (kg)')
plt.ylabel('Density')

plt.subplot(2, 2, 4)
sns.kdeplot(data=data_new['Income'], fill=True, color="lightsalmon")
plt.title('KDE Plot of Income')
plt.xlabel('Income')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

## Part 5 
## Boxplots to identify outliers 
# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Create boxplots for Age, Height, Weight, and Income
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.boxplot(x=data_new['Age'], color="skyblue")
plt.title('Boxplot of Age')
plt.xlabel('Age')

plt.subplot(2, 2, 2)
sns.boxplot(x=data_new['Height'], color="lightgreen")
plt.title('Boxplot of Height')
plt.xlabel('Height (cm)')

plt.subplot(2, 2, 3)
sns.boxplot(x=data_new['Weight'], color="lightcoral")
plt.title('Boxplot of Weight')
plt.xlabel('Weight (kg)')

plt.subplot(2, 2, 4)
sns.boxplot(x=data_new['Income'], color="lightsalmon")
plt.title('Boxplot of Income')
plt.xlabel('Income')

plt.tight_layout()
plt.show()

#Part6 
## Correlation Analysis 
# Calculate the Pearson correlation coefficient
correlation_matrix = data_new[['Age', 'Height', 'Weight', 'Income']].corr()

# Display the correlation matrix
print(correlation_matrix)

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
plt.show()


