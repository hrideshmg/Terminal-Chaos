import platform
import subprocess
import os

if platform.system() == "Linux":
    p = subprocess.Popen([".linuxDist/dist/Chest/Chest"])
    p.wait()
    try:
        os.rename("DarkBookI.txt", "DarkBookII.txt")
    except:
        print("File not found! Please inform your mentor")
if platform.system() == "Darwin":
    print("Mac OS file not loaded yet")
elif platform.system() == "Windows":
    print("What are yo doing on windows?")
