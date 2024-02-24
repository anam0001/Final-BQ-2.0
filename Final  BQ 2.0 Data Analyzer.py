#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_column(data, column):
    print("\n" + "="*40)
    print(f"Analysis for column '{column}':")
    column_data = data[column]

    if column_data.dtype == 'object':
        print("\nCategorical Data:")
        print(column_data.value_counts())

        # Additional statistics for categorical data
        total_count = len(column_data)
        percentage_per_category = (column_data.value_counts() / total_count) * 100
        print("\nPercentage per category:")
        print(percentage_per_category)
        
        
        custom_colors = ['saddlebrown','teal','maroon', 'navy', 'g', 'darkgoldenrod','darkslategrey','purple','dimgrey','dodgerblue']
        if len(column_data.unique()) <= 10:  # Limiting to 10 categories for pie or bar chart
            plt.figure(figsize=(8, 6))
            column_data.value_counts().plot(kind='pie', colors=custom_colors, autopct='%1.1f%%', startangle=140)
            plt.title(f"{column} Distribution", fontsize=20, fontweight='bold', color='saddlebrown', fontname='Times new roman')
            plt.ylabel('')
            plt.legend()
            plt.show()
        else:
            plt.figure(figsize=(10, 6))
            column_data.value_counts().plot(kind='bar', color='palegoldenrod',edgecolor='saddlebrown')
            plt.title(f"{column} Distribution", fontsize=20, fontweight='bold', color='saddlebrown', fontname='Times new roman')
            plt.xlabel(column, fontsize=16, fontweight='bold', color='saddlebrown', fontname='Times new roman')
            plt.ylabel('Count', fontsize=16, fontweight='bold', color='saddlebrown', fontname='Times new roman')
            plt.xticks(fontsize=10, fontweight='bold', color='saddlebrown', fontname='Arial')
            plt.yticks(fontsize=10, fontweight='bold', color='saddlebrown', fontname='Arial')
            plt.tight_layout()
            plt.show()

    elif column_data.dtype in ['int64', 'float64']:
        print("\nNumerical Data:")
        print(column_data.describe())
        print("\nSeven-number statistical summary:")
        print("Minimum:", column_data.min())
        print("25th percentile:", column_data.quantile(0.25))
        print("Median:", column_data.median())
        print("75th percentile:", column_data.quantile(0.75))
        print("Maximum:", column_data.max())
        print("Mean:", column_data.mean())
        print("Standard deviation:", column_data.std())

        plt.figure(figsize=(8, 6))
        if len(column_data.unique()) <= 10:  # Limiting to 10 unique values for box plot
            sns.boxplot(column_data)
        else:
            sns.histplot(column_data, edgecolor='saddlebrown', color="moccasin",linewidth=2)
            plt.title(f"{column} Distribution", fontsize=20, fontweight='bold', color='saddlebrown', fontname='Times new roman')
            plt.xlabel(column, fontsize=16, fontweight='bold', color='saddlebrown', fontname='Times new roman')
            plt.ylabel('Frequency' if len(column_data.unique()) > 10 else 'Count', fontsize=16, fontweight='bold', color='saddlebrown', fontname='Times new roman')
            plt.xticks(fontsize=10, fontweight='bold', color='saddlebrown', fontname='Arial')
            plt.yticks(fontsize=10, fontweight='bold', color='saddlebrown', fontname='Arial')
            plt.show()
    else:
        print("Unsupported data type for analysis.")

def main():
    while True:
        print("\n" + "="*40)
        print("MENU:")
        print("1. Analyze Dataset")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Load dataset
            file_path = input("Enter the path to the dataset (CSV file): ")
            try:
                data = pd.read_csv(file_path)
            except FileNotFoundError:
                print("File not found.")
                continue
            except Exception as e:
                print("An error occursaddlebrown while loading the dataset:", e)
                continue

            # Analyze each column
            for column in data.columns:
                analyze_column(data, column)

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()


# In[ ]:




