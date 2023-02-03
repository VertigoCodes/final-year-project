#LIBRARY IMPORTS
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("Welcome to FYP Project.")
print("For the first phase of this project, we will be looking at the data that we will be working with in a presentable manner and try to gain some insights and inferences from the data to forumlate our hypotheses.")

trichyHousingInfo = pd.read_csv('Trichy Housing Info .csv')

retainColumns = ['Total/ Rural/ Urban', 'Total - Persons', 'Total - Males', 'Total - Females', 'Scheduled Caste - Persons', 'Scheduled Caste - Males', 'Scheduled Caste - Females', 'Scheduled Tribe - Persons', 'Scheduled Tribe - Males', 'Scheduled Tribe - Females']
trichyHousing = trichyHousingInfo[retainColumns]

print(trichyHousing.head())
'''
plt.figure(figsize=(12,8))

sns.barplot(data=trichyHousing)
plt.show()

'''


