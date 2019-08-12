import argparse
from argparse import RawDescriptionHelpFormatter

description = ""
usage = None
epilog = ""

prog = ""

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

# parser.add_argument('FILE',
#                     metavar='FILE',
#                     type=str,
#                     nargs='+',
#                     help='help')

parg = parser.parse_args()

print(parser.print_help())
print(parg)