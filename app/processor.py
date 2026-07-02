import re


def parse_number(s):
    m = re.match(r'^\d+', s)
    if m:
        return int(m.group(0))
    return None
