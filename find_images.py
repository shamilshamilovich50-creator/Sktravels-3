import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.png') or 'охот' in f.lower() or 'нефрит' in f.lower() or 'озер' in f.lower() or 'image' in f.lower():
            p = os.path.join(root, f)
            mtime = os.path.getmtime(p)
            size = os.path.getsize(p)
            print(f"{p} | size: {size} | mtime: {mtime}")
