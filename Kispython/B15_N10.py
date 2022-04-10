import math
import datetime as DT
table = [[' ','0.127','+7 937 472-0944','17.06.1999'],
             [' ','0.057','+7 664 415-6864','20.06.2003'],
             [' ','0.057','+7 664 415-6864','20.06.2003'],
             [' ','0.037','+7 601 508-5538','07.05.2002'],
             [' ','0.008','+7 751 505-9653','25.09.2004'],
             [' ','0.057','+7 664 415-6864','20.06.2003']]

def main(table):
    for i in range(0, len(table)):
        table[i].pop(0)
    table1 = []
    for i in table:
        if i not in table1:
            table1.append(i)
    for i in range(len(table1)):
        table1[i][0] = str(round(float(table1[i][0])*100))+'%'
        table1[i][1] = table1[i][1].replace(' ', '(', 1)
        table1[i][1] = table1[i][1].replace(' ', ') ')
        table1[i][1] = table1[i][1].replace('+7', '')
        table1[i][1] = ('{}-{}'.format(table1[i][1][:12], table1[i][1][12:]))
        date = DT.datetime.strptime(table1[i][2], '%d.%m.%Y').date()
        table1[i][2] = date.strftime('%d-%m-%y')
    table = [list(x) for x in zip(*table1)]
    return table


print(main(table))
