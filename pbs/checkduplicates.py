#!/bin/env python3
# Check PBS for duplicates

import os
import sys


def parsedirs(pool):
    allvms = {}
    for dir in os.listdir(pool):
        vmdir = pool+'/'+dir+'/vm'
        if not os.path.isdir(vmdir):
            continue
        for vmid in os.listdir(vmdir):
            vmbackup = vmdir+"/"+vmid
            if len(os.listdir(vmbackup)) < 2:
                print("Directory "+vmbackup+" seems empty")
                continue
            if vmid in allvms.keys():
                print("Found ID "+vmid+" in "+dir+" but it already exists in "+allvms.get(vmid))
            else:
                allvms[vmid]=dir
#    return allvms

def print_help(name):
    print("Usage: "+name+" <path to storage pool>")

if len(sys.argv) > 1:
    pool = sys.argv[1]
    if os.path.exists(pool):
        if os.path.isdir(pool):
            parsedirs(pool)
        else:
            print(pool+" is not a directory")
            exit(1)
    else:
        print("Pool location "+pool+" does not exist")
        exit(1)
else:
    print_help(sys.argv[0])


