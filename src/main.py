import os
import shutil
from constants import ROOT_DIR
from mdToHtmlNode import mdToHtmlNode
from generatePage import generatePage


def main():
    if os.path.exists(ROOT_DIR + "/public"):
        shutil.rmtree(ROOT_DIR + "/public", ignore_errors=True)
    os.mkdir(ROOT_DIR + "/public")
    copyDirectory(ROOT_DIR + "/static", ROOT_DIR + "/public")


def copyDirectory(source, destination):
    src_contents = os.listdir(path=source)
    for content in src_contents:
        src_path = os.path.join(source, content)
        dest_path = os.path.join(destination, content)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            os.mkdir(dest_path)
            copyDirectory(src_path, dest_path)


if __name__ == "__main__":
    main()
