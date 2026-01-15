#!/bin/env python3

import json,subprocess,string
# cmd = 'pvesh get /cluster/backup --noborder 1 --noheader 1'
# cmd = 'pvesh get /cluster/backup --noborder 1 --noheader 1 --output-format json'
cmd = 'pvesh get /cluster/backup --output-format json'
IDS = subprocess.getoutput(cmd)
backups = json.loads(IDS)


# list of integers!
allvms = []

for backup in backups:
    if "all" in backup:
        # there might be 'excludes'
        node = backup["node"]
        if "exclude" in backup:
            exclude = backup["exclude"]
            # make very sure it's integers
            excludes = list(map(int,exclude.split(',')))
        else:
            excludes = []
        # get vmids on this node
        cmd = 'pvesh get /nodes/'+backup["node"]+'/qemu --output-format json'
        ret = subprocess.getoutput(cmd)
        vms = json.loads(ret)
        for vm in vms:
            vmid = int(vm["vmid"])
            if not vmid in excludes:
            #    print("not in excludes on node "+node+" : "+str(vmid))
                if not vmid in allvms:
                    allvms.append(vmid)
                else:
                    print("ALL ALREADY IN LIST: "+str(vmid)+" from node "+node)
    else:
        vms = backup["vmid"]
        ids = vms.split(',')
        for vmid in ids:
            id = int(vmid)
            if not id in allvms:
                allvms.append(id)
            else:
                print("ALREADY IN LIST: "+str(id))

#allvms.sort()
#print(allvms)
