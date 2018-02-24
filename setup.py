from distutils.core import setup
import py2exe, sys, os
from glob import glob
data_files = [
        ("USER32.dll", glob(r'C:\Windows\system32\USER32.dll')) 
        ,("SHELL32.dll", glob(r'C:\Windows\system32\SHELL32.dll'))                  
        ,("ADVAPI32.dll", glob(r'C:\Windows\system32\ADVAPI32.dll'))
        ,("GDI32.dll", glob(r'C:\Windows\system32\GDI32.dll'))
        ,("WS2_32.dll", glob(r'C:\Windows\system32\WS2_32.dll'))
        ,("CRYPT32.dll", glob(r'C:\Windows\system32\CRYPT32.dll'))
        ,("KERNEL32.dll", glob(r'C:\Windows\system32\KERNEL32.dll'))
        ,("PYTHON27.dll", glob(r'C:\Windows\System32\python27.dll'))
         ]
options = {'py2exe': {'bundle_files': 1, 'compressed': True,}}

#setup(console=['shell.py'],data_files=data_files ,options = options)
setup(console=['shell.py'], options = options, zipfile=None)
