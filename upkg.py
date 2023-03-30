#!/usr/bin/env python

#A simple little script to update all of your Python packages, your Arch packages, as well as pip! Written by Kaede <3

import pkg_resources
from subprocess import call

print("This tool will attempt to update the following Python packages, as well as your Arch system:")

tpkgs = [dist.project_name for dist in pkg_resources.working_set]
pkgs = []
for pkg in tpkgs:
    if not pkg.startswith("-"):
        print(pkg)
        if pkg != "pip":
            pkgs.append(pkg)
input("Press Enter to continue...\n")
call("python -m pip install --upgrade pip", shell=True)
call("pip install --upgrade " + ' '.join(pkgs), shell=True)
print("(Hopefully) Successfully updated all Python packages! Moving on to pacman -Syu!")
try:
    isPacman = call(['which', 'pacman'])
    if isPacman == 0:
        call("sudo pacman -Syu", shell=True)
    else:
        print("Could not find pacman... you are likely running this on a non Arch environment, and that's perfectly fine if you're just updating Python packages!")
except:
    print("You are likely not on *NIX... unexpected issues may occur, please refrain from use of this script. (pacman -Syu was NOT ran :)")
