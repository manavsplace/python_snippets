import matplotlib.pyplot as plt
import pandas as pd

df_plt = train.groupby(by=pd.qcut(train['loc'],10,duplicates='drop')).agg({'defects':['mean','count']}).reset_index()
df_plt.columns = ['loc','mean','count']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

train.groupby(by=pd.qcut(train['loc'],10,duplicates='drop')).agg({'defects':['mean']}).plot(ax=ax1)
