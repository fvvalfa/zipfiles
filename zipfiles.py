#!/usr/bin/env python3
import os
import argparse
import zipfile



parser = argparse.ArgumentParser()
parser.add_argument("dir", help="Directory",
                    type=str)
parser.add_argument("ext", help="Extension",
                    type=str)
parser.add_argument("-d", dest='del_file', action='store_true', help="Delete source files")
args = parser.parse_args()
print(args.dir)

print(os.path.abspath(args.dir))
print('.'+args.ext)

for cur_dir, sub_dir, files in os.walk(os.path.abspath(args.dir)):
    for file in files:
        if file.endswith('.'+args.ext):
            full_path_file = os.path.join(cur_dir, file)
            file_wo_ext = os.path.splitext(file)[0]
            full_path_file_wo_ext = os.path.splitext(full_path_file)[0]
            zip_obj = zipfile.ZipFile(file=full_path_file+'.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
            zip_obj.write(full_path_file, arcname=file)
            zip_obj.close()
            if args.del_file:
                os.remove(full_path_file)
            print(full_path_file+" archived")

