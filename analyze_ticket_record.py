import re

with open('5days.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx_oxota = c.find('tn_text_1783443829816000003')
idx_nefrit = c.find('tn_text_1783937391509000251')

print("ОХОТА at:", idx_oxota)
print("НЕФРИТОВЫЕ ОЗЕРА at:", idx_nefrit)

# Find the record enclosing them
rec_oxota = c.rfind('id="rec', 0, idx_oxota)
print("Enclosing rec for ОХОТА:", c[rec_oxota:rec_oxota+30])

rec_nefrit = c.rfind('id="rec', 0, idx_nefrit)
print("Enclosing rec for НЕФРИТ:", c[rec_nefrit:rec_nefrit+30])
