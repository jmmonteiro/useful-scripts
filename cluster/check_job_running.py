# Script that reads the ids from log files in the current folder
# and checks if those jobs are still running on the cluster

import subprocess as sp
import re
import glob

#--- Get list ids from of log files
log_files = glob.glob('*.o*')
pattern = re.compile('o([0-9]+)')
ids_log = []
for f in log_files:
    if pattern.findall(f):
        ids_log.append(pattern.findall(f)[0])


#--- Get ids from qstat
# Save qstat as temporary text file
sp.call('qstat > tmp.txt', shell=True)

tmp_file = open('tmp.txt', 'r')
pattern = re.compile('([0-9])+\w')
ids = []
for l in tmp_file:
    if pattern.findall(l):
        ids.append(pattern.match(l).group())


if any(x in ids for x in ids_log):
    print('There are still jobs running')
else:
    print('None of these jobs is running')

#--- Remove temporary text file
sp.call('rm tmp.txt', shell=True)
