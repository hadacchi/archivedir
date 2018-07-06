# test.py

test.py is sample to use archivedir.py.

# archivedir/archivedir.py

archive files under the target directory.
this depends on listdir.py

Example
-------

```
>>> from archivedir import archivedir
>>> archivedir(zipfilename, targetdir, mode)
```

Parameters:
-----------

<dl>
<dt>zipfilename : string</dt>
<dd>zip filename where files under the target directory will be stored.</dd>
<dt>targetdir : string</dt>
<dd>files under this directory will be archived.</dd>
<dt>mode : string</dt>
<dd>
only 'keep' or 'remove' will be accepted.<br>
if mode is 'keep', files and directories under the target directory will be kept back.<br>
if mode is 'remove', they will be removed.
</dd>
</dl>

# archivedir/listdir.py

return array of files or directories under the target directory.
``listfiles`` returns files with relative path from current directory or root.
``listdirs`` returns directories with relative path from current directory or root.
both of them don't return the target directory.

Examples
--------

```
>>> from archivedir import listdirs, listfiles
>>> listfiles(dname)
['dname/dir1/file1', 'dname/file2', ... ]
>>> listdirs(dname)
['dname/dir1', 'dname/dir1/dir2', ... ]
```

Parameter
---------

<dl>
<dt>dname : string</dt>
<dd>target directory.</dd>
</dl>
