"""fifth challenge from 'Data Analysis with Python Projects'
on FreeCodeCamp.org
"""

from os import X_OK
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.DataFrame(pd.read_csv('epa-sea-level.csv'))
    yA_csiro = df['CSIRO Adjusted Sea Level']
    xA_years = df['Year']
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(xA_years, yA_csiro)
    ax.set_ylabel('CSIRO Adjusted Sea Level')
    ax.set_xlabel('Year')

    # Create first line of best fit
    regressionA = linregress(xA_years, yA_csiro)
    xA_years = pd.Series(list(i for i in range(1880, 2051)))
    yA_csiro = xA_years*regressionA.slope + regressionA.intercept
    ax.plot(xA_years, yA_csiro, 'r', label='fitted line')
    ax.legend()

    # Create second line of best fit
    xB_years = df[df['Year'] >= 2000]['Year']
    yB_csiro = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    regressionB = linregress(xB_years, yB_csiro)

    xB_years = pd.Series(list(i for i in range(2000, 2051)))
    yB_csiro = xB_years*regressionB.slope + regressionB.intercept
    ax.plot(xB_years, yB_csiro, 'g', label='fitted line 2000 data onwards')
    ax.legend()

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    plt.tight_layout()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
