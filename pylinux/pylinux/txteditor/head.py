import argparse
from argparse import RawDescriptionHelpFormatter

description = '''Print the first 10 lines of each FILE to standard output.
With more than one FILE, precede each with a header giving the file name.'''

epilog = '''NUM may have a multiplier suffix:
b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/head>
or available locally via: info '(coreutils) head invocation\''''


prog = "head"
parser = argparse.ArgumentParser(prog=prog,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)
parser.add_argument("-n",dest="n",type = int,default=5)
parser.add_argument("fn")
parg = parser.parse_args()
n = parg.n
fn = parg.fn

with open(fn,"rb") as f:
    i = 0
    for i,line in enumerate(f):
        if i < n:
            print(line.strip().decode())