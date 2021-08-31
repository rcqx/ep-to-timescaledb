import pandas as pd

# North
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 5, 6]], axis=1) 
df.insert(1, "zoneid", "NorthZone")
df.to_csv('NorthZone-id.csv', header=False, index=False)

# South
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 3, 4, 5, 6]], axis=1) 
df.insert(1, "zoneid", "SouthZone")
df.to_csv('SouthZone-id.csv', header=False, index=False)

# East
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 4, 5, 6]], axis=1) 
df.insert(1, "zoneid", "EastZone")
df.to_csv('EastZone-id.csv', header=False, index=False)

# West
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 4, 6]], axis=1) 
df.insert(1, "zoneid", "WestZone")
df.to_csv('WestZone-id.csv', header=False, index=False)

# Core
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 4, 5]], axis=1) 
df.insert(1, "zoneid", "CoreZone")
df.to_csv('CoreZone-id.csv', header=False, index=False)

