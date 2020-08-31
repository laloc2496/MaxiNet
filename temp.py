import os,subprocess
from MaxiNet.tools import Tools
d = Tools.get_script_dir()
for f in filter(lambda x: x[-3:]==".sh",os.listdir(d)):
    print (f)
    subprocess.call(["sudo","chmod","a+x",d+f])
