# PASS_W6
Welcome to week 6's coding activity
- Note: you're not allowed to use in-built lists, sets and dictionaries
- To run tests, open terminal then:
```sh
python3 run_tests.py # and follow command line instructions
```

- If you encounter errors with the above, make sure that at least python runs on terminal
```sh
python3
```

- You may be directed to Microsoft Store (Windows), if so install python from there
- For if issues persist on Mac,  see this: https://docs.python-guide.org/starting/install3/osx/

---

### Q1: Maximum Nesting Depth of the Parentheses (adapted from [here](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/))
You are given a valid parentheses string (i.e. every open `(` there is a matching `)` later in the string). You are limited to using linked structures (linked queue/stack/list).

Nesting depth of `()` is 1  
Nesting depth of `(())` is 2  
Maximum nesting depth of `((()()()))` is 3  

Return an Integer represent the maximum nesting depth of the string

Example 1:

**Input**: s = "(1+(2*3)+((8)/4))+1"  
**Output**: 3  
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

**Input**: s = "(1)+((2))+(((3)))"  
**Output**: 3  


Note: 
- String consists of letters, numbers and one type of parentheses `()`

Extension: Can you do this without using any data structures? 


---
### Q2: Get book titles at and after start year

You are given a list of book objects sorted by publication year, `books`, and an integer `start_year`. Return an Iterable (any object with the `__iter__` method) of all book titles having a publication year greater than `start_year`. 

Extension: Write an algorithm that does not you any additional data structure and has an initial time complexity of O(log(n)), where n = number of books 

*Examples*

**Input**:  
`books` = [Book("Nineteen Eighty-Four", 1949, "George Orwell"), Book("To Kill a Mockingbird", 1960, Harper Lee), Book("The Handmaid's Tale", 1985, Margaret Atwood), Book("The Da Vinci Code", 2003, Dan Brown), Book("The Road", 2006, Cormac McCarthy)]  
`start_year` = 1984

**Output**: Iterable of collection ("The Handmaid's Tale", "The Da Vinci Code", "The Road")


