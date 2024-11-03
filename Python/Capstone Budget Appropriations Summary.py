#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Define column headers based on your SQL query output
column_headers = [
    "budget_function_title", 
    "fr_entity_description", 
    "reporting_period_end", 
    "total_budgetary_resources_amount_cpe", 
    "gross_outlay_amount_by_tas_cpe", 
    "unobligated_balance_cpe", 
    "status_of_budgetary_resources_total_cpe", 
    "omnibus_flag"
]

# Load the CSV file with the specified headers
df = pd.read_csv("C:/Users/culex/OneDrive/Documents/CSU-Global/MIS581/Capstone Data/budget_appropriations_summary", header=None, names=column_headers)

# Display the first few rows to inspect
df.head()


# In[2]:


# Display summary information about the dataset
df.info()

# Show basic descriptive statistics for numeric columns
df.describe()


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns

# Histograms for each budget-related field
budget_columns = [
    "total_budgetary_resources_amount_cpe", 
    "gross_outlay_amount_by_tas_cpe", 
    "unobligated_balance_cpe", 
    "status_of_budgetary_resources_total_cpe"
]

for column in budget_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=50, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


# In[4]:


# Group by omnibus_flag and calculate the mean for each budget metric
omnibus_summary = df.groupby('omnibus_flag')[budget_columns].mean()

# Plotting
omnibus_summary.plot(kind='bar', figsize=(12, 8), stacked=True)
plt.title("Average Budgetary Resources and Balances by Omnibus vs. Non-Omnibus Years")
plt.xlabel("Omnibus Flag")
plt.ylabel("Average Amount")
plt.legend(title="Budget Metric", bbox_to_anchor=(1.05, 1))
plt.show()


# In[5]:


# Convert reporting_period_end to datetime
df['reporting_period_end'] = pd.to_datetime(df['reporting_period_end'])

# Group data by year and omnibus flag
df['year'] = df['reporting_period_end'].dt.year
year_summary = df.groupby(['year', 'omnibus_flag'])[budget_columns].mean().unstack()

# Plot trends over time for each metric
for column in budget_columns:
    year_summary[column].plot(figsize=(14, 7))
    plt.title(f"Yearly Trend in {column} (Omnibus vs. Non-Omnibus)")
    plt.xlabel("Year")
    plt.ylabel(column)
    plt.legend(title="Omnibus Flag")
    plt.show()


# In[6]:


# Correlation matrix
correlation_matrix = df[budget_columns].corr()

# Heatmap for visualization
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix of Budgetary Metrics")
plt.show()


# In[7]:


import scipy.stats as stats

# Separate the data by omnibus flag
omnibus_data = df[df['omnibus_flag'] == 'Omnibus']
non_omnibus_data = df[df['omnibus_flag'] == 'Non-Omnibus']

# T-Tests for each metric
t_test_total_budget = stats.ttest_ind(omnibus_data['total_budgetary_resources_amount_cpe'], non_omnibus_data['total_budgetary_resources_amount_cpe'])
t_test_gross_outlay = stats.ttest_ind(omnibus_data['gross_outlay_amount_by_tas_cpe'], non_omnibus_data['gross_outlay_amount_by_tas_cpe'])
t_test_unobligated_balance = stats.ttest_ind(omnibus_data['unobligated_balance_cpe'], non_omnibus_data['unobligated_balance_cpe'])
t_test_status_total = stats.ttest_ind(omnibus_data['status_of_budgetary_resources_total_cpe'], non_omnibus_data['status_of_budgetary_resources_total_cpe'])

# Mann-Whitney U Tests for each metric
mw_test_total_budget = stats.mannwhitneyu(omnibus_data['total_budgetary_resources_amount_cpe'], non_omnibus_data['total_budgetary_resources_amount_cpe'])
mw_test_gross_outlay = stats.mannwhitneyu(omnibus_data['gross_outlay_amount_by_tas_cpe'], non_omnibus_data['gross_outlay_amount_by_tas_cpe'])
mw_test_unobligated_balance = stats.mannwhitneyu(omnibus_data['unobligated_balance_cpe'], non_omnibus_data['unobligated_balance_cpe'])
mw_test_status_total = stats.mannwhitneyu(omnibus_data['status_of_budgetary_resources_total_cpe'], non_omnibus_data['status_of_budgetary_resources_total_cpe'])

