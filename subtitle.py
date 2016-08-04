import string
import re
from math import floor

import sys

assTime = re.compile('^\d+:\d+:\d+\,\d+')

def assStringToTime(strr):
    (strr0, f0) = strr.split(',')
    t = strr0.split(':')
    time = 0
    time += int(t[0]) * 3600
    time += int(t[1]) * 60
    time += float(t[2])
    time += float('0.' + f0)
    return time

def assTimeToString(time):
    sec = floor(time)
    part = str(int((time - sec) * 100))
    if len(part) < 2:
        part = '0' + part
    h = str(int(sec // 3600))
    sec %= 3600
    m = str(int(sec // 60))
    if len(m) < 2:
        m = '0' + m
    sec = str(int(sec%60))
    if len(sec) < 2:
        sec = '0' + sec
    strr = h +':'+ m +':'+ sec + ',' + part
    return strr

def processAssLine(line,offset):
    if line.find('-->') > 0:
        line = line.strip()
        li = line.split(' --> ')
        if len(li) == 2:
            if assTime.match(li[0]):
                tt1 = assStringToTime(li[0]) + offset
                li[0] = assTimeToString(tt1)
            if assTime.match(li[1]):
                tt2 = assStringToTime(li[1]) + offset
                li[1] = assTimeToString(tt2)
        return ' --> '.join(li) + '\n'
    else:
        return line



assert len(sys.argv) >= 3, "Lack of Arguments"

inputfile = sys.argv[1]
filenames = inputfile.split("/")
filename = filenames[len(filenames) - 1]
offset = int(sys.argv[2])

print(inputfile)
print("./new." + filename)
print(offset)

f = open(inputfile, 'r')
t = open("./new." + filename ,'w')
for line in f.readlines():
    ans = processAssLine(line,offset)
    t.write(ans)

f.close()
t.close()
