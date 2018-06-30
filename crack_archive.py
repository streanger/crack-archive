#!/usr/bin/python3
import sys
import os
import zipfile
from time import sleep, time
from termcolor import colored

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def read_file(fileName, rmnl=False):
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    path = os.path.join(path, fileName)
    try:
        with open(path, "r") as file:
            if rmnl:
                fileContent = file.read().splitlines()
            else:
                fileContent = file.readlines()
    except:
        print("wrong dict file specified...")
        fileContent = []
    return fileContent

def crack_zip(file, dictFile):
    zip_ = zipfile.ZipFile(file)
    try:
        zip_ = zipfile.ZipFile(file)
    except zipfile.BadZipfile:
        print("wrong zip file specified...")
        sys.exit()
    passwords = read_file(dictFile, rmnl=True)
    if not passwords:
        print("empty passwords dictionary...")
        sys.exit()
    startTime = time()
    #we sure for zip and dictio:
    print("file to crack: {}, dictionary file: {}".format(file, dictFile))
    for key, password in enumerate(passwords):
        password = str.encode(password)
        try:
            zip_.extractall(pwd=password)
            password = colored(password, "cyan")        #comment this for non-color
            print("\npassword found: {}".format(password))
            break
        except:
            elapsed = round(time() - startTime, 4)
            elapsed = colored(elapsed, "cyan")          #comment this for non-color
            key = colored(key, "cyan")                  #comment this for non-color
            print("passwords tried: {}, elapsed time: {}[s]".format(key, elapsed), end='\r', flush=True)

def crack_7z(file, dictFile):
    #to be done
    print(42)

def pseudo_optargs(args):
    #make some useful optargs
    if len(args) > 1:
        file = args[0]
        dictFile = args[1]
    else:
        print("no files specified...")
        sys.exit()
    return file, dictFile

if __name__ == "__main__":
    path = script_path()                                #change dir to script one
    file, dictFile = pseudo_optargs(sys.argv[1:])       #get file and dictFile from user
    crack_zip(file, dictFile)
