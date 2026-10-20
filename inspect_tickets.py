import re

with open('tickets_snippets.txt', 'w', encoding='utf-8') as out:
    for fn in ['index.html', '5days.html', '6days.html', '7days.html', '8days.html']:
        with open(fn, 'r', encoding='utf-8') as f:
            c = f.read()
        out.write(f"=== {fn} ===\n")
        
        for word in ['охота', 'нефрит']:
            for m in re.finditer(word, c, re.IGNORECASE):
                start = max(0, m.start() - 300)
                end = min(len(c), m.end() + 300)
                out.write(f"--- Found '{word}' at {m.start()} ---\n")
                out.write(c[start:end] + "\n\n")
