import os
import copy
import zlib
from tkinter import filedialog

print("\033c\033[47;30m\ngive me the .txt pack file ? \n")
a=filedialog.askopenfile(title="give me the .txt pack file  ? ",defaultextension="*.txt")
a=a.name
f1=open(a,"r")
f=f1.read()
f1.close()
ff=f.split("\n")
names=ff[0]
files=ff[1]
counter=0
f1=open(names+".pack1","wb")
f1.close()

for d in ff:
    if counter!=0 and d.strip()!="":
        f1=open(d,"rb")
        fff=f1.read()
        f1.close()
        f1=open(names+".pack1","ba")
        f1.write(zlib.compress(fff,level=9))
        f1.write(b"\x01\x00\x05\x04\x03\x02")
        f1.close()
    counter=counter+1
