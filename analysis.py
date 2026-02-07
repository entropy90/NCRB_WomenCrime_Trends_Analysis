from matplotlib import pyplot as plt
import pandas as pd
#1Load the dataset
df=pd.read_csv("NCRB_CII_2020_Cleaned (2).csv")
#Look at first 5 rows
print(df.head())
#check structure
print(df.info())
#2specific crime only
crimes_only = df[df['Audit_Total'] == False].copy()
print("step 1 & 2 Complete: Data loaded and filtered.")
# 3. AUDIT: Let's check if the math adds up
#Total should = Pending from prev year+new Cases+Reopened cases crimes_only['Calculated_Total']= 
(crimes_only['Pending_Previous_Year']+
crimes_only['Cases_Reported']+
crimes_only['Cases_Reopened']
)
#check if there is any difference
crimes_only['Difference'] = crimes_only['Total_Cases_for_Investigation'] - crimes_only['Audit_Total']
#Find rows where the math is wrong
errors = crimes_only[crimes_only['Difference'] !=0]
if errors.empty:
    print("Audit Pass: All totals match the sum of their parts!")
else: 
    print(f"Audit Warning:Found {len(errors)}) rows with math discrepancies.") 
#Ranking: what are the top 5 most reported crime?
top_5_reported = crimes_only.sort_values(by='Cases_Reported',ascending=False).head(5)
print("\n-- Top 5 Reported Crimes Against women---")
#Print the name and number of cases
print(top_5_reported[['Crime_Category','Cases_Reported']])

#Visualize: Bar Chart Creation
plt.style.use('ggplot')
plt.figure(figsize=(10,6))

#Bar Creation
plt.barh(top_5_reported['Crime_Category'], top_5_reported['Cases_Reported'],facecolor='skyblue', edgecolor='navy')

#Addition of Labels and Title
plt.xlabel('Number of Cases Reported')
plt.ylabel('Crime Category')
plt.title('Top 5 Most Reported Crimes Against Women(NCRB 2020)')

#Inverting the list so the #1 crime is at the top
plt.gca().invert_yaxis()

#Chart as an image
plt.tight_layout()
plt.savefig('top_crimes_chart.png')
plt.show()
print("\nAnalysis complete! Chart saved as 'top_crimes_chart.png'")

print("i like aditya")
