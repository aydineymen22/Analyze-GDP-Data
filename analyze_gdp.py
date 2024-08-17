import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
all_data = pd.read_csv('all_data.csv')

# print(all_data.head())

countries= np.unique(all_data['Country'])

#Showing how life expectancy changes over years for each country in the data
def changing_in_life_expectancy():
    titles = [
    'Change of Life Expectancy in Years for Chile', 'Change of Life Expectancy in Years for China',
    'Change of Life Expectancy in Years for Germany','Change of Life Expectancy in Years for Mexico',
    'Change of Life Expectancy in Years for United States of America','Change of Life Expectancy in Years for Zimbabwe'
    ]

    for i, (country, title) in enumerate(zip(countries, titles), start=1):
        plt.subplot(3,2,i)
        plt.title(title)
        country_data = all_data[all_data['Country'] == country]
        plt.plot('Year', 'Life expectancy at birth (years)', marker='o', data=country_data)

        

    plt.tight_layout()
    plt.show()
    plt.clf()




# this plot shows life expectancies of countries
def comparing_countries_life_expectancy():
    mean_life_expectancy = all_data.groupby('Country')['Life expectancy at birth (years)'].mean().reset_index()

    sns.barplot(x='Country', y='Life expectancy at birth (years)', data=mean_life_expectancy)
    plt.xticks(rotation=30)
    plt.show()



# Plotting change of GDP over years for each country in all_data.csv
def changing_countries_gdp():
    titles = [
    'Change of GDP in Years for Chile', 'Change of GDP in Years for China',
    'Change of GDP in Years for Germany','Change of GDP in Years for Mexico',
    'Change of GDP in Years for United States of America','Change of GDP in Years for Zimbabwe'
    ]


    plt.figure(figsize=(15,10))
    for i, (country, title) in enumerate(zip(countries, titles), start=1):
        plt.subplot(3,2,i)
        plt.title(title)
        countries_data = all_data[all_data['Country'] == country]

        plt.plot('Year', 'GDP', marker='o', data=countries_data)
    
    plt.tight_layout()
    plt.show()
    plt.clf()



# Searching for the correlation between GDP and Life Expectancy
def corr_gdp_life_expectancy():
    plt.scatter(all_data['GDP'], all_data['Life expectancy at birth (years)'], alpha=0.5)

    plt.title('Relationship between GDP and Life Expectancy')
    plt.xlabel('GDP')
    plt.ylabel('Life Expectancy')


    slope, intercept, r_value, p_value, std_error = stats.linregress(all_data['GDP'], all_data['Life expectancy at birth (years)'])
    r_squared = r_value ** 2

    trendline = slope * all_data['GDP'] + intercept

    plt.plot(all_data['GDP'], trendline, color='r', linestyle = '--', label='Trendline')

    plt.annotate(f'Correlation: {r_value:.2f}\nR-squared: {r_squared:.2f}', xy=(0.77, 0.45), xycoords='axes fraction')

    plt.tight_layout()
    plt.show()




#Showing how life expectancy is distributed
def distribution_of_life_expectancy():

    plt.figure(figsize=(10, 6))


    sns.boxplot(x=all_data['Life expectancy at birth (years)'], 
                color="skyblue", 
                linewidth=2.5)

    plt.title('Distribution of Life Expectancy at Birth (Years)', fontsize=16, fontweight='bold')
    plt.xlabel('Life Expectancy (Years)', fontsize=14)

    plt.grid(True, linestyle='--', alpha=0.7)

    sns.despine(trim=True)

    plt.show()


