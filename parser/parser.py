from os import system as sys
from random import choice
import re

sys("clear")

differences = [["= 0 to 10","in range(0,10)"],["= 0 to 5","in range(0,5)"],["function ","def "]]

codefile = open("main.pseudopy", "r").read()
for iteration in range(0,len(differences)):
  codefile = codefile.replace(differences[iteration][0],differences[iteration][1])

code = [i.strip() for i in codefile.splitlines() if i.strip() != ""]

def removestrings(string):
    varpattern = "(\"|\')(.*?)(\"|\')"
    while len(re.findall(varpattern, string)) != 0:
        search = re.search(varpattern, string)
        if search:
            span = list(search.span())
            string = string.replace(string[span[0]:span[1]], " " * len(string[span[0]:span[1]]))
    return string

def parse(code):
    final = ""
    indent = 0
    for j, k in enumerate(code):
        for i, v in enumerate(k.splitlines()):
            v = v.strip()
            if v == "endfunction":
                indent -= 1
                v = ""
                continue
            elif v == "endif":
                indent -= 1
                v = ""
                continue
            elif v == "endwhile":
                indent -= 1
                v = ""
                continue
            elif "next " in v:
                indent -= 1
                v = ""
                continue
            if v.split()[0] in ["if", "elif", "else", "for", "while", "def", "class", "try", "except", "finally"]:
                v = "    " * indent + v
                indent += 1
            else: v = "    " * indent + v
            final += v + "\n"

    return "\n".join([i for i in final.splitlines() if i != ""])

exec(parse(code), {"$pseudopy_ver": 1.0})