import tkinter as tk
import subprocess
import os

def build_game():
    subprocess.Popen(["python", "setup.py", "build"], shell=True)

def open_script():
    subprocess.Popen(["notepad.exe", "data.py"])
def open_script_main():
    subprocess.Popen(["notepad.exe", "main.py"])

def open_explorer():
    os.startfile(os.getcwd())



PixLauncher = tk.Tk()
PixLauncher.geometry("300x300")
PixLauncher.title("PixLauncher 0.1")
PixLauncher.configure(bg="Black")

ledel = tk.Label(PixLauncher, text="PixEngineControl", font=("prstart.ttf", 20) , bg="Black" , fg="White")
ledel.pack()

author = tk.Label(PixLauncher, text="porko coder designer", font=("prstart.ttf", 10) , bg="Black", fg="White")
author.pack(pady=10)

open_config = tk.Button(PixLauncher, text="open config", command=open_script , )
open_config.pack(pady=10)

open_main = tk.Button(PixLauncher, text="open main", command=open_script_main)
open_main.pack(pady=10)

open_folder = tk.Button(PixLauncher, text="open folder", command=open_explorer)
open_folder.pack(pady=10)


build_button = tk.Button(PixLauncher, text="BiuldGame", command=build_game)
build_button.pack(pady=10)


PixLauncher.mainloop()
