import pandas as pd


df=pd.read_csv('results.csv')
df1=df[df['position']=='1']
df2=df[df['position']=='2']
newdf=pd.concat([df1,df2])
newdf=newdf.sort_values(by='resultId')
newdf.to_csv('result1-2.csv',index=False,columns=['resultId','raceId','constructorId','position'])
print(newdf)