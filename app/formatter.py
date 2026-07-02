import re

def format_report(title: str, count: int, data: dict) -> str:
    report = f"Report: {title!r} | Items: {count:,} | Rate: {count/float(data.get('total', 1))*100:.2f}%"
    return report

def process_lines(text: str) -> list:
    results = []
    lines = text.splitlines()
    for line in lines:
        m = re.match(r'\w+=(\d+)', line)
        if m:
            results.append({'key': m.group(1), 'val': int(m.group(2))})
        elif line.strip():
            results.append({'raw': line.strip()})
    return results
