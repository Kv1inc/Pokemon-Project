# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 21:44:36 2024

@author: kevin
"""

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
file_path = 'C:/Users/kevin/OneDrive/Documents/pokemontcg.csv'
pokemon_data = pd.read_csv(file_path)

# Step 2: Data cleaning
pokemon_data_clean = pokemon_data.rename(columns={
    'Portfolio Name': 'Portfolio',
    'Category': 'Category',
    'Set': 'Set',
    'Product Name': 'Card_Name',
    'Card Number': 'Card_Number',
    'Rarity': 'Rarity',
    'Variance': 'Variance',
    'Grade': 'Grade',
    'Average Cost Paid': 'Cost_Paid',
    'Quantity': 'Quantity',
    'Market Price (As of 2024-10-14)': 'Market_Price'
})

# Handle missing data by filling missing values in 'Cost_Paid' and 'Market_Price' with 0
pokemon_data_clean['Cost_Paid'] = pokemon_data_clean['Cost_Paid'].fillna(0)
pokemon_data_clean['Market_Price'] = pokemon_data_clean['Market_Price'].fillna(0)

# Ensure numeric columns are of the correct type
pokemon_data_clean['Quantity'] = pd.to_numeric(pokemon_data_clean['Quantity'], errors='coerce')
pokemon_data_clean['Cost_Paid'] = pd.to_numeric(pokemon_data_clean['Cost_Paid'], errors='coerce')
pokemon_data_clean['Market_Price'] = pd.to_numeric(pokemon_data_clean['Market_Price'], errors='coerce')

# Step 3: Analysis
# (1) Total market value of the collection
pokemon_data_clean['Total_Market_Value'] = pokemon_data_clean['Market_Price'] * pokemon_data_clean['Quantity']
total_market_value = pokemon_data_clean['Total_Market_Value'].sum()

# (2) Total cost paid for the collection
pokemon_data_clean['Total_Cost_Paid'] = pokemon_data_clean['Cost_Paid'] * pokemon_data_clean['Quantity']
total_cost_paid = pokemon_data_clean['Total_Cost_Paid'].sum()

# (3) Profit or loss
profit_or_loss = total_market_value - total_cost_paid

# (4) Rarity distribution
rarity_distribution = pokemon_data_clean.groupby('Rarity')['Quantity'].sum()

# (5) Top 5 most valuable cards
top_5_valuable_cards = pokemon_data_clean[['Card_Name', 'Total_Market_Value']].sort_values(by='Total_Market_Value', ascending=False).head(5)

# Display results
print(f"Total Market Value of Collection: ${total_market_value:.2f}")
print(f"Total Cost Paid for Collection: ${total_cost_paid:.2f}")
print(f"Profit/Loss: ${profit_or_loss:.2f}")
print("\nRarity Distribution:\n", rarity_distribution)
print("\nTop 5 Most Valuable Cards:\n", top_5_valuable_cards)

# Step 4: Visualizations

# Visualization 1: Bar chart for Rarity Distribution
plt.figure(figsize=(10, 6))
plt.bar(rarity_distribution.index, rarity_distribution.values, color='skyblue')
plt.title('Rarity Distribution of Pokémon Cards', fontsize=16)
plt.xlabel('Rarity', fontsize=12)
plt.ylabel('Number of Cards', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 2: Pie chart for Rarity Distribution
plt.figure(figsize=(8, 8))
plt.pie(rarity_distribution.values, labels=rarity_distribution.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Rarity Distribution of Pokémon Cards', fontsize=16)
plt.tight_layout()
plt.show()

# Visualization 3: Bar chart for Top 5 Most Valuable Cards
plt.figure(figsize=(10, 6))
plt.bar(top_5_valuable_cards['Card_Name'], top_5_valuable_cards['Total_Market_Value'], color='lightgreen')
plt.title('Top 5 Most Valuable Pokémon Cards', fontsize=16)
plt.xlabel('Card Name', fontsize=12)
plt.ylabel('Total Market Value ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
