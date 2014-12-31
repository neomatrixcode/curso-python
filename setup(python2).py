import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : 'clase2.py',
            'description'    : 'Pbtitulos.',
            #'icon_resources' : [(0, 'icon.ico')]
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='t',
    author='josue acevedo maldonado (Neomatrix)',
    author_email='josuecevedo@gmail.com',
    **kwargs)
