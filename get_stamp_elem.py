with open('5days.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('_6_.png')
start = c.rfind('<div class="t396__elem', 0, idx)
end = c.find('</div> </div>', idx) + 13
elem_code = c[start:end]

with open('oxota_stamp_elem.html', 'w', encoding='utf-8') as f:
    f.write(elem_code)

print("Saved oxota_stamp_elem.html, length:", len(elem_code))
