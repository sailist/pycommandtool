import argparse
from argparse import RawDescriptionHelpFormatter

description = '''Output pieces of FILE to PREFIXaa, PREFIXab, ...;
default size is 1000 lines, and default PREFIX is 'x'.

With no FILE, or when FILE is -, read standard input.'''
usage = "Usage: split [OPTION]... [FILE [PREFIX]]"
epilog = '''The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

CHUNKS may be:
  N       split into N files based on size of input
  K/N     output Kth of N to stdout
  l/N     split into N files without splitting lines/records
  l/K/N   output Kth of N to stdout without splitting lines/records
  r/N     like 'l' but use round robin distribution
  r/K/N   likewise but only output Kth of N to stdout

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/split>
or available locally via: info '(coreutils) split invocation'
'''

prog = "split"

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("-l","--lines",
                    dest="lines",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type = int,
                    default=None,
                    help="put NUMBER lines/records per output file")

parser.add_argument("-b","--bytes",
                    dest="bytes",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type = int,
                    default=None,
                    help="put SIZE bytes per output file")

parser.add_argument("-n","--number",
                    dest="number",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type = int,
                    default=None,
                    help="generate CHUNKS output files; see explanation below")

parser.add_argument("-a","--suffix-length",
                    dest="suffix_length",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type = int,
                    default=2,
                    help="generate suffixes of length N (default 2)")


parser.add_argument("-s","--additional-suffix",
                    dest="additional_suffix",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type=str,
                    default="",
                    help="append an additional SUFFIX to file names")

parser.add_argument("-f","--format-string",
                    dest="format_fname",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type=str,
                    default="{prefix}{suffix}",
                    help="Format")

parser.add_argument("--fix-length",
                    dest="fix_suffix_length",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="when suffixes exhausted, continuously increase the suffix. default False.")

parser.add_argument("-d",
                    dest="numeric_suffix",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="put SIZE bytes per output file")

parser.add_argument("--numeric-suffixes",
                    dest="numeric_suffixes",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type = int,
                    default=None,
                    help="same as -d, but allow setting the start value")

parser.add_argument("-e","--elide-empty-files",
                    dest="elide_empty_files",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="do not generate empty output files with '-n'")

parser.add_argument("--verbose",
                    dest="verbose",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="print a diagnostic just before each")



parser.add_argument('FILE',
                    metavar='FILE',
                    type=str,
                    nargs="?",
                    default="-",
                    help="Output pieces of FILE to PREFIXaa, PREFIXab, ...;default size is 1000 lines. With no FILE, or when FILE is -, read standard input.")

parser.add_argument('PREFIX',
                    metavar='PREFIX',
                    type=str,
                    nargs="?",
                    default="x",
                    help="default PREFIX is 'x'")

parg = parser.parse_args()

lines = parg.lines
bytes = parg.bytes
number = parg.number
numeric_suffix = parg.numeric_suffix
suffix_length = parg.suffix_length
additional_suffix = parg.additional_suffix
numeric_suffixes = parg.numeric_suffixes
elide_empty_files = parg.elide_empty_files
verbose = parg.verbose
file= parg.FILE
PREFIX= parg.PREFIX
additional_prefix = ""
fix_suffix_length = parg.fix_suffix_length


def check_state(lines,bytes,number):
    num = 0
    if lines:
        num+=1
    if bytes:
        num+=1
    if number:
        num+=1
    return num<=1

if not check_state(lines,bytes,number):
    print("split: cannot split in more than one way")
    print("Try 'split --help' for more information.")
    exit(0)

if lines is None and bytes is None and number is None:
    lines = 1000

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbet = "0123456789"


with open(file,"rb") as f:
    content = f.readlines()
    if lines:
        for i,line in enumerate(content):
            f = None
            if (i+1)%lines == 0:
                # f = open(f"{additional_prefix}{}")
                pass

### TODO