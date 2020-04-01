from statistics import mean
import csv
'''
'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Brazil - 200.17.202.195/tc_brazil_to_georgia.txt',
'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Brazil - 200.17.202.195/tc_brazil_to_japan2.txt'
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Citadel - 155.225.2.72/tc_citadel_to_canada.txt',
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Poland - 194.29.178.14/tc_poland_to_purdue.txt',
            'D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Japan1 - 165.242.90.128/tc_japan1_to_georgia.txt',
'''

filepath = ['D:/Academics/semester 3/CCN/1_Latest_Logs - 12-7-19/Japan2 - 133.9.81.166/tc_japan2_to_brazil.txt',
            
            ]
for file in filepath:
    trace = open(file,"r")

    #key = ['planetlab6.goto.info.waseda.ac.jp (133.9.81.166)','node1.planetlab.mathcs.emory.edu (170.140.119.69)','planetlab2.cs.ubc.ca (142.103.2.2)','planetlab2.cs.purdue.edu (128.10.18.53)','']
    latency = []


    for i in trace:
        if 'planetlab2.c3sl.ufpr.br (200.17.202.195)' in i:
            latency.append(float(i[i.find(')')+1:i.find('ms')-1]))
    #print(latency)


with open('returns1.csv', 'w') as f:
    writer = csv.writer(f)
    for val in latency:
        writer.writerow([val])
