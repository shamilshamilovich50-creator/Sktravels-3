with open('5days.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect around 'ОХОТА' in 5days.html
idx = c.find('ОХОТА')
start = max(0, idx - 1500)
end = min(len(c), idx + 2500)

with open('dump_oxota.html', 'w', encoding='utf-8') as f:
    f.write(c[start:end])

print("Written dump_oxota.html")
