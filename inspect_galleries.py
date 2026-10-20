with open('5days.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

with open('gallery_dump.txt', 'w', encoding='utf-8') as out:
    for gid in ['1783933847930', '1783936212918000124', '1783937391509000249', '1783937721526000412']:
        pos = c.find(f'data-elem-id="{gid}"')
        if pos != -1:
            # find where the elem ends: it might contain nested divs
            # find next elem
            next_elem = c.find('class="t396__elem tn-elem', pos + 20)
            chunk = c[pos-40:next_elem]
            out.write(f"=== Gallery {gid} ===\n")
            out.write(chunk + "\n\n")
