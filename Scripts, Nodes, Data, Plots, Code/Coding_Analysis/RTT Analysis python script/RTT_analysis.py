from statistics import mean

#Change the paths before executing
filepath = ['C:/Users/pranith/PycharmProjects/CCN/logs/Brazil - 200.17.202.195/p_brazil_to_georgia.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Brazil - 200.17.202.195/p_brazil_to_japan2.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Canada - 142.103.2.2/p_canada_to_citadel.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Citadel - 155.225.2.72/p_citadel_to_canada.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Georgia - 170.140.119.69/p_georgia_to_brazil.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Georgia - 170.140.119.69/p_georgia_to_japan1.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Japan1 - 165.242.90.128/p_japan1_to_georgia.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Japan2 - 133.9.81.166/p_japan2_to_brazil.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Michigan - 198.108.101.61/p_michigan_to_minnesota.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Minnesota - 146.57.249.98/p_minnesota_to_michigan.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Poland - 194.29.178.14/p_poland_to_purdue.txt',
            'C:/Users/pranith/PycharmProjects/CCN/logs/Purdue - 128.10.18.53/p_purdue_to_poland.txt'
            ]
for file in filepath:
    ping = open(file,"r")

    rtt = ''
    min= []
    max= []
    avg = []
    mdev = []


    for i in ping:
        if 'rtt min/avg/max/mdev' in i:
            rtt = rtt + i + '\n'
            # print(i)
            s = rtt.split('/')
            min.append(float(s[3][s[3].find('=') + 2:]))
            avg.append(float(s[4]))
            max.append(float(s[5]))
            mdev.append(float(s[6][:s[6].find('ms')-1]))

# rtt min / avg / max / mdev = 285.093 / 285.212 / 285.339 / 0.204 ms
    output = open('rtt_brazil_to_georgia.txt','w')
    output.write(rtt)
    output.close()

    print(file[file.find('p_')+2:file.find('.txt')])
    print('min: ' + str(round(mean(min), 2)))
    print('max: ' + str(round(mean(max), 2)))
    print('avg: ' + str(round(mean(avg), 2)))
    print('mdev: ' + str(round(mean(mdev), 2)))
    print('-----------------------------------')