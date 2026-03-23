def markdownToBlocks(markdown):
    blocks = markdown.split('\n\n')
    stripped_blocks = []
    for block in blocks:
        stripped_blocks.append(block.strip())
        if block == "":
            del block
    return stripped_blocks
