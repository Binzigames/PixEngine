from cx_Freeze import setup, Executable
import data

setup(
    name=data.GameName,
    version=data.GameVersion,
    description=data.GameDescripition,
    executables=[Executable("main.py")],
)
