from jugaad_data.nse import stock_df
from datetime import date
from dateutil.relativedelta import relativedelta
import os
import time
import sys
import pandas
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

symbol = sys.argv[1]
x=int(sys.argv[2])

today = date.today()
last = today - relativedelta(years=x) #+ relativedelta(days=1)
t = str(symbol)

df = stock_df(symbol="SBIN", from_date=last,to_date=today, series="EQ")
columns = ['DATE', 'OPEN', 'CLOSE', 'HIGH','LOW', 'LTP', 'VOLUME', 'VALUE', 'NO OF TRADES']
df = df.loc[:,columns]
sizes=[]
times=[]


file=t+".csv"
stime = time.time()
df.to_csv(file, index=False)
etime = time.time() 
sizes.append(os.path.getsize(file))
times.append((etime-stime)*10000)

file=t+".json"
stime = time.time()
df.to_json(file)
etime = time.time() 
sizes.append(os.path.getsize(file))
times.append((etime-stime)*10000)

file=t+".html"
stime = time.time()
df.to_html(file)
etime = time.time() 
sizes.append(os.path.getsize(file))
times.append((etime-stime)*10000)

file=t+".txt"
stime = time.time()
df.to_csv(file, sep='\t', index=False)
etime = time.time() 
sizes.append(os.path.getsize(file))
times.append((etime-stime)*10000)

file=t+".parquet"
stime = time.time()
df.to_parquet(file, compression=None)
etime = time.time() 
sizes.append(os.path.getsize(file))
times.append((etime-stime)*10000)

file=t+".orc"
stime = time.time()
df.to_orc(file)
etime = time.time()
sizes.append(os.path.getsize(file))
times.append((etime-stime)*10000)

file=t+".feather"
stime = time.time()
df.to_feather(file)
etime = time.time() 
sizes.append(os.path.getsize(file))
times.append((etime-stime)*10000)

files = ["csv", "json", "html", "txt", "parquet", "orc", "feather"]
colors = ['red', 'purple', 'brown', 'green', 'black', 'blue', 'orange']

for i in range(len(files)):
    plt.scatter(times[i],sizes[i],c=colors[i], label=files[i])


plt.title('Differrent file types')
plt.xlabel('time to create files(10-4 s)')
plt.ylabel('size of file(bytes)')
plt.legend()
plt.savefig(t+'.png')
