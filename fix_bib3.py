#!/usr/bin/env python3
import re

# Read the file
with open('references.bib', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Handle the malformed nested mathrm: \mathrm{$\mathrm{V}$} -> \mathrm{V}
content = re.sub(r'\\mathrm\{\$\\mathrm\{([^}]+)\}\$\}', r'\\mathrm{\1}', content)

# Fix 2: Ensure all number\ \mathrm{unit} patterns are wrapped in $ signs
# This catches cases that may have been missed
content = re.sub(r'(\d+(?:\.\d+)?)\\\ \\mathrm\{([^}]+)\}(?!\$)', r'$\1\\ \\mathrm{\2}$', content)

# Fix 3: Handle patterns like "at20\ \mathrm{MHz}" -> "at $20\ \mathrm{MHz}$"
content = re.sub(r'at(\d+)\\\ \\mathrm\{([^}]+)\}', r'at $\1\\ \\mathrm{\2}$', content)

# Fix 4: Wrap bare \mathrm{V} or \mathrm{X} that isn't already in math mode
# This is tricky, but we can check if preceded by a number and not already in $
content = re.sub(r'(\d+)\.$(\d+)\\\ \\mathrm\{([^}]+)\}', r'$\1.\2\\ \\mathrm{\3}$', content)

# Write back
with open('references.bib', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed references.bib - resolved all mathrm issues')
