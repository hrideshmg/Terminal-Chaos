import platform
import subprocess

if platform.system() == "Linux":
    p = subprocess.Popen([".linuxDist/dist/Chest1/Chest"])
    p.wait()
if platform.system() == "Darwin":
    print("Mac OS file not loaded yet")
elif platform.system() == "Windows":
    print("What are yo doing on windows?")
