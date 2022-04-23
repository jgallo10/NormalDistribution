#done by Jason and Khizar

import pandas_datareader.data as dat
import datetime

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = dat.DataReader("TSLA", 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
#df = df.drop("Symbol", axis=1)     #this is giving me an error that i couldn't figure out: KeyError: "['Symbol'] not found in axis"

print(df.head())