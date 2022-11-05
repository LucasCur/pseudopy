from os import system as sys
from random import choice
import re

sys("clear")

differences = [["function ","def "]]

codefile = open("main.pseudopy", "r").read()

for iteration in range(0,len(differences)):
  codefile = codefile.replace(differences[iteration][0],differences[iteration][1])

codefile = open("main.pseudopy", "r").read()
code = [i.strip() for i in codefile.splitlines() if i.strip() != ""]

for line in range(0,len(code)):
    code[line] = re.sub("([A-Za-z0-9]+) = ([A-Za-z0-9]+) to ([A-Za-z0-9]+)", "\\1 in range(\\2, \\3)", code[line])
    code[line] = re.sub("function ([A-Za-z0-9]+)()", "def \\1", code[line])
    code[line] = code[line].replace("function$", "function")

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

exec(parse(code), {"$pseudopy_ver": 1.1})
