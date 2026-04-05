import os
import shutil
from mdToHtmlNode import mdToHtmlNode


def main():
    ROOT_DIR = "/home/jds1988/myProjects/staticSiteGen"
    if os.path.exists(ROOT_DIR + "/public"):
        shutil.rmtree(ROOT_DIR + "/public", ignore_errors=True)
    os.mkdir(ROOT_DIR + "/public")
    copyDirectory(ROOT_DIR + "/static", ROOT_DIR + "/public")


def copyDirectory(source, destination):
    sourceContents = os.listdir(path=source)
    for content in sourceContents:
        srcPath = os.path.join(source, content)
        destPath = os.path.join(destination, content)
        if os.path.isfile(srcPath):
            shutil.copy(srcPath, destPath)
        else:
            os.mkdir(destPath)
            copyDirectory(srcPath, destPath)


if __name__ == "__main__":
    main()
