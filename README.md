# archivedir.py

archive files under the target directory.
this depends on listdir.py

Example
-------

```
>>> archivedir(zipfilename, targetdir, mode)
```

Parameters:
-----------

zipfilename : string
    zip filename where files under the target directory will be stored.
targetdir : string
    files under this directory will be archived.
mode : string
    only 'keep' or 'remove' will be accepted.
    if mode is 'keep', files and directories under the target directory will be kept back.
    if mode is 'remove', they will be removed.

# listdir.py

return array of files or directories under the target directory.
``listfiles`` returns files with relative path from current directory or root.
``listdirs`` returns directories with relative path from current directory or root.
both of them don't return the target directory.

Examples
--------

```
>>> listfiles(dname)
['dname/dir1/file1', 'dname/file2', ... ]
>>> listdirs(dname)
['dname/dir1', 'dname/dir1/dir2', ... ]
```

Parameter
---------

dname : string
    target directory.
