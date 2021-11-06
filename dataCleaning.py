import pandas as pd
import numpy as np 
import os

pd.set_option('display.max_columns', None)

os.chdir('/Users/monroefarris/Desktop')
fileName = 'MERGED2019_20_PP.csv'
originalData = pd.read_csv(fileName)
cleanData = pd.DataFrame()

cleanData['University Name'] = originalData['INSTNM']
cleanData['University City'] = originalData['CITY']
cleanData['University State'] = originalData['STABBR']
cleanData['Most Awarded Decree'] = originalData['PREDDEG']
cleanData['Predominantly Black'] = originalData['PBI']
cleanData['Admission Rate'] = round(originalData['ADM_RATE'] * 100, 2) 
cleanData['SAT Average'] = originalData['SAT_AVG']
cleanData['SAT Reading Mid'] = originalData['SATVRMID']
cleanData['SAT Math Mid'] = originalData['SATMTMID']
cleanData['ACT Cumulative Average'] = originalData['ACTCMMID']
cleanData['Undergraduate Enrollment'] = originalData['UGDS']
cleanData['Percent of Students (White)'] = round(originalData['UGDS_WHITE'] * 100, 2) 
cleanData['Percent of Students (Black)'] = round(originalData['UGDS_BLACK'] * 100, 2)
cleanData['Percent of Students (Hispanic)'] = round(originalData['UGDS_HISP'] * 100, 2)
cleanData['Percent of Students (Asian)'] = round(originalData['UGDS_ASIAN'] * 100, 2) 
cleanData['Average Cost per Academic Year'] = originalData['COSTT4_A']
cleanData['In State Tuition and Fees'] = originalData['TUITIONFEE_IN']
cleanData['Out of State Tuition and Fees'] = originalData['TUITIONFEE_OUT']
cleanData['Completion Rate (4-year institutions'] = round(originalData['C150_4'], 2) 
cleanData['Year'] = fileName.split('MERGED')[1].split('_PP')[0]

for i in range(len(cleanData)):
    if cleanData['Most Awarded Decree'][i] == 3:
        cleanData['Most Awarded Decree'][i] = "Bachelor's"
    elif cleanData['Most Awarded Decree'][i] == 2:
        cleanData['Most Awarded Decree'][i] = "Associate's"
    elif cleanData['Most Awarded Decree'][i] == 1:
        cleanData['Most Awarded Decree'][i] = "Certificate"
    elif cleanData['Most Awarded Decree'][i] == 4:
        cleanData['Most Awarded Decree'][i] = "Graduate"
    elif cleanData['Most Awarded Decree'][i] == 0:
        cleanData['Most Awarded Decree'][i] = "Not Classified"

    if cleanData['Predominantly Black'][i] == 1:
        cleanData['Predominantly Black'][i] = 'YES'
    else: 
        cleanData['Predominantly Black'][i] = 'NO'

cleanData = cleanData[['Year'] + [col for col in cleanData.columns if col != 'Year']]

print(cleanData)

cleanData.to_csv('initialCleaning.csv')

