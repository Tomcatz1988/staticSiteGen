import os
import shutil
import sys
from mdtohtml import mdToHtmlNode
from genpage import generatePage


def main():
    basepath = "/" if len(sys.argv) > 0 else os.path.dirname(os.path.dirname(sys.argv[0])) + "/"
    dest_path = basepath + "docs"
    static_path = basepath + "static"
    md_path = basepath + "content"
    template_path = basepath + "template.html"

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path, ignore_errors=True)
    os.mkdir(dest_path)
    copyDirectory(static_path, dest_path)
    generatePageRecursive(md_path, template_path, dest_path, basepath)


def copyDirectory(src_path, dest_path):
    src_contents = os.listdir(path=src_path)
    for content in src_contents:
        new_src_path = os.path.join(src_path, content)
        new_dest_path = os.path.join(dest_path, content)
        if os.path.isfile(new_src_path):
            shutil.copy(new_src_path, new_dest_path)
        else:
            os.mkdir(new_dest_path)
            copyDirectory(new_src_path, new_dest_path)


def generatePageRecursive(src_path, template_path, dest_path, basepath):
    src_contents = os.listdir(path=src_path)
    for content in src_contents:
        new_src_path = os.path.join(src_path, content)
        new_dest_path = os.path.join(dest_path, str(content).replace(".md", ".html"))
        if os.path.isfile(new_src_path):
            generatePage(new_src_path, template_path, new_dest_path, basepath)
        else:
            os.mkdir(new_dest_path)
            generatePageRecursive(new_src_path, template_path, new_dest_path, basepath)


if __name__ == "__main__":
    main()
