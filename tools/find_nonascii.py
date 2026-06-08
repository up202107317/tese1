from pathlib import Path
p=Path(r"c:\Users\gonca\Downloads\meec-distrib-v2024 (2)\meec-distrib\chapter3.tex")
text=p.read_text(encoding='utf-8')
for i,line in enumerate(text.splitlines(), start=1):
    for j,ch in enumerate(line, start=1):
        if ord(ch)>127:
            print(f"{i}:{j} U+{ord(ch):04X} {ch!r} -> {line}")
            break
