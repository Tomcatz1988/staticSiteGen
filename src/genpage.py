import os
import shutil
from mdtohtml import mdToHtmlNode


def extractTitle(html):
    title_split = html.split("h1")
    if len(title_split) < 3:
        raise Exception("no valid heading for title generation")
    title = title_split[1][1:len(title_split[1]) - 2]
    return title


def generatePage(src_path, template_path, dest_path, basepath):
    print(f"Generating page from \'{src_path}\' to \'{dest_path}\' using template \'{template_path}\'")
    file = open(src_path)
    md = file.read()
    file.close()
    file = open(template_path)
    template = file.read()
    file.close()
    
    html = mdToHtmlNode(md).toHtml()
    title = extractTitle(html)
    page = template.replace(
        "{{ Title }}", title).replace(
        "{{ Content }}", html).replace(
        "href=\"/", f"href=\"{basepath}").replace(
        "src=\"/", f"src=\"{basepath}"
    )

    os.makedirs(os.path.abspath(os.path.dirname(dest_path)), exist_ok=True)
    file = open(dest_path, mode='w')
    file.write(page)
    file.close()
