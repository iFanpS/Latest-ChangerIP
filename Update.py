# By iFanpS
# Helped by KIPAS
from os import replace
import re, time

print("="*20)
print("ChangerIP by iFanpS")
print("="*20)

def gantiIP():
    newIP = input("Put ur GTPS IP: ")
    task1 = open("Path to your ETC/Hosts file","r")
    ip = re.findall("(.*?)growtopia1.com",str(task1))[0]
    
    gantiIPS = replace(ip, newIP)
    
    task2 = open("Path to your ETC/Hosts file", "w")
    task2.write(gantiIPS)
    task2.close()

if __name__ == "__main__":
    gantiIP()
    time.sleep(2)
    input("Type anykey to close...")