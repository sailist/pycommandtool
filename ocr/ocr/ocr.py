import argparse
import pyperclip
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageGrab
from argparse import RawDescriptionHelpFormatter


description = "识别中文汉字"
usage = None
epilog = ""

prog = ""

parser = argparse.ArgumentParser(prog=prog,
                                 usage=usage,
                                 description=description,
                                 epilog=epilog,
                                 formatter_class=RawDescriptionHelpFormatter)

parser.add_argument("-s","--shell",
                    dest="shell",
                    action="store_true", #store,store_const,store_true/store_false,append,append_const,version
                    default=False,
                    help="help")

parser.add_argument('FILE',
                    metavar='FILE',
                    type=str,
                    nargs='*',
                    help='help')

parg = parser.parse_args()

fs = parg.FILE
shell = parg.shell

from cnocr import CnOcr
ocr = CnOcr()
def mergelines(res):
    for line in res:
        if line[-1] in [".","。"]:
            line.append("\n")
    return "".join(["".join(line) for line in res])

if shell:
    try:
        print("wait any input.")
        while True:
            i = input()
            print("start.")
            im = ImageGrab.grabclipboard()
            if im is not None:
                im = np.asarray(im)
                res = ocr.ocr(im)
                res = mergelines(res)
                print(res)
                pyperclip.copy(res)
    except KeyboardInterrupt:
        print("bye")
        exit(0)
else:
    ims = []
    if len(fs) == 0:
        im = ImageGrab.grabclipboard()
        if im is not None:
            im = np.asarray(im)
            ims.append(im)
    else:
        for f in fs:
            ims.append(plt.imread(f))

    if len(ims) == 0:
        print("No image to recognition.")
        exit(1)

    ress = []
    for im in ims:
        res = ocr.ocr(im)
        res = mergelines(res)
        print(res)
        ress.append(res)

    pyperclip.copy("\n".join(ress))

    exit(0)