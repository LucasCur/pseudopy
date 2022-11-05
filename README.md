# PseudoPY
- All pseudocode must be contained within the "main.pseudopy" master file or will not be ran by the parser
- All normal python syntax is still functional and available
- Indents are no longer neccesary for code to function, however still highly recommended as this feature is experimental and may introduce errors to code when used
- All new pseudocode alternative syntax can be found under the "Syntax" section

## Syntax
- [v1.0] [ENDING DENOTATION] "endwhile", "endfunction", "endif", "next i", etc. can all be used to denote the end of a statement, loop or function.

- [v1.0] [FUNCTIONS] "function" can be used instead of "def" when defining functions.

- [v1.1] [FOR LOOPS] "for x = y to z" can be used instead of "for x in range(y,z)".

- [v1.1] [ANTI-REPLACE] If the parser changed all instances of "function" to "def" inside your code to make the pseudocode run in python, however for a singular instance or multiple instances you want this to not be the case (i.e. you referenced the word "function" in a string and the parser changed it to "def", then include a $ after "function" and this instance of function will not be replaced. If however, you want a $ to come after the word function inside your code for whatever reason and this is now preventing that, simply add another $ as if the first one you added doesn't exist).

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

- Example #3 (Functions & For Loops $ Anti-Replace)
```
function funcName(argument):
  for i = 0 to argument:
    print("the function$ says:")
    print(i)
  next i
endfunction

funcName(10)
```

## Changelog
- [v1.1] Overhauled old, rudimentary for loop system to allow any variable to be the iterator and any variable or value to be the beginning or ending parameters.
- [v1.1] Implemented $ system to allow .
- 
### ARCHIVED INFORMATION
- [ARCHIVE-DATE] [ARCHIVE-VERSION] [ARCHIVE-REASON] [INFO-TYPE] INFORMATION 
- [05/11/22] [v1.1] [Newer, improved system added] [FOR LOOPS] "= x to y" can be used instead of "in range(x,y)".
