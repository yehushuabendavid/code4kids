import os
import sys
import time
import os.path
from subprocess import Popen
open("c4k","w")
time.sleep(1)
if os.path.exists("c4k"):
    Popen([sys.executable,"c4k.py"])

def txt(s):
    open("cmd_c4k","w").write("print:"+str(s));
    time.sleep(0.5)
def lire(s):
    if os.path.exists("rsp_c4k"):os.unlink("rsp_c4k")
    open("cmd_c4k", "w").write("input:" + str(s));
    time.sleep(1)
    while not os.path.exists("rsp_c4k"):
        time.sleep(0.5)
    return open("rsp_c4k","r").read()

def cls():
    open("cmd_c4k", "w").write("clear:");
    time.sleep(0.5)
def anime(s):
    open("cmd_c4k", "w").write("anime:"+str(s));
    time.sleep(0.5)
