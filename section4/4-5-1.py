import pandas as pd
#기본 읽기
#df = pd.read_csv('/Users/dkkim/Documents/section4/csv_s1.csv')
#print(df)

#df = pd.read_csv('/Users/dkkim/Documents/section4/csv_s1.csv', skiprows=[0,1])  # 0행과 1행 스킵해라
#print(df)



#df = pd.read_csv('/Users/dkkim/Documents/section4/csv_s1.csv', skiprows=[0], header=None)  # 0행 스킵하고 헤더없이 출력해라
#print(df)

#df = pd.read_csv('/Users/dkkim/Documents/section4/csv_s1.csv', skiprows=[0], header=None , names=['Month',2013,2014,2015])  # 헤더를 임의로 설정해줌
#print(df)

#인덱스 컬럼 정의
#df = pd.read_csv('/Users/dkkim/Documents/section4/csv_s1.csv', skiprows=[0], header=None , names=['Month',2013,2014,2015],index_col=[0])  # 인덱스 지정
#print(df)

#특정 값 치환
#df = pd.read_csv('/Users/dkkim/Documents/section4/csv_s1.csv', skiprows=[0], header=None , names=['Month',2013,2014,2015],index_col=[0],na_values=["JAN"])
#print(pd.isnull(df))
#print(df)

#실습 정리및 인덱스 재정의
df = pd.read_csv('/Users/dkkim/Documents/section4/csv_s1.csv', skiprows=[0], header=None , names=['Month',2013,2014,2015])
#print(df.index)
#print(list(df.index))
#print(df.index.values.tolist())
#print(df.rename(index=lambda x:x*10))


df2 = pd.read_csv('/Users/dkkim/Documents/section4/csv_s2.csv',sep=';',skiprows=[0], header=None , names=['Test1','Test2','Test3','Final','Grade'])
#print(df)

#컬럼 내용 변경
#print(df2['Grade'])
#df2['Grade'] = df2['Grade'].str.replace('C','A++')
#print(df2)

#평균 컬럼추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1)
#print(df2)


#합계 컬럼 추가
df2['Sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)
