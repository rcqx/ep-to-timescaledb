import pandas as pd

# North
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 5, 6]], axis=1) 
df.insert(1, "northZone", "northZone")
df.to_csv('northZone.csv', header=False, index=False)

# South
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 3, 4, 5, 6]], axis=1) 
df.insert(1, "southZone", "southZone")
df.to_csv('southZone.csv', header=False, index=False)

# East
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 4, 5, 6]], axis=1) 
df.insert(1, "eastZone", "eastZone")
df.to_csv('eastZone.csv', header=False, index=False)

# West
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 4, 6]], axis=1) 
df.insert(1, "westZone", "westZone")
df.to_csv('westZone.csv', header=False, index=False)

# Core
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 4, 5]], axis=1) 
df.insert(1, "coreZone", "coreZone")
df.to_csv('coreZone.csv', header=False, index=False)