import re

with open('5days.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's find the record for tickets.
# In 5days.html:
# Let's search for 'АРАЛЬСКОЕ' or 'ДОПОЛНЕНИЯ К ВАШЕМУ МАРШРУТУ'
pos = c.find('ДОПОЛНЕНИЯ')
print("ДОПОЛНЕНИЯ position:", pos)

rec_start = c.rfind('<div class="r t-rec"', 0, pos)
# Let's see what rec this is
m = re.search(r'id="(rec\d+)"', c[rec_start:rec_start+100])
rec_id = m.group(1) if m else "unknown"
print(f"Record containing ДОПОЛНЕНИЯ: {rec_id}")

# Let's find all records from here until the next major section (e.g. hotels)
pos_hotels = c.find('ОТЕЛИ', pos)
print("Hotels position:", pos_hotels)

tickets_block = c[rec_start:pos_hotels]
print("Tickets block length:", len(tickets_block))

# Find all records in tickets_block
recs = re.findall(r'<div class="r t-rec[^"]*"[^>]*id="([^"]+)"', tickets_block)
print("Records in tickets section:", recs)

# For each record, let's find all images and texts
for r in recs:
    r_pos = tickets_block.find(r)
    r_next = tickets_block.find('class="r t-rec"', r_pos + 10)
    chunk = tickets_block[r_pos:r_next if r_next != -1 else len(tickets_block)]
    texts = re.findall(r'<div class="tn-atom"[^>]*>([\s\S]*?)</div>', chunk)
    clean_texts = [re.sub(r'<[^>]+>', '', t).strip() for t in texts if len(re.sub(r'<[^>]+>', '', t).strip()) > 2]
    imgs = re.findall(r'(?:data-original|src|background-image:url\([\'"]?)([^\'")\s>]+)', chunk)
    print(f"\n--- Record {r} ---")
    print("  Texts:", clean_texts[:8])
    print("  Imgs:", [i for i in imgs if not i.endswith(('.svg', '.js', '.css'))][:5])
