# I have too many figures and versions on my .tex files to keep track
# This script reads a .tex file and copies the figures that are displayed to a separate folder <texFilemane>_figs/
# Useful when journals ask for the figures in separate
# Written by: Joao M. Monteiro
import re
import os, shutil

texFilemane = 'monteiro2015.tex'


# Open file
f = open(texFilemane , 'r')
fig_pattern1 = re.compile('^[^%]\s*\\includegraphics.*') # figure line is idented "\s*" matches empty space
fig_pattern2 = re.compile('^[^%]*\\includegraphics.*') # figure line is not idented
path_pattern = re.compile('\{.*\}') # get path

# Make output directory
out_dir = texFilemane[0:-4] + '_figs/'
if os.path.isdir(out_dir) == False:
    os.makedirs(out_dir)

for line in f:
    if fig_pattern1.match(line) != None or fig_pattern2.match(line) != None:
        path = path_pattern.search(line) # search for the path string
        path = path.group() # convert to string
        path = path[1:-1] # remove { }
        print(path)
        shutil.copy2(path, out_dir)



# Close file
f.close()
