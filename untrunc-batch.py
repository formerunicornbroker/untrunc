import subprocess
from os import listdir
import os.path

print("#################################\nu n t r u n c  b a t c h  t o o l\n#################################")


corruptDir = input("Where is the corrupt directory path? (full path- no subdirectories): ")
referenceFile = input("Where is the reference (known good) file? (full path): ")
untruncPath = input("Where is untrunc.exe? (full path): ")
fileType = input("What type of video files? (e.g. .mp4): ")


fileList = [os.path.join(corruptDir.strip('"'), f) for f in os.listdir(corruptDir.strip('"')) if f.endswith(fileType.strip('"'))]
print(os.listdir(corruptDir.strip('"')))  


for f in fileList:
    subprocess.run([untruncPath.strip('"'), "-s", referenceFile.strip('"'), f], check=True)


print('DONE!')
input("Press Enter to exit...")