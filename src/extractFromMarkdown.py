import re


def extractMarkdownImages(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extractMarkdownLinks(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches
