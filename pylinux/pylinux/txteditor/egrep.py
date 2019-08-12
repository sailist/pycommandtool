import re,argparse,sys,os
from argparse import RawDescriptionHelpFormatter
from colorprint.printer import uprint
from colorprint.unicolor import FOREGROUND_GREEN,FOREGROUND_RED,FOREGROUND_PINK


'''
--color   用颜色显示出来
-v        条件取反
-i        忽略大小写
-c        统计匹配的行数
-q        静默，无任何输出，一般用于检测。如果$?是0说明有匹配，否则没有
-n        显示出匹配结果所在的行号
'''
# usage = "Usage: grep [OPTION]... PATTERN [FILE]..."
usage = None


description = '''Search for PATTERN in each FILE or standard input.
PATTERN is, by default, a basic regular expression (BRE).
Example: egrep -i 'hello world' menu.h main.c'''

epilog ='''This egrep is an imitation of egrep in linux, I try my best to do it but as you 
can see, it's not completed.

When FILE is -, read standard input.  With no FILE, read . if a command-line
-r is given, - otherwise.  If fewer than two FILEs are given, assume -h.
Exit status is 0 if any line is selected, 1 otherwise;
if any error occurs and -q is not given, the exit status is 2.

Report bugs to: sailist@outlook.com
my github page: <http://www.gnu.org/software/grep/>
'''

prog = "egrep"

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("-v","--invert-match",
                    dest="invert_match",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    help="select non-matching lines",
                    default=False,)
parser.add_argument("-i","--ignore-case",
                    dest="ignorec_case",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    help="ignore case distinctions",
                    default=False,)
parser.add_argument("-n","--line-number",
                    dest="line_number",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    help="print line number with output lines",
                    default=False,)
parser.add_argument("-c","--count",
                    dest="count",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    help="print only a count of matching lines per FILE",
                    default=False,)
parser.add_argument("-o","--only-matching",
                    dest="only_matching",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    help="show only the part of a line matching PATTERN",
                    default=False,)
# parser.add_argument("-v","--nn",
#                     dest="invert_match",
#                     action="store_true", #store,store_const,store_true/store_false,append,append_const,version
#                     type = str,
#                     default="",
#                     nargs=1)

parser.add_argument('PATTERN',
                    metavar='PATTERN',
                    type=str,
                    help='By default, a basic regular expression (BRE).')
parser.add_argument('FILE',
                    metavar='FILE',
                    type=str,
                    nargs='+',
                    help='place markdown path')


args = parser.parse_args()

ignore_case = args.ignorec_case
pattern = args.PATTERN
invert_match = args.invert_match
line_number = args.line_number
only_matching = args.only_matching
count = args.count
files = args.FILE

if ignore_case:
    egrex = re.compile(pattern,re.IGNORECASE)
else:
    egrex = re.compile(pattern)

all_num = 0
multi_file = len(files) != 1


for file in files:
    # print(file)
    cur_num = 0
    with open(file,"rb") as f:
        for i,line in enumerate(f):
            line = line.decode().strip("\n")
            match = re.search(egrex,line)


            if match is None and invert_match:
                cur_num += 1
                if not only_matching:

                    if not count:
                        if multi_file:
                            uprint(file, fore=FOREGROUND_PINK)

                        if line_number:
                            uprint(f"{i + 1}:", fore=FOREGROUND_GREEN)

                        uprint(line,end="\n")
            elif match is not None and not invert_match:
                cur_num += 1

                if not count:
                    if multi_file:
                        uprint(file, fore=FOREGROUND_PINK)

                    if line_number:
                        uprint(f"{i + 1}:", fore=FOREGROUND_GREEN)
                    elif multi_file:
                        uprint(f":", fore=FOREGROUND_GREEN)

                    if only_matching:
                        uprint(line[match.start():match.end()],fore=FOREGROUND_RED,end="\n")
                    else:
                        uprint(line[0:match.start()])
                        uprint(line[match.start():match.end()],fore=FOREGROUND_RED)
                        uprint(line[match.end():],end="\n")
        if count:
            if multi_file:
                uprint(file,fore=FOREGROUND_PINK)
                uprint(":",fore=FOREGROUND_GREEN)
            uprint(cur_num,end="\n")
    all_num += cur_num

if all_num == 0:
    print(f"pattern:{pattern} matches none.")
    exit(1)
else:
    exit(0)
