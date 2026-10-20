import re

with open('5days.html', 'r', encoding='utf-8') as f:
    c = f.read()

with open('ticket_records.txt', 'w', encoding='utf-8') as out:
    m = list(re.finditer(r'<div class="r t-rec"[^>]*id="([^"]+)"', c))
    for i, r in enumerate(m):
        start = r.start()
        end = m[i+1].start() if i+1 < len(m) else len(c)
        block = c[start:end]
        if 'ОХОТА' in block or 'НЕФРИТ' in block or 'ДОПОЛНЕНИЯ' in block:
            out.write(f"Record {r.group(1)} (length {len(block)}):\n")
            elems = re.findall(r'data-elem-id="([^"]+)"\s+data-elem-type="([^"]+)"', block)
            out.write(f"  Total elems: {len(elems)}\n")
            for eid, etype in elems:
                pos = block.find(eid)
                elem_chunk = block[max(0, pos-50):min(len(block), pos+1000)]
                text = re.sub(r'<[^>]+>', ' ', elem_chunk)
                text = re.sub(r'\s+', ' ', text).strip()
                imgs = re.findall(r'(?:data-original="([^"]+)"|src="([^"]+)"|background-image:url\([\'"]?([^\'")\s>]+))', elem_chunk)
                flat_imgs = [i for group in imgs for i in group if i]
                out.write(f"    elem {eid} ({etype}): text='{text[:60]}', imgs={flat_imgs}\n")
