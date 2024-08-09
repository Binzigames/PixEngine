from cx_Freeze import setup, Executable

setup(
    name="PixLauncher",
    version="0.1",
    description="Launcher to use PixGameEngine made by porko",
author="porko ",
    executables=[Executable("main.py")],

)