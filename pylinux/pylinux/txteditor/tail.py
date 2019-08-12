import argparse
from argparse import RawDescriptionHelpFormatter

description = '''Print the last 10 lines of each FILE to standard output.
With more than one FILE, precede each with a header giving the file name.
With no FILE, or when FILE is -, read standard input.'''

epilog = '''NUM may have a multiplier suffix:
b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.

With --follow (-f), tail defaults to following the file descriptor, which
means that even if a tail'ed file is renamed, tail will continue to track
its end.  This default behavior is not desirable when you really want to
track the actual name of the file, not the file descriptor (e.g., log
rotation).  Use --follow=name in that case.  That causes tail to track the
named file in a way that accommodates renaming, removal and creation.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/tail>
or available locally via: info '(coreutils) tail invocation'''

prog = "tail"

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
    size = 0
    for size,line in enumerate(f):
        pass
with open(fn,"rb") as f:
    i = 0
    for i,line in enumerate(f):
        if size-i<n:
            print(line.strip().decode())