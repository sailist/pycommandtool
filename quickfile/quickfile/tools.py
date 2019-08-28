import os,zipfile,shutil
_store_path = os.path.join(os.getenv("APPDATA"),".quickfile")

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

def list_curfs():
    fspath = _store_path
    os.makedirs(fspath, exist_ok=True)
    res = os.listdir(fspath)
    res = [os.path.join(fspath,f) for f in res if not f.endswith("..desc")]
    return res

def _type_string(f:str):
    if f.endswith("zip"):
        return "dir"
    else:
        return "file"

def _raw_file_string(f:str):
    _,fn = os.path.split(f)
    if f.endswith("zip"):
        return os.path.splitext(fn)[0]
    else:
        return fn

def _load_desc(f):
    descf = f"{f}..desc"
    if os.path.exists(descf):
        with open(descf,encoding="utf-8") as f:
            return f.readline()
    else:
        return ""
def format_fs(fs):
    res = "\n".join(["\t".join([str(i),_type_string(f),_raw_file_string(f),_load_desc(f)])
                     for i,f in enumerate(fs)])
    return res

def _init_path():
    os.makedirs(_store_path,exist_ok=True)

def save(fpath,desc:str = None):
    _init_path()
    _,fn = os.path.split(fpath)
    if os.path.isdir(fpath):
        output_path = os.path.join(_store_path, f"{fn}.zip")
        zip(fpath, output_path)
    else:
        output_path = os.path.join(_store_path, fn)
        shutil.copy(fpath,output_path)
    if desc:
        with open(os.path.join(_store_path,f"{fn}..desc"),"w",encoding="utf-8") as w:
            w.write(desc.strip())
    print(output_path)

def load(loadf:str,outputpath:str):
    _,fn = os.path.split(loadf)
    if loadf.endswith("zip"):
        unzip(loadf,outputpath)
    else:
        shutil.copy(loadf,os.path.join(outputpath,fn))

def bak(output):
    if not os.path.exists(output):
        output = os.path.join(output)
    elif not os.path.isdir(output):
            print("output path must be a path.")
            exit(1)
    zip(_store_path,os.path.join(output,"bak.zip"))

def unbak(source:str):
    if not source.endswith(".zip"):
        print("bak file must be zip file, do not change it.")
        exit(1)

    unzip(source,os.path.join(_store_path,"../"))


