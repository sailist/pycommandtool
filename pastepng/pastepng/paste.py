from PIL import ImageGrab
import argparse
from argparse import RawDescriptionHelpFormatter
import time,os
description = "save clipboard image"
usage = None
epilog = ""

prog = ""

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

# parser.add_argument("-n","--nn",
#                     dest="n",
#                     action="store", #store,store_const,store_true/store_false,append,append_const,version
#                     type = str,
#                     default="",
#                     nargs=1,
#                     help="help")

parser.add_argument('FILE',
                    metavar='FILE',
                    type=str,
                    nargs='?',
                    help='help')

parg = parser.parse_args()

fpre = parg.FILE


#转换成localtime

if not fpre:
    time_local = time.localtime(time.time())
    # 转换成新的时间格式(2016-05-05 20:28:54)
    fpre = time.strftime("%y%m%d%H%M%S", time_local)

fname = os.path.abspath(f"{fpre}.png")

im = ImageGrab.grabclipboard()
if im:

    im.save(fname,'PNG')
    print(f"save to {fname}")
else:
    print("clipboard doesn't have image.")
    exit(1)

exit(0)