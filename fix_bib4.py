#!/usr/bin/env python3
import re

# Read the original file again - we need to start fresh from a backup or the original format
# Since the original had the errors, let me be very aggressive in fixing them

with open('references.bib', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix pattern: 3.$3\ \mathrm{$\mathrm{V}$$}$ -> 3.3\ \mathrm{V}
# This pattern is: decimal.$decimal\ \mathrm{$\mathrm{X}$$}$
content = re.sub(r'(\d+)\.\$(\d+)\\ \\mathrm\{\$\\mathrm\{([^}]+)\}\$\$\}', r'\1.\2\\ \\mathrm{\3}', content)

# Fix pattern: remove stray $ signs in mathrm parameters
# E.g., \mathrm{$X$} -> \mathrm{X}
content = re.sub(r'\\mathrm\{\$([^}]+?)\$\}', r'\\mathrm{\1}', content)

# Ensure number\mathrm pairs are in math mode
content = re.sub(r'([,\s])(\d+)\.\$', r'\1$\2.', content)

# Fix: if we have $X.Y\ \mathrm{...}$ keep it, otherwise wrap it
# Find patterns like: 3.3\ \mathrm{V} that aren't wrapped in $
content = re.sub(r'([,\s])(\d+\.\d+)\\ \\mathrm\{([^}]+)\}(?!\$)', r'\1$\2\\ \\mathrm{\3}$', content)

# Also handle: A$12\ \mathrm{b}$3.3\ \mathrm{V}$ADC
# This should become: A$12\ \mathrm{b}$ $3.3\ \mathrm{V}$ADC or similar
# Specifically: )$....}$X -> )$....}$ X
content = re.sub(r'(\}\$)([A-Z])', r'\1 \2', content)

with open('references.bib', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed all edge cases in references.bib')
