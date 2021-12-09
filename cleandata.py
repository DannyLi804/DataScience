"""
Name: Danny Li

Title: Does F1 Research Trickle Down to Consumer-Grade Vehicles

Resources: https://f1metrics.wordpress.com/2015/05/01/how-money-predicts-success-in-for
mula-1/, https://www.eia.gov/environment/emissions/state/, https://www.fia.com/sites/default/files/2021_formula_1_technical_regulations_-_is
s_7_-_2020-12-16.pdf, https://www.fia.com/sites/default/files/regulation/file/2013%20F1TECHNICAL%20REGULATIONS%20-%20PUBLISHED%20ON%2004.07.2013.pdf, https://www.fia.com/sites/default/files/2021_formula_1_sporting_regulations_-_iss_5_-_2020-12-16.pdf, https://www.fia.com/regulation/category/761, https://www.f1technical.net/articles/19, https://www.fueleconomy.gov/feg/pdfs/guides/FEG2021.pdf 

URL:https://dannyli804.github.io/DataScience/
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def CleanF1result():
    df=pd.read_csv('results.csv')
    df1=df[df['position']=='1']
    df2=df[df['position']=='2']
    df3=df[df['position']=='3']
    df4=df[df['position']=='4']
    df5=df[df['position']=='5']
    newdf=pd.concat([df1,df2,df3,df4,df5])
    newdf=newdf.sort_values(by='resultId')
    newdf.to_csv('result1-2.csv',index=False,columns=['resultId','raceId','constructorId','position'])
def mergeF1():
    df=pd.read_csv('result1-2.csv')
    
    df1=pd.read_csv('races.csv')
    df1=df1[['raceId','year']]
    
    df2=pd.read_csv('constructors.csv')
    df2=df2[['constructorId','name']]
    
    newdf=pd.merge(df,df1,on='raceId',how='left')
    lastdf=pd.merge(newdf,df2,on='constructorId',how='left')
    lastdf['year']=pd.to_numeric(lastdf['year'])
    lastdf=lastdf[lastdf['year']>=1998]
    lastdf=lastdf.sort_values(by=['year','position'])
    lastdf['name']=lastdf['name'].apply(upperCaseName)
    lastdf['name']=lastdf['name'].apply(cleanF1Name)
    lastdf.to_csv('finishingdata.csv',index=False)
def nycgraphCO2Emission():
    df=pd.read_csv('newyorkCO2emission.csv')
    df=df[df['Sector']=='Fuel Totals']
    year=[1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
    coal=[29.1,28.7,27,25.1,28,28.2,23.7,27.6,31.2,34.1,33.2,33.5,33.8,30.9,30,28.9,29.5,30.8,32,30.2,31.4,29.2,26.7,27.3,26.4,24.5,24.4,24.6,21.8,14.9,15.9,11.9,6.9,6.5,6.2,3.9,2.8,1.9,1.6]
    petrol=[155,137.1,127.8,114.9,112.8,118.6,128.1,131.8,135.1,134.2,127.5,118.3,110.3,109.1,104.1,100.1,105.6,102.1,104.1,105.6,112.4,112.8,108.5,123.8,127.2,126.3,107.2,108.6,102,95.3,104.8,97.6,94.1,93.7,97.8,97.6,97.2,97.3,100.4]
    gas=[40.1,41.2,42.1,39.3,43,41.6,39.8,42.5,43.1,46.2,47.5,48.7,54.9,54.3,58.1,68.7,65.3,72.1,67.2,69.4,67.9,64,65.1,60,59.8,58.7,59.4,64.4,63.9,61.9,65,66.2,66.9,69.8,73.9,74.1,70.9,67.7,73.9]
    total=[224.2,207,196.9,179.2,183.9,188.5,191.6,202,209.5,214.5,208.2,200.5,199,194.2,192.2,197.8,200.5,204.9,203.4,205.2,211.7,205.9,200.3,211,213.3,209.6,191.1,197.7,187.8,172.1,185.7,175.7,168,170,177.8,175.6,171,166.9,175.9]
        
    plt.plot(year,coal,label='Coal')
    plt.plot(year,petrol,label='Petrol')
    plt.plot(year,total,label='Total')
    plt.plot(year,gas,label='Gas')
    plt.title('New York CO2 Emission')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emission(million metric tons)')
    plt.legend()
    plt.show()
def piechartCO2BySector():
    
    total=[224.2,207,196.9,179.2,183.9,188.5,191.6,202,209.5,214.5,208.2,200.5,199,194.2,192.2,197.8,200.5,204.9,203.4,205.2,211.7,205.9,200.3,211,213.3,209.6,191.1,197.7,187.8,172.1,185.7,175.7,168,170,177.8,175.6,171,166.9,175.9]
    transport=[71.7,67.2,60.1,54.2,49.3,58,59.2,62.5,59.7,59.9,63.8,62.3,60.8,61.7,60.6,62.4,65.7,65.6,66,66.5,66.9,66.7,68.4,73.2,74.9,73.2,74.2,73.6,73,71,82.6,77.3,75.6,76.4,80.9,79.1,82.3,82.9,83.3]
    industrial=[34.4,29.3,25.6,19.8,22.6,21.4,18.6,19.6,19.9,20.4,19.1,18.5,19.3,20,20.3,22.2,22.8,22,20.6,16.3,16.5,14.2,12.8,12.5,11.9,12.4,11.7,11.3,10.6,8.7,9.2,9.4,9,9.2,9,9.1,8.5,8.5,8.6]
    commercial=[28.8,22.8,25.8,21.9,25.7,24.9,28.6,27.3,27.7,27.4,27.2,26.8,27.8,28.5,28,27.2,28,29.8,27.8,30.3,32.2,30.8,31.3,33.2,34.9,28.7,25.5,26.8,25.9,25.2,24.3,24.3,21,22.4,22,22.8,21.7,22.1,23.2]
    resident=[35.6,34.5,33.6,31.5,35.4,34.4,36.4,38.3,40,38.5,33.6,32.9,36.3,35.7,35.3,34.3,36.6,34.7,31.6,34.3,39.3,38.2,36,39.1,38.1,39.1,32.5,36.2,34.9,32.5,31.3,30.8,30,31.9,35.2,35.3,30.7,31.3,36.3]
    electric=[53.7,53.2,51.7,51.9,50.9,49.7,48.8,54.2,62.2,68.3,64.5,60,54.8,48.3,48.1,51.8,47.4,52.9,57.3,57.8,56.9,56.1,51.8,53.2,53.6,56.2,47.2,49.9,43.3,34.6,38.2,33.9,32.3,30.1,30.6,29.2,27.8,22.1,24.5]
    year=[1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
    for x in range(0,len(total),1):
        transport[x]=round(((transport[x]/total[x])*100),2)
        industrial[x]=round(((industrial[x]/total[x])*100),2)
        commercial[x]=round(((commercial[x]/total[x])*100),2)
        resident[x]=round(((resident[x]/total[x])*100),2)
        electric[x]=round(((electric[x]/total[x])*100),2)
    plt.plot(year,transport,label='Transportation')
    plt.plot(year,industrial,label='Industrial')
    plt.plot(year,commercial,label='Commerical')
    plt.plot(year,resident,label='Residential')
    plt.plot(year,electric,label='Electrical')
    plt.xlabel('Year')
    plt.ylabel('Total CO2 Emission(%)')
    plt.title('CO2 Emission by Sector')
    plt.legend()
    plt.show()

    y=[]
    y.append(round(sum(transport)/len(transport),2))
    y.append(round(sum(industrial)/len(industrial),2))
    y.append(round(sum(commercial)/len(commercial),2))
    y.append(round(sum(resident)/len(resident),2))
    y.append(round(sum(electric)/len(electric),2))
    mylabel=['Transportation','Industrial','Commerical','Residential', 'Electrical']
    myexplode=[0.1,0,0,0,0]
    plt.pie(y,labels=mylabel,explode=myexplode,autopct='%1.1f%%',shadow=True)
    plt.title('Average CO2 Emission by Sector')
    plt.legend()
    plt.show()
def upperCaseName(word):
    word=word.upper()
    return word   
def cleanF1Name(word):
    word=word.replace('ALPINE F1 TEAM','ALPINA')
    word=word.replace('BMW SAUBER','BMW')
    word=word.replace('RED BULL','HONDA')
    word=word.replace('MCLAREN','MCLAREN AUTOMOTIVE')
    word=word.replace('MERCEDES','MERCEDES-BENZ')
    return word
def cleanName(word):
    
    word=word.replace('CHRYSLER GROUP LLC','CHRYSLER')
    word=word.replace('GM','GENERAL MOTORS')
    word=word.replace('GENERAL MOTORSC','GENERAL MOTORS')
    word=word.replace('FORD MOTOR COMPANY','FORD')
    word=word.replace('JAGUAR CARS','JAGUAR')
    word=word.replace('JAGUAR LAND ROVER L','JAGUAR')
    word=word.replace('MITSUBISHI MOTORS CO','MITSUBISHI')
    word=word.replace('MITSUBISHI MOTORS NA','MITSUBISHI') 
    word=word.replace('MCLAREN AUTOMOTIVE ','MCLAREN AUTOMOTIVE')  
    word=word.replace('QUANTUM FUEL SYSTEM','QUANTUM') 
    word=word.replace('SAAB CARS NORTH AMERICA','SAAB') 
    word=word.replace('ROUSH PERFORMANCE','ROUSH') 
    word=word.replace('SPYKR','SPYKER')
    word=word.replace('SUBARU TECNICA INTE','SUBARU')
    word=word.replace('VOLKSWAGEN GROUP OF','VOLKSWAGEN')
    word=word.replace('VOLKSWAGENGROUPOF','VOLKSWAGEN')
    word=word.replace('VW','VOLKSWAGEN')
    return word
def cleanMPG():
    count=2022
    while count>1997:
        if count>2009:
           
            df=pd.read_excel(str(count)+'.xlsx', index_col=0)
            
                
            try:
                groupdf=df.groupby(['Mfr Name']).mean()
                groupdf=groupdf.reset_index()
            except:
                groupdf=df.groupby(['Mfr Name ']).mean()
                groupdf=groupdf.reset_index()
                groupdf=groupdf.rename(columns={'Mfr Name ':'Mfr Name'})
            groupdf['Year']=str(count)
            try:
                groupdf=groupdf[['Year','Mfr Name','Comb FE (Guide) - Conventional Fuel','Comb CO2 Rounded Adjusted (as shown on FE Label)']]
            except:
                groupdf=groupdf[['Year','Mfr Name','Comb FE (Guide) - Conventional Fuel']]
            groupdf.to_csv(str(count)+'.csv',index=False)
            count=count-1
        elif count==2008 or count<=2006 and count>=2003 or count<=1999:
            df=pd.read_csv(str(count)+'.csv',error_bad_lines=False)
            try:
                groupdf=df.groupby(['MFR']).mean()
            except:
                groupdf=df.groupby(['Manufacturer']).mean()
            groupdf['Year']=str(count)
            groupdf=groupdf.reset_index()
            try:
                groupdf=groupdf[['Year','MFR','COMB MPG (GUIDE)']]
            except:
                groupdf=groupdf[['Year','Manufacturer','cmb']]
            groupdf.to_csv(str(count)+'.csv',index=False)
            count=count-1    
        
        else:
            df=pd.read_excel(str(count)+'.xls')
            try:
                groupdf=df.groupby(['MFR']).mean()
            except:
                groupdf=df.groupby(['Manufacturer']).mean()
            groupdf['Year']=str(count)
            groupdf=groupdf.reset_index()
            try:
                groupdf=groupdf[['Year','MFR','COMB MPG (GUIDE)']]
            except:
                groupdf=groupdf[['Year','Manufacturer','cmb']]
            groupdf.to_csv(str(count)+'.csv',index=False)
            count=count-1
            #COMB MPG (GUIDE)
def cleanColName():
    count=2022
    while count>1997:
        df=pd.read_csv(str(count)+'.csv') 
        if count>2009:   
            df=df.rename(columns={'Comb FE (Guide) - Conventional Fuel':'COMB MPG'})
            df=df.rename(columns={'Comb CO2 Rounded Adjusted (as shown on FE Label)':'COMB CO2'})
        elif count<=2009 and count>2005:
            df=df.rename(columns={'MFR':'Mfr Name'})
            df=df.rename(columns={'COMB MPG (GUIDE)':'COMB MPG'})
            
        else:
            df=df.rename(columns={'Manufacturer':'Mfr Name'})
            df=df.rename(columns={'cmb':'COMB MPG'})
        df.to_csv(str(count)+'.csv',index=False)
        count=count-1
def addingMPGcsv():
    count=2022
    while count>1998:
        df=pd.read_csv('2022.csv')
        df1=pd.read_csv(str(count-1)+'.csv')
        df=pd.concat([df,df1])
        df.to_csv('2022.csv',index=False)
        count=count-1
def cleanMfrName():
    df=pd.read_csv('2022.csv')
    df['Mfr Name']=df['Mfr Name'].apply(upperCaseName)
    df['Mfr Name']=df['Mfr Name'].apply(cleanName)
    df.to_csv('MPGConcat.csv',index=False)  
def plotStanding():

    df=pd.read_csv('finishingdata.csv')
    dfnew=df.groupby(['year','name']).mean()
    dfnew=dfnew.sort_values(['year','position']).groupby('year').head(5)
    positions=[]
    count=1
    for i in range(len(dfnew.index)):
        if count<5:
            positions.append(count)
            count+=1
        else:
            positions.append(count)
            count=1
    dfnew['position']=positions
    dfnew=dfnew.reset_index()
    
    data=[]
    #list1=dfnew['name'].unique()
    for x in range(1,6,1):
        dfposition=dfnew[dfnew['position']==x]
        list1=dfposition['name'].tolist()
        data.append(list1)
    
    val1 = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021] 
    val2 = ['First','Second','Third','Fourth','Fifth'] 
    val3 = data 

    fig, ax = plt.subplots() 
    ax.set_axis_off() 
    table = ax.table( 
        cellText = val3,
        rowLabels = val2,
        colLabels = val1, 
        rowColours =["palegreen"] * len(val2),
        colColours =["palegreen"] * len(val1), 
        cellLoc ='center',
        loc ='upper left'
        )

    ax.set_title('F1 Standings', 
                fontweight ="bold") 
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(3,3)
    plt.title('F1 Standings')
    plt.show()
"""  
    for i in list1:
        dfmfr=dfnew[dfnew['name']==i]
        x=dfmfr['year'].tolist()
        y=dfmfr['position'].tolist()
        plt.scatter(x,y,label=i)
        
        
        for j,k in zip(x,y):
            if j%2==0:
                plt.annotate(i,xy=(j,k),xytext=(j,k-.30),ha='center',arrowprops=dict(arrowstyle="->", color='black'))
            else:
                plt.annotate(i,xy=(j,k),xytext=(j,k-.15),ha='center',arrowprops=dict(arrowstyle="->", color='black'))
            
        
    ax = plt.gca()
    ax.set_ylim([6, 0])
    plt.xticks([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,2021])
    plt.xticks(rotation=45)
    plt.ylabel('Placement')
    plt.xlabel('Year')
    plt.show()
"""
    

#CleanF1result()
#mergeF1()
#nycgraphCO2Emission()
#piechartCO2BySector()
#cleanMPG()
#cleanColName()
#addingMPGcsv()
#cleanMfrName()
plotStanding()
