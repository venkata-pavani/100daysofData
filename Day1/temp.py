# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

print('Absolute path of file:	 ',
	os.path.abspath(__file__))
print('Absolute directoryname: ',
	os.path.dirname(os.path.abspath(__file__)))

# =============================================================================
# * READING FILE NAME AS STRING AND SPLITTING STRINGS*
# import os
# =============================================================================
path = 'I:\100 DAYS OF DATA\LOG.txt'
print("Calling file from custom drive:",os.path.splitext(path))
print("Calling file from custom drive:",os.path.basename(path))
print("Calling file from custom drive:",os.path.basename(path).split('/'))
print("Calling file from custom drive:",os.path.basename(path).split('/')[-1])


# =============================================================================
# USING PATH LIB
# =============================================================================
from pathlib import Path
file_path = 'I:\100 DAYS OF DATA\LOG.txt'
print(Path(file_path))
print("STEM USAGE FROM PATH",Path(file_path).stem)
print("NAME USAGE FROM PATH",Path(file_path).name)


# =============================================================================
# HOW TO OPEN A FILE 
# =============================================================================
file2 = open(r"I:\100 DAYS OF DATA\LOG.txt","r+")
print("after read",file2.read())
print()
file2.seek(0)
# readlines function
print("Output of Readlines function is ") 
print(file2.readlines(9)) 
print()
file2.close()