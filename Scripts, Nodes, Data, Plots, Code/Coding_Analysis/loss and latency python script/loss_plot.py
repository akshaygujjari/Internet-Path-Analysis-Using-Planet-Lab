import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plot
from pylab import *

df = pd.read_csv('loss_output.csv')
A = list(df['A'])
B = list(df['B'])
C = list(df['C'])
D = list(df['D'])
E = list(df['E'])

y = np.arange(1, len(A)+1) / len(A)
Y = np.flip(y)
plot.title('Cumulative Distribution Function')
plot.xlabel('loss percentage')
plot.ylabel('cumulative frequency')
plot.plot(A,Y,label='Brazil-Georgia', marker = '<')
plot.plot(B,Y,label='poland-purdue',marker='v')
plot.plot(C,Y,label='canada-citadel',marker='>')
plot.plot(D,Y,label='japan-georgia',marker='8')
plot.plot(E,Y,label='minnesota_to_michigan',marker='^')
plot.legend()
plot.show()

