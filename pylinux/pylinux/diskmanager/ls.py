import argparse,os
import time
import win32api
import win32con
import win32security

from colorprint.unicolor import FOREGROUND_BLUE
from colorprint.printer import uprint
from argparse import RawDescriptionHelpFormatter

description = ""
usage = '''Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
'''
epilog = '''The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors command to set it.

Exit status:
 0  if OK,
 1  if minor problems (e.g., cannot access subdirectory),
 2  if serious trouble (e.g., cannot access command-line argument).

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/ls>
or available locally via: info '(coreutils) ls invocation\''''

def mod2str(val,isdir=False):
    alres = []
    if isdir:
        alres.append("d")
    else:
        alres.append("-")
    for i in val:
        i = int(i)
        res = []
        res.append("r" if i|4 else "-")
        res.append("w" if i|2 else "-")
        res.append("x" if i|1 else "-")
        alres.append("".join(res))
    return "".join(alres)


prog = "ls"

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("-n","--nn",
                    dest="n",
                    action="store", #store,store_const,store_true/store_false,append,append_const,version
                    type = str,
                    default="",
                    nargs=1,
                    help="help")

parser.add_argument("-l",
                    dest="long_list_format",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="use a long listing format")

parser.add_argument('PATH',
                    metavar='PATH',
                    type=str,
                    nargs="?",
                    default=os.getcwd(),
                    help='help')

parg = parser.parse_args()


path = parg.PATH
long_list_format = parg.long_list_format


fs = os.listdir(path)
for f in fs:
    absf = os.path.join(path,f)
    if long_list_format:
        end = "\n"
    else:
        end = "  "

    if long_list_format:
        fstat = os.stat(absf)
        mod = oct(fstat.st_mode)[-3:]
        mod = mod2str(mod,os.path.isdir(absf))
        owner = fstat.st_uid
        fsize = fstat.st_size
        fctime = fstat.st_ctime
        timestr = time.strftime("%Y-%m-%d %H:%M", time.localtime(fctime))

        sd = win32security.GetFileSecurity(absf, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, type = win32security.LookupAccountSid(None, owner_sid)

        uprint(mod,end="  ")(domain,end="\t")(name)(fsize)(timestr)


    if os.path.isdir(absf):
        uprint(f,fore=FOREGROUND_BLUE,end=end)

    else:
        uprint(f,end=end)

uprint(end="\n")

exit(0)