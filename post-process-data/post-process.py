import pandas as pd

# North
df = pd.read_csv("eplusout.csv")

df = df.drop(df.columns[[1, 2, 3, 5, 6]], axis=1) 

df.insert(1, "northZone", "northZone")

# df.columns = [''] * len(df.columns)

df.to_csv('northZone.csv', header=False, index=False)

# South
df = pd.read_csv("eplusout.csv")

df = df.drop(df.columns[[1, 2, 3, 5, 6]], axis=1) 

df.insert(1, "northZone", "northZone")

# df.columns = [''] * len(df.columns)

df.to_csv('northZone.csv', header=False, index=False)