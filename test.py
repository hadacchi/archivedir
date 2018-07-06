from archivedir import archivedir, listdirs, listfiles

import os
import sys

os.mkdir('test')
os.mkdir('test/a')
f = open('test/c','w')
f.close()
f = open('test/a/a1','w')
f.close()
f = open('test/a/a2','w')
f.close()

print("listdirs('test')", listdirs('test'), file=sys.stderr)
print("listfiles('test')", listfiles('test'), file=sys.stderr)
print("archive 'test' into 'test.zip'")
archivedir('test.zip','test')
