# Bit by Bit

Bitwise operators are operators used on binary numbers. Examples include:
- And(&)
- Or(|)
- Xor(^)
- Not(~)
- Shift(>> or << for dir)

# And
And is the first one, represented by &, it says:
if a = 1 **and** b = 1, c = 1
else c = 0
so here is the table


| **a value** | **b value** | **c value** |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

# Or
Or is next, represented by |, it says:
if either a = 1 **or** b = 1, then c = 1
else c = 0
so here is the table


| **a value** | **b value** | **c value** |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

# Xor
Xor is the next major operator, represented by ^, it says:
if a is not equal b, c = 1, 
else c = 0
so here is the table


| **a value** | **b value** | **c value** |
| :--- | :--- | :--- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

it also gives the last place for binary addition

# Not
Not is the simplest, if a = 1 then b = 0 but if a = 0 then b = 1


| **a value** | **b value** |
| :--- | :--- | :--- |
| 0 | 1 |
| 1 | 0 |

# Larger Numbers

Let us try

```python
b001010110 & b101101100
```
You take the and for each digit

that would be
| d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

Same digit by digit for or, xor, not, etc

# Left/Right Shift

When shifting a large binary number, you do this for example 

``` python
b011010110 >> b011
```


| d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 |
| 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |

in the shift dir, it replaces with 0s

# The Project

The project is a 2d led lighting. each led is a bit, I have 8, 8-bit numbers that each change with the leds. The colors are 24-bit numbers circular shifted(Out shifted numbers put on other side) numbers that change to create the patterns


