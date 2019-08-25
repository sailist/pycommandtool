import argparse,sys
from argparse import RawDescriptionHelpFormatter

description = "Copy standard input to each FILE, and also to standard output."
usage = None
epilog = ""

prog = '''MODE determines behavior with write errors on the outputs:
  'warn'         diagnose errors writing to any output
  'warn-nopipe'  diagnose errors writing to any output not a pipe
  'exit'         exit on error writing to any output
  'exit-nopipe'  exit on error writing to any output not a pipe
The default MODE for the -p option is 'warn-nopipe'.
The default operation when --output-error is not specified, is to
exit immediately on error writing to a pipe, and diagnose errors
writing to non pipe outputs.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/tee>
or available locally via: info '(coreutils) tee invocation'
'''

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("-a","--append",
                    dest="append",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="append to the given FILEs, do not overwrite")

parser.add_argument("-i","--ignore-interrupts",
                    dest="ignore_interrupts",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="ignore interrupt signals")

parser.add_argument("-p",
                    dest="diagnose_pipes",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="diagnose errors writing to non pipes")

parser.add_argument("--output-error",
                    dest="output_error",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="set behavior on write error.  See MODE below")

parser.add_argument('OUT',
                    metavar='OUT',
                    type=str,
                    nargs='*',
                    help='FILE, or standard output')

parg = parser.parse_args()

append = parg.append
ignore_interrupts = parg.ignore_interrupts
diagnose_pipes = parg.diagnose_pipes
output_error = parg.output_error

fs = parg.OUT
if len(fs) == 0:
    fs =["-"]

stream = []

for i in range(len(fs)):
    f = fs[i]
    if f == "-":
        stream.append(sys.stdout)
    else:
        if append:
            stream.append(open(f,"wab"))
        else:
            stream.append(open(f, "wb"))

while True:
    try:
        ipt = input("")
        for s in stream:
            s.write(f"{ipt}\n".encode(encoding="utf-8"))
            s.flush()
    except KeyboardInterrupt:
        for s in stream:
            s.close()
        exit(0)

