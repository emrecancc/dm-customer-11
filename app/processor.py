import re


def process_line(line):
    m = re.match(r'(\w+)=(\d+)', line)
    if m:
        key, value = m.group(1), int(m.group(2))
        return {key: value}
    return None


def process_file(filepath):
    results = []
    with open(filepath, 'r') as f:
        for line in f:
            res = process_line(line.strip())
            if res:
                results.append(res)
    return results
