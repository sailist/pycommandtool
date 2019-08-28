import argparse,sys,shutil,os
from quickfile import tools
# import tools
from argparse import RawDescriptionHelpFormatter

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
# parser.add_argument("-b",action="store_true",default=False,help="build.cmd, use to run build method.")
# parser.add_argument("-p",action="store_true",default=False,help="pulish.cmd, use to publish python whl.")
parser.add_argument("-s","--save",
                    dest="s",
                    action="store_true",
                    default=False,
                    help="save.")

parser.add_argument("-l","--load",
                    dest="l",
                    action="store_true",
                    default=False,
                    help="load.")

parser.add_argument("-d","--desc",
                    dest="desc",
                    action="store",
                    default="",
                    help="describe.")

parser.add_argument("-o","--open_dir",
                    dest="o",
                    action="store_true",
                    default=False,
                    help="describe.")

parser.add_argument("-b","--bak",
                    dest="b",
                    action="store",
                    default=None,
                    help="describe.")

parser.add_argument("-u","--unbak",
                    dest="u",
                    action="store",
                    default=None,
                    help="describe.")

parser.add_argument('FILE',
                    metavar='FILE',
                    type=str,
                    nargs='*',
                    help='help')


args = parser.parse_args()
l = args.l
s = args.s
d = args.desc
b = args.b
u = args.u
fs = args.FILE
o = args.o
if o:
    os.startfile(tools._store_path)
    exit(0)

if not l and not s and not b and not u:
    l = True

def while_choose(flist,key,origin):
    if key.isdigit():
        flist = [flist[int(key)]]
    else:
        flist = [f for f in flist if os.path.split(f)[1].startswith(key)]

    if len(flist) == 0:
        print(f"no candiate with key '{key}', rechoose please.")
        while_choose(origin,"",origin)

    if len(flist) == 1:
        tools.load(flist[0],"./")
    else:
        print(tools.format_fs(flist))
        key = input(f"please specify use index or fprefix. cur key = {key}")
        while_choose(flist,key,origin)

if s:
    if len(fs) == 0:
        print("save mode must have files")
        exit(1)
    if len(fs) == 1:
        tools.save(fs[0],d)
    for f in fs:
        tools.save(f)
elif l:
    if len(fs)>2:
        print("load mode must specify one file.")
        exit(1)
    if len(fs) == 0:
        try:
            flist = tools.list_curfs()
            while_choose(flist,"",flist)
        except KeyboardInterrupt:
            print()
            exit(1)
elif b:
    tools.bak(b)
elif u:
    tools.unbak(u)

exit(0)