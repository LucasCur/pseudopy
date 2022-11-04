# PseudoPY
- All pseudocode must be contained within the "main.pseudopy" master file or will not be ran by the parser
- All normal python syntax is still functional and available
- Indents are no longer neccesary for code to function, however still highly recommended as this feature is experimental and may introduce errors to code when used
- All new pseudocode alternative syntax can be found under the "Syntax" section

## Syntax
- [v1.0] [ENDING DENOTATION] "endwhile", "endfunction", etc. can all be used to denote the end of a statement/loop/function
- [v1.0] [FOR LOOPS] "= x to y" can be used instead of "in range(x,y)"
- [v1.0] [FUNCTIONS] "function" can be used instead of "def" when defining functions


## Example Usage

- Example #1 (For Loops)
```
for i = 0 to 5:
  print(i)
next i
```

- Example #2 (While Loops & If Statements)
```
x = True
y = 0
while x == True:
  y += 1
  print(y)
  if y >= 5:
    x = False
  endif
endwhile
```

- Example #3 (Functions & For Loops)
```
function funcName(argument):
  for i = 0 to argument:
    print(i)
  next i
endfunction

funcName(10)
```

### ARCHIVED INFORMATION
- [ARCHIVE-DATE] [ARCHIVE-VERSION] INFORMATION 
