from pathlib import Path
p=Path(r"c:\Users\gonca\Downloads\meec-distrib-v2024 (2)\meec-distrib\chapter3.tex")
lines=p.read_text(encoding='utf-8').splitlines()
for idx in [171,173,239,240,247]:
    l=lines[idx-1]
    print('\nLine {}: {}'.format(idx,repr(l)))
    for i,ch in enumerate(l, start=1):
        print('{:03d} U+{:04X} {}'.format(i, ord(ch), ch))
    print('---')