# Print results
print("T-Test Results:")
print("Total Budgetary Resources:", t_test_total_budget)
print("Gross Outlay Amount:", t_test_gross_outlay)
print("Unobligated Balance:", t_test_unobligated_balance)
print("Status of Budgetary Resources:", t_test_status_total)

print("\nMann-Whitney U Test Results:")
print("Total Budgetary Resources:", mw_test_total_budget)
print("Gross Outlay Amount:", mw_test_gross_outlay)
print("Unobligated Balance:", mw_test_unobligated_balance)
print("Status of Budgetary Resources:", mw_test_status_total)


# In[8]:


# ANOVA and Kruskal-Wallis Tests
# ANOVA for Total Budgetary Resources by Year within Omnibus and Non-Omnibus categories
anova_total_budget_omnibus = stats.f_oneway(*(group['total_budgetary_resources_amount_cpe'] for name, group in omnibus_data.groupby(df['reporting_period_end'].dt.year)))
anova_total_budget_non_omnibus = stats.f_oneway(*(group['total_budgetary_resources_amount_cpe'] for name, group in non_omnibus_data.groupby(df['reporting_period_end'].dt.year)))

# Kruskal-Wallis Test for Total Budgetary Resources by Year within Omnibus and Non-Omnibus categories
kw_total_budget_omnibus = stats.kruskal(*(group['total_budgetary_resources_amount_cpe'] for name, group in omnibus_data.groupby(df['reporting_period_end'].dt.year)))
kw_total_budget_non_omnibus = stats.kruskal(*(group['total_budgetary_resources_amount_cpe'] for name, group in non_omnibus_data.groupby(df['reporting_period_end'].dt.year)))

# Print results
print("ANOVA Results by Year within Omnibus Flag:")
print("Omnibus Years:", anova_total_budget_omnibus)
print("Non-Omnibus Years:", anova_total_budget_non_omnibus)

print("\nKruskal-Wallis Results by Year within Omnibus Flag:")
print("Omnibus Years:", kw_total_budget_omnibus)
print("Non-Omnibus Years:", kw_total_budget_non_omnibus)


# In[9]:


# Selecting only numeric columns for correlation analysis
numeric_columns = ['total_budgetary_resources_amount_cpe', 
                   'gross_outlay_amount_by_tas_cpe', 
                   'unobligated_balance_cpe', 
                   'status_of_budgetary_resources_total_cpe']

# Pearson and Spearman correlations for Omnibus years (numeric columns only)
pearson_corr_omnibus = omnibus_data[numeric_columns].corr(method='pearson')
spearman_corr_omnibus = omnibus_data[numeric_columns].corr(method='spearman')

# Pearson and Spearman correlations for Non-Omnibus years (numeric columns only)
pearson_corr_non_omnibus = non_omnibus_data[numeric_columns].corr(method='pearson')
spearman_corr_non_omnibus = non_omnibus_data[numeric_columns].corr(method='spearman')

# Print results
print("Omnibus Year Correlations:")
print("Pearson:\n", pearson_corr_omnibus)
print("\nSpearman:\n", spearman_corr_omnibus)

print("\nNon-Omnibus Year Correlations:")
print("Pearson:\n", pearson_corr_non_omnibus)
print("\nSpearman:\n", spearman_corr_non_omnibus)


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt

# Box plot for total budgetary resources by omnibus flag
plt.figure(figsize=(10, 6))
sns.boxplot(x='omnibus_flag', y='total_budgetary_resources_amount_cpe', data=df)
plt.title("Total Budgetary Resources by Omnibus Flag")
plt.xlabel("Omnibus Flag")
plt.ylabel("Total Budgetary Resources Amount (CPE)")
plt.show()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the headers
column_headers = [
    "budget_function_title", 
    "fr_entity_description", 
    "reporting_period_end", 
    "total_budgetary_resources_amount_cpe", 
    "gross_outlay_amount_by_tas_cpe", 
    "unobligated_balance_cpe", 
    "status_of_budgetary_resources_total_cpe", 
    "omnibus_flag"
]

# Load the CSV file into a DataFrame with the specified headers
data = pd.read_csv("C:/Users/culex/OneDrive/Documents/CSU-Global/MIS581/Capstone Data/budget_appropriations_summary", header=None, names=column_headers)

# Convert 'omnibus_flag' to a categorical variable
data['omnibus_flag'] = data['omnibus_flag'].astype('category')

