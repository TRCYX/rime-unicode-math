from itertools import *
import re

FILE_NAMES = {
    "\\": "unicode_math",
    "@": "unicode_math_at",
    ";": "unicode_math_semi",
}

VERSION = "0.1.7"

FILE_START = rf"""---
name: {{name}}
version: "{VERSION}"
sort: original
...

# Escape
{{start}}	{{start}}{{start}}

"""

CMD_REGEX = re.compile(r"^<!-- (.*) -->$")

with open("source.md", "r", encoding="utf8") as source:
    sources = tee(source, len(FILE_NAMES))
    for lines, (start, name) in zip(sources, FILE_NAMES.items()):
        with open(f"{name}.dict.yaml", "w", encoding="utf8") as dest:
            dest.write(FILE_START.format(name=name, start=start))

            use = True
            for line in lines:
                if "\t" in line:
                    if use:
                        symbol, code = line.split("\t", 1)
                        dest.write(f"{symbol}\t{start}{code}")
                    use = True
                elif m := re.match(CMD_REGEX, line):
                    cmd = m[1]
                    if cmd == f"NO {start}":
                        use = False
                        continue
                else:
                    dest.write(line)
