# By iFanpS
# Helped by KIPAS
from os import replace
import re

newip = input("Input Your GTPS IP: ")
task1 = open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r').read();
ip = re.findall("(.*?) growtopia1.com",str(task1))[0]

cngip = task1.replace(ip, newip);

task2 = open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'w')
task2.write(cngip)
task2.close()