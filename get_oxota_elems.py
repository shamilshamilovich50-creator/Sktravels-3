import re

with open('5days.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('1783443829816000003')
start = c.rfind('<div class="t396__elem tn-elem', 0, idx - 500)
# Let's find all t396__elem in a wider range
sub = c[idx-4000:idx+6000]

matches = list(re.finditer(r'<div class="t396__elem tn-elem [^"]*" data-elem-id="([^"]+)" data-elem-type="([^"]+)"', sub))
with open('oxota_elems.txt', 'w', encoding='utf-8') as out:
    for i, m in enumerate(matches):
        eid = m.group(1)
        etype = m.group(2)
        # find content until next elem or 500 chars
        next_pos = matches[i+1].start() if i+1 < len(matches) else len(sub)
        content = sub[m.start():next_pos]
        
        # find any images or text
        imgs = re.findall(r'(?:data-original|src|background-image:url\([\'"]?)([^\'")\s>]+)', content)
        text = re.sub(r'<[^>]+>', ' ', content)
        text = re.sub(r'\s+', ' ', text).strip()
        
        out.write(f"Elem {i}: id={eid}, type={etype}\n")
        out.write(f"  imgs: {imgs}\n")
        out.write(f"  text: {text[:100]}\n\n")

print("Saved oxota_elems.txt")
