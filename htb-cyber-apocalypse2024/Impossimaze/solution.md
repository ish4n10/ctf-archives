The challenge gave a hint to NCurses, i am not sure but it is related to text based interface.

If we look at the code, there's "getmaxx" and "getmaxy" functions used, which returns max x or y coordinate.

These values are compared with 13 and 37 respectively, and if it passes, it executes the statement inside the condition, if we just set manually using stty 


```
stty rows 13 cols 37
```

and run the challenge, we get the flag displayed.