# 1. Boxplot for financial metrics by Omnibus vs Non-Omnibus Years
plt.figure(figsize=(12, 6))
sns.boxplot(x="omnibus_flag", y="total_budgetary_resources_amount_cpe", data=data)
plt.title("Total Budgetary Resources by Omnibus vs Non-Omnibus Years")
plt.xlabel("Omnibus Flag")
plt.ylabel("Total Budgetary Resources Amount (CPE)")
plt.show()

# Gross Outlay Amount
plt.figure(figsize=(12, 6))
sns.boxplot(x="omnibus_flag", y="gross_outlay_amount_by_tas_cpe", data=data)
plt.title("Gross Outlay Amount by Omnibus vs Non-Omnibus Years")
plt.xlabel("Omnibus Flag")
plt.ylabel("Gross Outlay Amount (CPE)")
plt.show()

# Unobligated Balance
plt.figure(figsize=(12, 6))
sns.boxplot(x="omnibus_flag", y="unobligated_balance_cpe", data=data)
plt.title("Unobligated Balance by Omnibus vs Non-Omnibus Years")
plt.xlabel("Omnibus Flag")
plt.ylabel("Unobligated Balance (CPE)")
plt.show()

# Status of Budgetary Resources Total
plt.figure(figsize=(12, 6))
sns.boxplot(x="omnibus_flag", y="status_of_budgetary_resources_total_cpe", data=data)
plt.title("Status of Budgetary Resources by Omnibus vs Non-Omnibus Years")
plt.xlabel("Omnibus Flag")
plt.ylabel("Status of Budgetary Resources Total (CPE)")
plt.show()


# In[12]:


# Convert reporting_period_end to datetime format
data['reporting_period_end'] = pd.to_datetime(data['reporting_period_end'])

# Line plot for Total Budgetary Resources over time
plt.figure(figsize=(14, 8))
sns.lineplot(x='reporting_period_end', y='total_budgetary_resources_amount_cpe', hue='omnibus_flag', data=data)
plt.title("Total Budgetary Resources Over Time by Omnibus Flag")
plt.xlabel("Reporting Period End")
plt.ylabel("Total Budgetary Resources Amount (CPE)")
plt.show()


# In[13]:


# Histogram for Total Budgetary Resources by Omnibus Flag
plt.figure(figsize=(12, 6))
sns.histplot(data, x='total_budgetary_resources_amount_cpe', hue='omnibus_flag', element='step', kde=True)
plt.title("Distribution of Total Budgetary Resources by Omnibus Flag")
plt.xlabel("Total Budgetary Resources Amount (CPE)")
plt.ylabel("Frequency")
plt.show()


# In[14]:


# Select only numeric columns for correlation
numeric_columns = data.select_dtypes(include=['float64', 'int64'])

# Filter data for Omnibus years and calculate correlations
omnibus_corr = numeric_columns[data['omnibus_flag'] == 'Omnibus'].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(omnibus_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Financial Metrics in Omnibus Years")
plt.show()

# Filter data for Non-Omnibus years and calculate correlations
non_omnibus_corr = numeric_columns[data['omnibus_flag'] == 'Non-Omnibus'].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(non_omnibus_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Financial Metrics in Non-Omnibus Years")
plt.show()


# In[15]:


# Group by budget_function_title and omnibus_flag
grouped_data = data.groupby(['budget_function_title', 'omnibus_flag'])['total_budgetary_resources_amount_cpe'].mean().reset_index()

# Bar plot
plt.figure(figsize=(14, 10))
sns.barplot(x='total_budgetary_resources_amount_cpe', y='budget_function_title', hue='omnibus_flag', data=grouped_data, dodge=True)
plt.title("Average Total Budgetary Resources by Budget Function and Omnibus Flag")
plt.xlabel("Average Total Budgetary Resources Amount (CPE)")
plt.ylabel("Budget Function Title")
plt.show()


# In[16]:


# Extract fiscal year from reporting_period_end
data['fiscal_year'] = data['reporting_period_end'].dt.year

# Boxplot for Total Budgetary Resources by Year and Omnibus Flag
plt.figure(figsize=(14, 8))
sns.boxplot(x='fiscal_year', y='total_budgetary_resources_amount_cpe', hue='omnibus_flag', data=data)
plt.title("Total Budgetary Resources by Fiscal Year and Omnibus Flag")
plt.xlabel("Fiscal Year")
plt.ylabel("Total Budgetary Resources Amount (CPE)")
plt.xticks(rotation=45)
plt.show()


# In[ ]:




