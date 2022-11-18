import os
import inspect

Import("env")

env.Execute("$PYTHONEXE -m pip install heatshrink2 hiyapyco")
mkespfsbat = '@{0} -B "{1}\\mkespfsimage.py" %*'.format(env.get("PYTHONEXE"), os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))))
mkespfsbatpath = "{}\\mkespfs.bat".format(env.get("PROJECT_DIR"))

try:
    with open(mkespfsbatpath, 'r') as f:
        if f.read() != mkespfsbat:
            raise Exception("rewrite")
except Exception as e:
    with open(mkespfsbatpath, 'w') as f:
        f.write(mkespfsbat)

env.Replace(MKFSTOOL='{}\\mkespfs.bat'.format(env.get("PROJECT_DIR")) )  # PlatformIO now believes it has actually created a SPIFFS
