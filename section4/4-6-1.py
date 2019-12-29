import pandas as pd
#xlrd openpyxl

#기본 읽기
#sheet_name 안써주면 디폴트로 0번시트
df = pd.read_excel('/Users/dkkim/Documents/section4/excel_s1.xlsx', sheet_name=0)
#print(df)
#head - 상위 5개 tail- 하위 5개
#print(df.head())
#print(df.tail())

#행, 푸터(Footer) 스킵
#skiprows = 행 스킵 skip_footer = 하위 10개 스킵
#df = pd.read_excel('/Users/dkkim/Documents/section4/excel_s1.xlsx', skiprows=[0], skip_footer=10)
#print(df)

#헤더 정의(1)
#df = pd.read_excel('/Users/dkkim/Documents/section4/excel_s1.xlsx',header=0)
#print(df)
#print(list(df))
#print(list(df.columns.values))


#헤더 정의(2)
#df = pd.read_excel('/Users/dkkim/Documents/section4/excel_s1.xlsx',skiprows=[0],header=None,names=['state',2003,3004,3005])
#print(df)

# 특정 값 치환
#60000이상이면 그대로 아니면 none으로 표시
#df = pd.read_excel('/Users/dkkim/Documents/section4/excel_s1.xlsx',header=0, na_values='...',converters={"2003":lambda w:w if w > 60000 else None})
#print(df)
#print(pd.isnull(df))

#실습 정의 및 인덱스 재정의
df = pd.read_excel('/Users/dkkim/Documents/section4/excel_s1.xlsx',header=0)
print(df.rename(index=lambda x:x+1))
print(df.rename(index=lambda x:x+1).index)
