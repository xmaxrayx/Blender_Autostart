#import os
#result = os.system("\"C:/Program Files (x86)/Notepad++/notepad++.exe\"")
#couse crash when notepad wasn't running at first before run the script   


#result = subprocess.run(["C:/Program Files (x86)/Notepad++/notepad++.exe"], capture_output=True)
#print(result.stdout)
#print(result.stderr)




import bpy
import time
import subprocess
subprocess.run(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"], capture_output=False)




subprocess.Popen([r"C:/Program Files (x86)/Notepad++/notepad++.exe"])






#result = subprocess.run(["C:/Program Files (x86)/Notepad++/notepad++.exe"], capture_output=False)



#result = subprocess.run("\"C:/Program Files (x86)/Notepad++/notepad++.exe\"")
#time.sleep(1) #add it to pervent multi-spam running that can lead blender to crash 
#never mind turn out it pervent to use blnder unless you close the other apps
