import os

def listfiles(dname):
    '''list files recursively
    '''

    result = []
    for f in os.listdir(dname):
        obj = dname + '/' + f
        if os.path.isfile(obj):
            result.append(obj)
        elif os.path.isdir(obj):
            result += listfiles(obj)
    return result

def listdirs(dname):
    '''list dirs recursively
    '''

    result = []
    for f in os.listdir(dname):
        obj = dname + '/' + f
        if os.path.isfile(obj):
            continue
        elif os.path.isdir(obj):
            result.append(obj)
            result += listdirs(obj)
    return result
