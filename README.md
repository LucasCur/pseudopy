# PseudoPY
- All pseudocode must be contained within the "main.pseudopy" master file or will not be ran by the parser
- All normal python syntax is still functional and available
- Indents are no longer neccesary for code to function, however still highly recommended as this feature is experimental and may introduce errors to code when used
- All new pseudocode alternative syntax can be found under the "Syntax" section

## Syntax
- [v1.0] [ENDING DENOTATION] "endwhile", "endfunction", etc. can all be used to denote the end of a statement/loop/function
- [v1.0] [FUNCTIONS] "function" can be used instead of "def" when defining functions
- [v1.1] [FOR LOOPS] "for x = y to z" can be used instead of "for x in range(y,z)"
- [v1.1] [SYNTAX] If the parser changes all instances of "function" to "def" to make the pseudocode run in python, however for an instance you want this to not be the case (i.e. you referenced function in the string "i am using a function because xyz" and the parser changed this to "i am using a def because xyz", then include a $ after "function" and this will be ignored from the parsing. After doing this, "i am using a function$ because xyz" will become "i am using a function because xyz" inside your string. If however, you want a $ to come after the word function in a string for whatever reason and this is now preventing that, simply add a second $)

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

## Changelog
- [v1.1] Overhauled old, rudimentary for loop system to allow any variable to be the iterator and any variable or value to be the beginning or ending parameters.
- [v1.1] Implemented $ system to allow .
- 
### ARCHIVED INFORMATION
- [ARCHIVE-DATE] [ARCHIVE-VERSION] INFORMATION 
