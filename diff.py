import difflib

def check_for_changes(lc, cc):
    lc = str(lc)
    lc = lc.splitlines()
    cc = str(cc)
    cc = cc.splitlines()

    differ = difflib.Differ()
    diff = differ.compare(lc, cc)

    changes = []
    for line in diff:
        if line.startswith('+') or line.startswith('-'):
            changes.append(line)

    return changes
