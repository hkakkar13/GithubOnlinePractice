import pandas as pd
import numpy as np

user_data = {'MarksA':np.random.randint(50,100,5) ,'MarksB':np.random.randint(50,100,5) ,'MarksC':np.random.randint(50,100,5)}
            
df = pd.DataFrame(user_data,dtype='float32')         
print(df)

df.to_csv('marks.csv')

mydata = pd.read_csv('marks.csv',usecols=[1,2,3])
print(mydata)
print(mydata.describe())

idx=[df.columns.get_loc('MarksB'),df.columns.get_loc('MarksC')]
print(f"\nSlicing Operations:\n{df.iloc[:3,idx]}\n{df.iloc[3:,[0,1]]}")