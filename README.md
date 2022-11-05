# PseudoPY
- The only usable pseudopy file extensions are `.pseudopy` and `.pspy`".
- All pseudocode must be contained within a `main.pspy` file with any suitable pseudopy file extension, or will not be ran by the parser.
- All normal python syntax is still functional and available.
- Indents are no longer neccesary for code to function, however still **highly** recommended as this feature is experimental and may introduce errors to code when used.
- All new pseudocode alternative syntax can be found under the **"Syntax"** section.

## Syntax
- **[v1.0]** [ENDING DENOTATION] `endwhile`, `endfunction`, `endif`, `next i`, etc. can all be used to denote the end of a statement, loop or function.

- **[v1.0]** [FUNCTIONS] `function funcName():` can be used instead of `def funcName():` when defining functions.

- **[v1.1]** [FOR LOOPS] `for x = y to z` can be used instead of `for x in range(y,z)`.

- **[v1.1]** [ANTI-REPLACE] If the parser, for example, changed all instances of one word to another, such as "function" to "def" `(which is done to allow you to define functions using the keyword function instead of def)`, you are able to revert this for specific instances by including a **$** after the word, which will prevent the change and remove itself after doing so, leaving the word unchanged in the final parsed code that is ran. If however, you do want a **visible** **$** to come after the word for whatever reason and this is now preventing that, simply add another **$** as if the first one you added doesn't exist. **This is applicable to all cases when words may be replaced, not just with the word "function"**
- 
## Example Usage

- Example #1 `(For Loops)`
```
for i = 0 to 5:
  print(i)
next i
```

- Example #2 `(While Loops & If Statements)`
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

- Example #3 `(Functions & For Loops $ Anti-Replace)`
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
- **[v1.1]** Overhauled old, rudimentary for loop system to allow any variable to be the iterator and any variable or value to be the beginning or ending parameters.
- **[v1.1]** Implemented $ system (Anti-Replace) to allow for exclusions to be made to how the parser replaces certain words to allow the pseudocode to run in python.
- 
### ARCHIVED INFORMATION
- **[ARCHIVE-DATE] [ARCHIVE-VERSION] [ARCHIVE-REASON] [INFO-TYPE]** INFORMATION 
- **[05/11/22] [v1.1] [Newer, improved system added] [FOR LOOPS]** `= x to y` can be used instead of `in range(x,y)`.
