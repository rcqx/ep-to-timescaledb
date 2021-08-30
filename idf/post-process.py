import pandas as pd

# North
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 5, 6]], axis=1) 
df.insert(1, "zone", "northZone")
df.to_csv('northZone.csv', header=False, index=False)

# South
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 3, 4, 5, 6]], axis=1) 
df.insert(1, "zone", "southZone")
df.to_csv('southZone.csv', header=False, index=False)

# East
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 4, 5, 6]], axis=1) 
df.insert(1, "zone", "eastZone")
df.to_csv('eastZone.csv', header=False, index=False)

# West
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 4, 6]], axis=1) 
df.insert(1, "zone", "westZone")
df.to_csv('westZone.csv', header=False, index=False)

# Core
df = pd.read_csv("eplusout.csv")
df = df.drop(df.columns[[1, 2, 3, 4, 5]], axis=1) 
df.insert(1, "zone", "coreZone")
df.to_csv('coreZone.csv', header=False, index=False)