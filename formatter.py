import fileinput
import sys

for line in fileinput.input(['./swears.yml'], inplace=True):
    sys.stdout.write('- {l}'.format(l=line))
