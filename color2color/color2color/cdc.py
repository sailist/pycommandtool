import argparse
import pyperclip
import re
from argparse import RawDescriptionHelpFormatter

re_numrgb = re.compile("([0-9]+)[, ]+([0-9]+)[, ]+([0-9]+)")
re_digrgb = re.compile("([0-9.]*)[, ]+([0-9.]*)[, ]+([0-9.]*)")
re_hexrgb = re.compile("#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})")


description = "convert color from one format to another format"
usage = None
epilog = ""

prog = "cdc"

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("-n","--num",
                    dest="n",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="help")
parser.add_argument("-f","--float",
                    dest="f",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="help")
parser.add_argument("-e","--hex",
                    dest="h",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="help")

parser.add_argument('colors',
                    metavar='colors',
                    type=str,
                    nargs='*',
                    help='help')

parg = parser.parse_args()

cs = parg.colors
n = parg.n
f = parg.f
h = parg.h

if not n and not f and not h:
    f = True

if len(cs) == 0:
    cs = [pyperclip.paste()]

res = []
for color in cs:
    print(color)

    match_num = re.search(re_numrgb,color)
    match_float = re.search(re_digrgb,color)
    match_hex = re.search(re_hexrgb,color)

    if match_hex:
        color = int(match_hex.group(1), 16), int(match_hex.group(2), 16), int(match_hex.group(3), 16)
    elif match_num:
        color = int(match_num.group(1)), int(match_num.group(2)), int(match_num.group(3))
    elif match_float:
        color = float(match_float.group(1)), float(match_float.group(2)), float(match_float.group(3))
        color = [int(i*255) for i in color]
    else:
        print(f"error color format of{color}, exit.")
        exit(1)
    if n:
        res.append(",".join([str(i) for i in color]))
    elif f:
        res.append(",".join([f"{i/255:.4f}" for i in color]))
    elif h:
        color = [hex(i)[-2:] for i in color]
        res.append(f"#{color[0]}{color[1]}{color[2]}")

res = "\n".join(res)
print(res)
print("result has been copy to the clipboard.")
pyperclip.copy(res)

exit(0)