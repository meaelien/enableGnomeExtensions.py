#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from os import listdir
from os import popen
from os.path import isdir, join, expanduser
import time

pre_installed_ext_folder = "/usr/share/gnome-shell/extensions"
my_ext_folder = "{}/.local/share/gnome-shell/extensions".format(expanduser("~"))

black_list = ["window-list@gnome-shell-extensions.gcampax.github.com"]
white_list = []

######## GET EXTENSIONS ###########

def getAllExtensions(): 
	extensions = [d for d in listdir(pre_installed_ext_folder) if isdir(join(pre_installed_ext_folder,d))] # Get pre installed extensions
	extensions = extensions + [d for d in listdir(my_ext_folder) if isdir(join(my_ext_folder,d))] # Add my extensions
	return extensions

def getEnabledExtensions():
	extensions_string = popen("gsettings get org.gnome.shell enabled-extensions").read()
	extensions = [extension.strip("'") for extension in extensions_string.strip().strip('[').strip(']').split(',')]
	return extensions

def getDisabledExtensions():
	extensions = [extension for extension in getAllExtensions() if extension not in getEnabledExtensions()]
	return extensions

####### ENABLE/DISABLE EXTENSIONS ##########

def enableAllExtensions():
	popen("gsettings set org.gnome.shell enabled-extensions \"{}\"".format(getAllExtensions()))

def enableOneExtension(extension):
	popen("gnome-shell-extension-tool -e {}".format(extension))

def disableAllExtensions():
	popen("gsettings set org.gnome.shell enabled-extensions \"[]\"")

def disableOneExtension(extension):
	popen("gnome-shell-extension-tool -d {}".format(extension))

####### OTHERS #########

# Sometimes, it's necessary to restart gnome shell if not startup
def restartGnomeShell():
	popen("nohup gnome-shell --replace &")

def disableBlackListExtensions():
	for extension in black_list:
		disableOneExtension(extension)

def enableWhiteListExtensions():
	for extension in white_list:
		enableOneExtension(extension)

####### MAIN ##########

if __name__ == '__main__':
	time.sleep(2) # Just in case
	enableAllExtensions()
	disableBlackListExtensions()