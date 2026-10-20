import re

with open('5days.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

for rid in ['rec2461795101', 'rec2465978771']:
    pos = c.find(f'id="{rid}"')
    if pos != -1:
        start = c.rfind('<div class="r t-rec"', 0, pos)
        print(f"{rid}: {c[start:pos+35]}")
