# -*- coding: utf-8 -*-
import os, string, sys, re

filePath = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
os.chdir(filePath)


def fileit( path ):
    a = []
    for root, dirs, files in os.walk( path ):
        for fn in files:
            if fn[-3:] == 'txt':
                p = root+'/'+fn
                a.append(p)
                
    return a
            

files = fileit('.')
newf = []
for each in files:
    newf.append(each[2:])
    
files = newf
print files

for each in files:
    out = each
    lines = open(each).readlines()
    fp = open(each,'w')  #打开你要写得文件pp2.txt
    pt = re.compile(r'(<.+?>)|(^[AB]: )')
    for s in lines:
       fp.write(re.sub(pt, '', s))
    fp.close()  # 关闭文件

    
