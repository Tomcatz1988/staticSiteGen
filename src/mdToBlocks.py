def mdToBlocks(markdown):
    blocks = markdown.split('\n\n')
    stripped_blocks = []
    for block in blocks:
        tmp_block = block.strip()
        if tmp_block != "":
            stripped_blocks.append(tmp_block)
    return stripped_blocks
