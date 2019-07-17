''' info:
    The zipfile module from the Python standard library supports only CRC32 encrypted zip files.
    If we want to decompress an AES-128 encrypte file, we need to use 7z tool and call it as subprocess
'''

import sys
import os
import zipfile
from time import sleep, time
import subprocess


def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
    
def simple_read(file):
    '''simple_read data from specified file'''
    with open(file, "r") as f:
        content = f.read().splitlines()
    return content
    
    
if __name__ == "__main__":
    path = script_path()  
    dictFile = "polish_pass.txt"
    passwords = simple_read(dictFile)
    # file = "something.zip"
    file = "Master_Darling.zip"
    sevenz_path = r'D:\Programy\7z\7-Zip\7z.exe'
    
    try:
        zip_ = zipfile.ZipFile(file)
    except zipfile.BadZipfile:
        print("wrong zip file specified...")
        sys.exit()
        
    for key, password in enumerate(passwords):
        # print(password, end=', ')
        # input()
        # if True:
        try:
            out = subprocess.check_output([sevenz_path, "x", "-y", "-so", "-p" + password, file])
            # print("{}".format(key))
            print("\npassword found: {}".format(password))
            break
        except:
        # else:
            pass
            
