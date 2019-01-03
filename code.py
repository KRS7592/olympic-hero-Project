# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

data=pd.read_csv(path)
data.rename_axis(mapper={'Total':'Total_Medals'},axis=1,inplace=True)
data.head()

#Code starts here




# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter'))

better_event=data['Better_Event'].value_counts().index[0]


# --------------
#Code starts here

top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
drp=len(top_countries)-1

top_countries.drop(top_countries.index[drp],inplace=True)
len(top_countries)

def top_ten(df,cln):
    country_list=[]
    
    country_list=list(df.nlargest(10,cln)['Country_Name'])
    return country_list

top_10_summer= top_ten(top_countries,'Total_Summer')
top_10_winter=  top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

common=[]

common=list(set(top_10)&set(top_10_winter)&set(top_10_summer))



# --------------
#Code starts here

summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer',figsize=(15,15))
winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter',figsize=(15,15))
top_df.plot(kind='bar',x='Country_Name',y='Total_Medals',figsize=(15,15))


# --------------
#Code starts here

#Write a function to do it all 
def doit(df,a):
    if a=='Total':
        df['Golden_Ratio']=df.apply(lambda x:x.Gold_Total/ x.Total_Medals,axis =1)
    else :
        gold='Gold_'+str(a)
        total='Total_'+str(a)
        df['Golden_Ratio']=df[gold]/df[total]
    x=df['Golden_Ratio'].max()
    y=df[df['Golden_Ratio']==x]['Country_Name'].tolist()
    return (df,x,y[0])

summer_df,summer_max_ratio,summer_country_gold=doit(summer_df,'Summer')

winter_df,winter_max_ratio,winter_country_gold=doit(winter_df,'Winter')

top_df,top_max_ratio,top_country_gold=doit(top_df,'Total')


print("Summer "+str(summer_max_ratio)+" : "+str(summer_country_gold))
print("Winter "+str(winter_max_ratio)+" : "+str(winter_country_gold))
print("Top "+str(top_max_ratio)+" : "+str(top_country_gold))


# --------------
#Code starts here
data_1=data.drop(data.tail(1).index,inplace=False)

data_1['Total_Points']=3*data_1['Gold_Total']+2*data_1['Silver_Total']+data_1['Bronze_Total']

most_points=data_1['Total_Points'].max()
best_country=data_1[data_1['Total_Points']==most_points]['Country_Name'].tolist()[0]


# --------------
#Code starts here

best=data[data['Country_Name']==best_country][['Gold_Total','Silver_Total','Bronze_Total']]


best.plot(stacked=True).bar(x='Country_Name',height=['Gold_Total','Silver_Total','Bronze_Total'])
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)




