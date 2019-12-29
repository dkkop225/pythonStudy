import pandas as pd

#읽기
df2 = pd.read_csv('/Users/dkkim/Documents/section4/csv_s2.csv',sep=';',skiprows=[0], header=None , names=['Test1','Test2','Test3','Final','Grade'])
#print(df)

#컬럼 내용 변경
#print(df2['Grade'])
#df2['Grade'] = df2['Grade'].str.replace('C','A++')
#print(df2)

#평균 컬럼추가
#df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1)
#print(df2)


#합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)

df2.to_csv('/Users/dkkim/Documents/section4/result_cs1.csv',index=False)
