#!/usr/bin/env python3

def distribution():
    with open('/etc/os-release') as file1:
        for lines in file1:
            words = lines.split("=")
            if words[0] == 'NAME':
                name = words[1].strip('"\n')
            if words[0] == 'VERSION_ID':
                versionid = words[1].strip('"\n')
                break
    return(name,versionid)
if __name__ == '__main__':
    print(distribution()) 
