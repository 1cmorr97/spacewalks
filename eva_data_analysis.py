import json
import csv
import datetime as dt
import matplotlib.pyplot as plt

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', "r")
output_file = open(
    './eva-data.csv',
    "w",
)
graph_file = 'myplot.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data = []

for i in range(375):
    line = input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
# data.pop(0)
## Comment out this bit if you don't want the spreadsheet

writer = csv.writer(output_file)

time = []
date = []

j = 0
for i in data:
    print(data[j])
    # and this bit
    writer.writerow(data[j].values())
    if 'duration' in data[j].keys():
        duration = data[j]['duration']
        if duration == '':
            pass
        else:
            eva_t = dt.datetime.strptime(duration, '%H:%M')
            deltaT = dt.timedelta(
                hours=eva_t.hour,
                minutes=eva_t.minute,
                seconds=eva_t.second).total_seconds() / (60 * 60)
            print(eva_t, deltaT)
            time.append(deltaT)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                # date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j += 1

eva_t = [0]
for i in time:
    eva_t.append(eva_t[-1] + i)

date, time = zip(*sorted(zip(date, time)))


plt.plot(date, eva_t[1:], "ko-")
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
