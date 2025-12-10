#!/usr/bin/env python3
import re

# Read the original file
with open('references.bib', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern 1: Wrap number\ \mathrm{unit} with $ signs
# This handles: 10\ \mathrm{b} -> $10\ \mathrm{b}$
content = re.sub(r'(\d+)\\ \\mathrm\{([^}]+)\}', r'$\1\\ \\mathrm{\2}$', content)

# Write back
with open('references.bib', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed references.bib successfully - wrapped mathrm in math mode')
