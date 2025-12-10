#!/usr/bin/env python3
import re

with open('references.bib', 'r', encoding='utf-8') as f:
    content = f.read()

# The proper fix: ensure all \mathrm commands are inside $ ... $
# Pattern: }$X.Y\ \mathrm{...}$ should be }$ X.Y\ \mathrm{...}$
# or better: }$ X.Y\ \mathrm{...}$ A should be }$ X.Y\ \mathrm{...}$ A

# Fix: }$ at end of mathrm should have space before next letter
content = re.sub(r'(\$\s+[\d\.]+\\ \\mathrm\{[^}]+\}\$)([A-Z])', r'\1 \2', content)

# Fix: ensure 3.3\ \mathrm{V} that's not in $ is wrapped
content = re.sub(r'(\$[\d\w\\ \\\\mathrm\{[^}]+\}\$)(\d+\.\d+\\ \\mathrm\{[^}]+\})(?!\$)', 
                 r'\1$\2$', content)

# Simpler approach: wrap any digit\.\digit\ \mathrm{...} that's not already in $
content = re.sub(r'([^\$])(\d+\.\d+\\ \\mathrm\{[^}]+\})([^\$])', r'\1$\2$\3', content)

# Fix the specific case in line 11: 3.3\ \mathrm{V}$ A should be 3.3\ \mathrm{V}$ A
# Actually if it's already }$ A then it's: $12\ \mathrm{b}$3.3\ \mathrm{V}$ ADC
# which should be: $12\ \mathrm{b}$ $3.3\ \mathrm{V}$ ADC
content = re.sub(r'(\}\$)(\d+\.\d+\\ \\mathrm\{[^}]+\}\$)', r'\1 $\2', content)

with open('references.bib', 'w', encoding='utf-8') as f:
    f.write(content)

print('Applied final comprehensive fix')
