#!/usr/bin/env python3
import re

# Read the file
with open('references.bib', 'r', encoding='utf-8') as f:
    content = f.read()

# The real fix: replace \mathrm{...} with $ \mathrm{...} $ to keep them in math mode
# We need to wrap all \mathrm{unit} patterns with $ signs

# Pattern 1: Units appearing in titles without proper math delimiters
# Find patterns like: \mathrm{b}, \mathrm{MHz}, \mathrm{MS/s}, etc
# that are not already in math mode

# First, handle already-fixed patterns (those without $ signs around them)
# These should be wrapped in $ signs for math mode
content = re.sub(r'(\d+)\\ \\mathrm\{b\}(?![\$}])', r'$\1\\ \\mathrm{b}$', content)
content = re.sub(r'(\d+)\\ \\mathrm\{([^}]+)\}(?![\$}])', r'$\1\\ \\mathrm{\2}$', content)

# Handle cases like: at20\ \mathrm{MHz} -> at $20\\ \\mathrm{MHz}$
content = re.sub(r'at(\d+)\\ \\mathrm\{([^}]+)\}', r'at $\1\\ \\mathrm{\2}$', content)

# Handle cases like: for digital IF extraction at20\ \mathrm{MHz}
content = re.sub(r'(\d+)\\ \\mathrm\{([^}]+)\}(?=[A-Za-z}])', r'$\1\\ \\mathrm{\2}$', content)

# Write back
with open('references.bib', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed references.bib successfully')
