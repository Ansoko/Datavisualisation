import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/annes/anaconda3/tcl/tk8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/annes/anaconda3/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['C:/Users/annes/anaconda3/DLLs/tcl86t.dll', 'C:/Users/annes/anaconda3/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('Graph_Dataviz.py', base=base)
]

setup(name = "Interface Datavisualisation 2",
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)

