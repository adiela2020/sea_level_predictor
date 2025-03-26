import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('epa-sea-level.csv')

# scatter plot
plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

from scipy.stats import linregress

# Get slope and intercept
slope, intercept = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])[:2] 
years = pd.Series(range(1880,2051))

# line of best fit
plt.plot(years.values,slope*years.values + intercept, label ='First line of best fit')


# new line of best fit
df2 = df[df['Year']>=2000]
slope2,intercept2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])[:2]
years2 = pd.Series(range(2000,2051))

# label of title, x and y axis
plt.plot(years2.values,slope2*years2.values + intercept2, label ='Second line of best fit')

plt.legend()
plt.xlabel('Years')
plt.title('Rise in Sea Level')
plt.ylabel('Sea Level (inches)')