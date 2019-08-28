import os,zipfile


def unzip(zippath,path):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(zippath)
    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)
    for names in zip_file.namelist():
        zip_file.extract(names,path)
    zip_file.close()

def zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    if os.path.isdir(source_dir):
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)     #相对路径
                zipf.write(pathfile, arcname)
    else:
        zipf.write(source_dir,source_dir)
    zipf.close()

if __name__ == '__main__':
    zip("./","../k.zip")
    unzip("../k.zip","../tmp/",)