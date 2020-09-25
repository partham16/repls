## Investigation of **Python's `__mro__`**
> in case of a diamond relationship

```
          A
     |          |  
    A1          A2
 |     |         |
B11    B12      B21
   | |     |  |
    D1      D2
```

### Take- Away 
> MRO goes upwards, but, subclass always before parent
