import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from pylab import *

df = pd.read_csv('returns.csv')
A = list(df['col1'])
B = list(df['col2'])
C = list(df['col3'])
D = list(df['col4'])
E = list(df['col5'])

Y = np.arange(1, len(A)+1) / len(A)
plot.title('Cumulative Distribution Function')
plot.xlabel('latency')
plot.ylabel('cumulative frequency')
plot.plot(A,Y,label='Brazil-Georgia')
plot.plot(B,Y,label='Brazil-japan')
plot.plot(C,Y,label='citadel-canada')
plot.plot(D,Y,label='poland-purdue')
plot.plot(E,Y,label='japan-georgia')
plot.legend()
plot.show()



