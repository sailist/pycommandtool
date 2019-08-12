import argparse,os
from argparse import RawDescriptionHelpFormatter

description = '''Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
characters delimited by white space.

The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.'''

usage = None

epilog = '''GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/wc>
or available locally via: info '(coreutils) wc invocation'
'''

prog = "wc"

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("-c","--bytes",
                    dest="bytes",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="print the byte counts")

parser.add_argument("-m","--chars",
                    dest="chars",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="print the character counts")

parser.add_argument("-l","--lines",
                    dest="lines",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="print the newline counts")

parser.add_argument("-L","--max-line-length",
                    dest="max_line_length",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="print the maximum display width")

parser.add_argument("-w","--words",
                    dest="words",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="print the word counts")

parser.add_argument('FILE',
                    metavar='FILE',
                    type=str,
                    nargs='+',
                    help='read input from the files specified by NUL-terminated names in file F;')

parg = parser.parse_args()

clines = parg.lines
cwords = parg.words
cchars = parg.chars
cbytes = parg.bytes
cmax_line_length = parg.max_line_length
fs = parg.FILE

if not cbytes and not cchars and not clines and not cwords and not cmax_line_length:
    clines,cwords,cbytes = True,True,True

count_res = []

# newline, word, character, byte, maximum line length
allres_dict = dict(
    line_count=0,
    word_count=0,
    char_count=0,
    byte_count=0,
    len_count=0
)

switch = dict(
    line_count=clines,
    word_count=cwords,
    char_count=cchars,
    byte_count=cbytes,
    len_count=cmax_line_length
)

for fn in fs:
    res_dict = dict(
        line_count=0,
        word_count=0,
        char_count=0,
        byte_count=0,
        len_count=0
    )
    with open(fn,"rb") as f:
        lines = f.readlines()

        if clines:
            res_dict["line_count"] = len(lines)
        word_count = 0
        char_count = 0
        byte_count = 0
        len_count = 0
        for line in lines:
            dline = line.decode()
            dllen = len(dline)
            if cwords:
                word_count+=len([i for i in dline.strip().split(" ") if len(i) != 0])
            if cchars:
                char_count+=dllen
            if cbytes:
                byte_count+=len(line)
            if cmax_line_length:
                len_count = max(len_count,dllen)
        if clines:
            allres_dict["line_count"] += len(lines)
        if cwords:
            res_dict["word_count"] = word_count
            allres_dict["word_count"] += word_count
        if cchars:
            res_dict["char_count"] = char_count
            allres_dict["char_count"] += char_count
        if cbytes:
            # print(byte_count)
            res_dict["byte_count"] = byte_count
            allres_dict["byte_count"] += byte_count
        if cmax_line_length:
            res_dict["len_count"] = len_count
            allres_dict["len_count"] = max(allres_dict["len_count"],len_count)

    for k, v in res_dict.items():
        if switch[k]:
            print(v,end="\t")
    print(fn)


if len(fs) > 1:
    for k,v in allres_dict.items():
        if switch[k]:
            print(v,end="\t")
    print("total")


exit(0)
