import argparse,sys,shutil,os
from argparse import RawDescriptionHelpFormatter

templete_path = os.path.join(os.path.split(__file__)[0],"templete")
bfn = "build.cmd"
gfn = "gitpush.cmd"
pfn = "publish.cmd"

if len(sys.argv) == 1:
    try:
        typ = input("please choose a templete:\nb:build.cmd\tg:gitpush.cmd\tp:publish.cmd")
        sys.argv.append(typ)
    except KeyboardInterrupt:
        exit(0)

parser = argparse.ArgumentParser(prog = "quickfile",
                                 description="",
                                 epilog="",
                                 formatter_class=RawDescriptionHelpFormatter)
parser.add_argument("-b",action="store_true",default=False)
parser.add_argument("-p",action="store_true",default=False)
parser.add_argument("-g",action="store_true",default=False)

args = parser.parse_args()

cur_dir = os.getcwd()
if args.b:
    shutil.copy(os.path.join(templete_path,bfn),os.path.join(cur_dir,bfn))

if args.g:
    shutil.copy(os.path.join(templete_path, gfn), os.path.join(cur_dir, gfn))

if args.p:
    shutil.copy(os.path.join(templete_path, pfn), os.path.join(cur_dir, pfn))