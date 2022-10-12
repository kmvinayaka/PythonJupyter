import os
import shutil 

files = (file for file in os.listdir(".") if os.path.isfile(os.path.join(".", file)))
for file in files:
    
    if os.path.exists(file.split('.')[-1]):

        shutil.copy(file,os.path.join(file.split('.')[-1],file))
    else:

        os.mkdir(file.split('.')[-1])
        shutil.copy(file,os.path.join(file.split('.')[-1],file))
        
        
    print(file)
