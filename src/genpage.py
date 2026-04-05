import os
import shutil
from mdtohtml import mdToHtmlNode


def extractTitle(html):
    title_split = html.split("h1")
    if len(title_split) < 3:
        raise Exception("no valid heading for title generation")
    title = title_split[1][1:len(title_split[1] - 2)]
    return title
