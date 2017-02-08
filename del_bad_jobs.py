#!/bin/python3
# Script that checks for cluster jobs that have an error and deletes them
import subprocess as sp
import re

#--- Save qstat as temporary text file
sp.call('qstat > tmp.txt', shell=True)

#--- Get ids
file = open('tmp.txt', 'r')
pattern = re.compile('([0-9])+\w')
status = re.compile('(Eqw)')
ids = []
for l in file:
    if pattern.findall(l):
        if status.findall(l):
            ids.append(pattern.match(l).group())

#--- Stop jobs
for i in ids:
    sp.call('qdel ' +  i, shell=True)


#--- Remove temporary text file
sp.call('rm tmp.txt', shell=True)
