import os
import shutil
from constants import ROOT_DIR
from mdtohtml import mdToHtmlNode
from genpage import generatePage


def main():
    dest_path = ROOT_DIR + "/public"
    static_path = ROOT_DIR + "/static"
    md_path = ROOT_DIR + "/content"
    template_path = ROOT_DIR + "/template.html"

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path, ignore_errors=True)
    os.mkdir(dest_path)
    copyDirectory(static_path, dest_path)
    generatePageRecursive(md_path, template_path, dest_path)


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


def generatePageRecursive(src_path, template_path, dest_path):
    src_contents = os.listdir(path=src_path)
    for content in src_contents:
        new_src_path = os.path.join(src_path, content)
        new_dest_path = os.path.join(dest_path, str(content).replace(".md", ".html"))
        if os.path.isfile(new_src_path):
            generatePage(new_src_path, template_path, new_dest_path)
        else:
            os.mkdir(new_dest_path)
            generatePageRecursive(new_src_path, template_path, new_dest_path)


if __name__ == "__main__":
    main()
