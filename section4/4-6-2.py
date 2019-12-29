import pandas as pd

df = pd.read_excel('/Users/dkkim/Documents/section4/excel_s1.xlsx',header=0)

#print(df)

#컬럼값 수정
#print(df['state'])
#df['State'] = df['State'].str.replace(' ','|')
#print(df)


#평균컬럼추가
df['Avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)
print(df)

#평균컬럼추가
df['Sum'] = df[['2003','2004','2005']].mean(axis=1).round(2)
print(df)

#최대값 출력
print(df[['2003','2004','2005']].max(axis=0))

#최소값 출력
print(df[['2003','2004','2005']].min(axis=0))

#상세 정보 출력  판다스 내장 속성
print(df.describe())

df.to_excel('/Users/dkkim/Documents/section4/result_s1.xlsx' ,index=None)
