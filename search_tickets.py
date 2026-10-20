import re

for fn in ['index.html', '5days.html', '6days.html', '7days.html', '8days.html']:
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    print(f"=== {fn} ===")
    for word in ['охота', 'охот', 'нефрит', 'арал', 'дополнения', 'tickets', 'ticket']:
        matches = len(re.findall(word, c, re.IGNORECASE))
        print(f"  {word}: {matches}")
