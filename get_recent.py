import os

with open('recent_files.txt', 'w', encoding='utf-8') as out:
    for root, dirs, files in os.walk('.'):
        for f in files:
            p = os.path.join(root, f)
            mtime = os.path.getmtime(p)
            if mtime > 1792389000: # recent
                out.write(f"{p} | size: {os.path.getsize(p)} bytes\n")
