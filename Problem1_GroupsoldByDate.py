import pandas as pd

#Soln 1 Without pandas
# def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
#    dict={}  

#    for i in range(len(activities)):
#        sell_date=activities['sell_date'][i]
#        product=activities['product'][i]

#        if sell_date not in dict:
#             dict[sell_date]=set()
#        dict[sell_date].add(product)
        

#    result=[]  

#    for key,value in dict.items():
#         temp=[]
#         for product in value:
#             temp.append(product)
#         temp.sort()
#         s=','.join(temp)
#         result.append([key,len(value),s])

#    df=pd.DataFrame(result,columns=['sell_date','num_sold','products'])
#    return df.sort_values(by='sell_date')

#Soln 2 With pandas
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    groups=activities.groupby('sell_date').agg(
        num_sold=('product','nunique'),
        products=('product',lambda x: ','.join(sorted(set (x))))
    ).reset_index()
    return groups.sort_values(by='sell_date')
