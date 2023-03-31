bl_info = {
    "name": "Auto start",
    "author": "xMaxrayx",
    "version": (0, 1),
    "blender": (3, 40, 0),
    "location": "addon-section",
    "description": "sssst",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}
import bpy
import time
import subprocess

class AutomationStartBlender(bpy.types.Operator):
    # Give it a bl_idname attribute
    bl_idname = "automation.start_blender"
    bl_label = "Automation Start Blender"
    
    def execute(self, context):
    

    subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
    subprocess.Popen([r"C:/Program Files (x86)/Notepad++/notepad++.exe"])
    subprocess.Popen([r"C:/Windows/System32/calc.exe"])

def register():
    bpy.utils.register_class(automation.start_blender)


def unregister():
    bpy.utils.unregister_class(automation.start_blender)



#import os
#result = os.system("\"C:/Program Files (x86)/Notepad++/notepad++.exe\"")
#couse crash when notepad wasn't running at first before run the script   

#result = subprocess.run(["C:/Program Files (x86)/Notepad++/notepad++.exe"], capture_output=True)
#print(result.stdout)
#print(result.stderr)





#subprocess.run(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"], capture_output=False)







#result = subprocess.run(["C:/Program Files (x86)/Notepad++/notepad++.exe"], capture_output=False)



#result = subprocess.run("\"C:/Program Files (x86)/Notepad++/notepad++.exe\"")


#time.sleep(1) #add it to pervent multi-spam running that can lead blender to crash 
#never mind turn out it pervent to use blnder unless you close the other apps"

'''
will this explain why
the main difference is that subprocess.run() executes a command and waits for it to finish, while with subprocess.
Popen you can continue doing your stuff while ...
'''


'''
The difference between using r"" and “” is that r"" creates a raw string that does not interpret backslashes as escape characters. 
This can be useful when dealing with Windows paths that contain backslashes. However,
you can also use forward slashes in Windows paths, as you did in the second line.
'''



