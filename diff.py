import difflib

def check_for_changes(lc, cc):

    lc = lc.splitlines()
    cc = cc.splitlines()

    differ = differlib.Differ()
    diff = differ.compare(lc, cc)

    changes = []
    for line in diff:
        if line.startswith('+') or line.startswith('-'):
            changes.append(line)

    return changes
