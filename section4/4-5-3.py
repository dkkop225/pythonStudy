import pandas as pd
import numpy as np

#랜덤으로 DataFrame 생성
#df = pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=list('ABCD'))
df = pd.DataFrame(np.random.randn(100,4),columns=list('ABCD'))
print(df)


df.to_csv('/Users/dkkim/Documents/section4/result_cs2.csv',index=False,header=False)
