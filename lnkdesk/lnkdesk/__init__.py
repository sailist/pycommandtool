# coding:utf-8
# GetLink.py
# hbxcyz.cn
import os
import pythoncom
import winshell


def create_shortcut_to_desktop(target,title):
    """Create shortcut to desktop"""
    s = os.path.basename(target)
    fname = os.path.splitext(s)[0]
    winshell.CreateShortcut(Path = os.path.join(winshell.desktop(), fname + '.lnk'),
                            Target = target,
                            Icon=(target, 0),
                            Description=title)



if __name__ == "__main__":
    import os

    Desttop_path = r"C:\Users\saili\Desktop\\"


    create_shortcut_to_desktop(r"E:\Python\pycommandtool\lnkdesk\lnkdesk\lnk.py","lnk")
