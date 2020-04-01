from statistics import mean
import csv
import numpy as np
import matplotlib.pyplot as plot

filepath = [
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Brazil - 200.17.202.195/p_brazil_to_georgia.txt',
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Poland - 194.29.178.14/p_poland_to_purdue.txt',
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Canada - 142.103.2.2/p_canada_to_citadel.txt',
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Japan1 - 165.242.90.128/p_japan1_to_georgia.txt',
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Minnesota - 146.57.249.98/p_minnesota_to_michigan.txt'
            ]
losses = []
for file in filepath:
    ping = open(file, "r")

    loss = []
    loss_data = []

    for i in ping:
        if 'packet loss' in i:
            s = i.split(',')
            loss.append(float((s[2][:s[2].find('%')]).strip()))
            loss_data.append(i)
    losses.append(loss)
    #print(loss)
A=losses[0]
B=losses[1]
C=losses[2]
D=losses[3]
E=losses[4]

with open('loss_output4.csv','w') as f:
    writer = csv.writer(f)
    for i in E:
        writer.writerow([i])

'''
Y = np.arange(1, len(A)+1) / len(A)
plot.title('Cumulative Distribution Function')
plot.xlabel('latency')
plot.ylabel('cumulative frequency')
plot.plot(A,Y,label='Brazil-Georgia')
plot.plot(B,Y,label='poland-purdue')
plot.plot(C,Y,label='canada-citadel')
plot.plot(D,Y,label='japan-georgia')
plot.plot(E,Y,label='minnesota_to_michigan')
plot.legend()
plot.show()
'''



