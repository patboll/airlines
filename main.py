import pandas as pd
import matplotlib.pyplot as plot


data = pd.read_csv(r'C:\Users\Patrick\Downloads\JUL22cond.csv')


airlines = []
df_extra = pd.DataFrame(data, columns=['DAY_OF_MONTH', 'OP_UNIQUE_CARRIER', 'DEP_DELAY_NEW'])
airlines = df_extra.OP_UNIQUE_CARRIER.unique()


for i in airlines:
    df = pd.DataFrame(data, columns=['DAY_OF_MONTH', 'OP_UNIQUE_CARRIER', 'DEP_DELAY_NEW'])
    df = df[df["OP_UNIQUE_CARRIER"].str.contains(i) == True]
    df2 = df[df['DEP_DELAY_NEW'] > 0]
    del df2['OP_UNIQUE_CARRIER']
    df3 = df2.groupby(['DAY_OF_MONTH']).count()
    df3.plot.bar()
    plot.title(i)
    plot.show()


