import difflib

def check4changes(lc, cc):
    lc = str(lc).splitlines()
    cc = str(cc).splitlines()

    differ = difflib.Differ()
    diff = differ.compare(lc, cc)

    changes = []
    for line in diff:
        if line.startswith('+ ') or line.startswith('- '):
            changes.append(line)

    return "\n".join(changes)
