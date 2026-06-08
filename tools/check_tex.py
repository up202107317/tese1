from pathlib import Path
p=Path(r"c:\Users\gonca\Downloads\meec-distrib-v2024 (2)\meec-distrib\chapter3.tex")
text=p.read_text(encoding='utf-8')
print('Total $ count:', text.count('$'))
print('Total \{ count:', text.count('{'))
print('Total \} count:', text.count('}'))
# find lines with odd number of $ in line
for i,l in enumerate(text.splitlines(), start=1):
    if l.count('$')%2==1:
        print('Odd $ at line', i, '->', l)
# simple brace balance per line
balance=0
for i,l in enumerate(text.splitlines(), start=1):
    balance += l.count('{') - l.count('}')
    if balance<0:
        print('Negative balance at line', i)
print('Final brace balance:', balance)
