import os
files = ['main','connect']
for i in files:
    file = i + '.ui'
    tgt = i + '.py'
    os.system('pyuic5 {} -o {}'.format(file,tgt))