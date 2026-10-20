import re

with open('5days.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

with open('stamp_elements.txt', 'w', encoding='utf-8') as out:
    def analyze_rec(rec_id):
        pos = c.find(f'id="{rec_id}"')
        end = c.find('<!-- /T396 --> </div>', pos)
        chunk = c[pos:end]
        
        matches = list(re.finditer(r'<div class="t396__elem tn-elem ([^"]*)" data-elem-id="([^"]+)" data-elem-type="([^"]+)"([\s\S]*?)<div class="tn-atom[^"]*"([^>]*)>([\s\S]*?)</div>\s*</div>', chunk))
        out.write(f"=== {rec_id} has {len(matches)} elements ===\n")
        
        for m in matches:
            cls = m.group(1)
            eid = m.group(2)
            etype = m.group(3)
            attrs = m.group(4)
            atom_attrs = m.group(5)
            atom_body = m.group(6)
            
            clean_text = re.sub(r'<[^>]+>', ' ', atom_body).strip()
            
            img_match = re.search(r'data-original="([^"]+)"|src="([^"]+)"|background-image:url\([\'"]?([^\'")\s>]+)', atom_attrs + atom_body)
            img = img_match.group(1) or img_match.group(2) or img_match.group(3) if img_match else ""
            
            left_m = re.search(r'data-field-left-value="([^"]+)"', attrs)
            top_m = re.search(r'data-field-top-value="([^"]+)"', attrs)
            width_m = re.search(r'data-field-width-value="([^"]+)"', attrs)
            height_m = re.search(r'data-field-height-value="([^"]+)"', attrs)
            
            left = left_m.group(1) if left_m else "?"
            top = top_m.group(1) if top_m else "?"
            w = width_m.group(1) if width_m else "?"
            h = height_m.group(1) if height_m else "?"
            
            out.write(f"  [{eid}] ({etype}) w={w}, h={h}, left={left}, top={top} | img={img} | text={clean_text[:40]}\n")

    analyze_rec('rec2461795101')
    analyze_rec('rec2465978771')
