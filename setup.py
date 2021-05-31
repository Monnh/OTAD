import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "tkinter"]}

base = None

setup(  name = "GUI1",
        version = "0.1",
        description = "GUI1 for T-schakt",
        options = {"build_exe": build_exe_options},
        executables = [Executable("GUI1.py", base=base)])