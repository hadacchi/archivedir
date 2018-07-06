from .listdir import listdirs,listfiles
from os import remove, rmdir
from os.path import isdir
from zipfile import ZipFile, ZIP_STORED

def archivedir(zipfilename,targetdir,mode='keep'):
    '''archive dir recursively
    mode is 'keep' or 'remove'
    'keep' means keep archived files.
    'remove' means remove archived files.
    '''
    if not isdir(targetdir):
        raise Exception('No directory')
    flist = listfiles(targetdir)
    with ZipFile(zipfilename,'w',ZIP_STORED) as zfile:
        for f in flist:
            zfile.write(f)
    if mode == 'remove':
        for f in flist:
            remove(f)
        for d in listdirs(targetdir):
            rmdir(d)
