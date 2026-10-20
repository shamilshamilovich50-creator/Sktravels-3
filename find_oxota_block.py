with open('5days.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('tn_text_1783443829816000003') # This is ОХОТА
print("ОХОТА tn_text at:", idx)

# Find the record id enclosing this
rec_start = c.rfind('<div class="r t-rec"', 0, idx)
rec_snippet = c[rec_start:rec_start+150]
print("Record tag:", rec_snippet)

# Let's find the closing of this record
rec_end = c.find('<!-- /T396 --> </div>', idx)
print("Record end at:", rec_end)
print("Record length:", rec_end - rec_start)

# Save the whole record
with open('ticket_record_full.html', 'w', encoding='utf-8') as out:
    out.write(c[rec_start:rec_end+50])

print("Saved ticket_record_full.html")
