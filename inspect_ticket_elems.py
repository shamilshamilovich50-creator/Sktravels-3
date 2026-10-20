import re

with open('5days.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's find elements around 'ОХОТА'
idx = c.find('ОХОТА')
# Look 2000 chars before and 2000 chars after
snippet = c[max(0, idx - 2500):min(len(c), idx + 2500)]
elems = re.findall(r'<div[^>]*class="[^"]*tn-elem[^"]*"[^>]*data-elem-id="([^"]+)"[^>]*data-elem-type="([^"]+)"[^>]*>([\s\S]*?)</div>\s*</div>', snippet)

print(f"Found {len(elems)} elements around ОХОТА:")
for eid, etype, body in elems:
    clean_body = re.sub(r'<[^>]+>', ' ', body)
    clean_body = re.sub(r'\s+', ' ', clean_body).strip()
    img_match = re.search(r'data-original="([^"]+)"|background-image:url\([\'"]?([^\'")]+)', body)
    img = img_match.group(1) or img_match.group(2) if img_match else ""
    print(f"  id: {eid} | type: {etype} | img: {img} | text: {clean_body[:40]}")
