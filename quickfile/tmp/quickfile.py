import argparse,sys,shutil,os
from argparse import RawDescriptionHelpFormatter

templete_path = os.path.join(os.path.split(__file__)[0],"templete")
bfn = "build.cmd"
gfn = "gitpush.cmd"
pfn = "publish.cmd"
sfn = "setup.py"

if len(sys.argv) == 1:
    try:
        typ = input("please choose a templete:\nb:build.cmd\tg:gitpush.cmd\tp:publish.cmd\n")
        sys.argv.append(f"-{typ}")
    except KeyboardInterrupt:
        exit(0)

description = '''
一行命令快速建立模板，可能使用ide会好一些不过我还是用了命令行，感觉配置文件不是很容易在不同设施之间同步。

目前支持创建的有：
- setup.py, 用于发布Python库时候的模板文件,只需要把其中todo的部份改好就可以了
- build.cmd, 包含了自动利用setup.py文件进行编译并且在目录内寻找到最近的版本并安装到本地的命令
- publish.cmd, 包含了使用twine自动发布的命令
- gitpush.cmd, 包含了add,commit,push三条命令,在开头会提示输入commit信息
'''

parser = argparse.ArgumentParser(prog = "quickfile",
                                 description=description,
                                 epilog="to be continued",
                                 formatter_class=RawDescriptionHelpFormatter)
parser.add_argument("-b",action="store_true",default=False,help="build.cmd, use to run build method.")
parser.add_argument("-p",action="store_true",default=False,help="pulish.cmd, use to publish python whl.")
parser.add_argument("-g",action="store_true",default=False,help="gitpush.cmd, use to auto push your project.")
parser.add_argument("-s",action="store_true",default=False,help="setup.py, use to build python whl.")
parser.add_argument("--proot",action="store_true",default=False,help="same as [-bpg]")
parser.add_argument("-a","--all",dest="all",action="store_true",default=False,help="same as [-bpgs]")




args = parser.parse_args()

cur_dir = os.getcwd()

if args.all:
    shutil.copy(os.path.join(templete_path, bfn), os.path.join(cur_dir, bfn))
    shutil.copy(os.path.join(templete_path, gfn), os.path.join(cur_dir, gfn))
    shutil.copy(os.path.join(templete_path, pfn), os.path.join(cur_dir, pfn))
    shutil.copy(os.path.join(templete_path, sfn), os.path.join(cur_dir, sfn))
    exit(0)

if args.proot:
    shutil.copy(os.path.join(templete_path, bfn), os.path.join(cur_dir, bfn))
    shutil.copy(os.path.join(templete_path, gfn), os.path.join(cur_dir, gfn))
    shutil.copy(os.path.join(templete_path, pfn), os.path.join(cur_dir, pfn))
    exit(0)

if args.b:
    shutil.copy(os.path.join(templete_path,bfn),os.path.join(cur_dir,bfn))

if args.g:
    shutil.copy(os.path.join(templete_path, gfn), os.path.join(cur_dir, gfn))

if args.p:
    shutil.copy(os.path.join(templete_path, pfn), os.path.join(cur_dir, pfn))

if args.s:
    shutil.copy(os.path.join(templete_path, sfn), os.path.join(cur_dir, sfn))


exit(0)