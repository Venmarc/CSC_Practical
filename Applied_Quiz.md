# APPLIED QUIZ

## APPLIED QUIZ 1

1. **Compilation of python program before execution is valid TRUE or FALSE?**
   - **Answer:** FALSE
   *Explanation: Python is an interpreted language. While it does compile to bytecode (.pyc) automatically at runtime, it is generally considered an interpreted language and does not require an explicit compilation step by the user like C or Java.*

2. **Fill the blank to display the string "I love python programming"**
   - `>>>` **print**("I love python programming")

3. **What kind of error will this expression cause: `>>>(17+94)/(-5+5)`**
   - **Answer:** ZeroDivisionError
   *Explanation: `-5 + 5` equals `0`. Division by zero is not allowed.*

4. **`__________` and `__________` are used to determine quotient and remainder of a division.**
   - **Answer:** `//` (floor division) and `%` (modulus)

5. **Write a simple python code to assign "Hello World" to a variable `a`, and print.**
   - **Answer:**
     ```python
     a = "Hello World"
     print(a)
     ```

6. **Complete the code to create a string Weather with variable M**
   - `>>> M = "Weather"`

7. **What will be the output of the code below**
   ```python
   >>> float("45" * int(input("enter a number")))
   # When enter a number: 7
   ```
   - **Answer:** `45454545454545.0`
   *Explanation: `int("7")` is `7`. The string `"45"` is repeated 7 times, resulting in `"45454545454545"`. `float()` converts it to a floating-point number.*

---

## APPLIED QUIZ 2

1. **`__________` and `__________` are the two Boolean values for python.**
   - **Answer:** `True` and `False`

2. **Which part of an *if statement* is indented?**
   - **Answer:** The body (or the code block to be executed if the condition is true).

3. **What part of the code above is print or displayed part.**
   ```python
   sam = 6
   if sam > 3:
       print("nice name")
   else:
       print("what is the meaning")
   ```
   - **Answer:** `nice name`
   *Explanation: `sam` is 6, which is greater than 3, so the `if` block executes.*

4. **Fill in the blank spaces using the *if statement***
   ```python
   a = 20
   b = 34
   __________ a > b:
       print("you got it")
   ```
   - **Answer:** `if not` (or potentially just `if`, but the condition `a > b` is False, so it wouldn't print. Assuming the goal is to make it print "you got it", `if not a > b:` or `if b > a:` would work. Given "Fill in the blank... a>b", `if not` fits best to make the condition true).
   *Note: If the question implies just syntax, `if` is the keyword.*

5. **What is the output for this expression: `>>> Not 2==2 or 2>1`**
   - **Answer:** `True`
   *Explanation: `2==2` is True, so `Not True` is False. `2>1` is True. `False or True` is `True`.*

6. **What is the output of this code below**
   ```python
   >>> number = [2, 5, 3, 6, 2, 1]
   >>> number.reverse()
   >>> number
   ```
   - **Answer:** `[1, 2, 6, 3, 5, 2]`

7. **How many item are in this list A = [2, 4, 5, 6, 8]**
   - **Answer:** 5

8. **Fill in the blank spaces to create a list B and print the 4th element**
   - `B = [6, 7, 10, 1, 2]`
   - `print(B[3])`

9. **`__________` is used to end the while loop prematurely**
   - **Answer:** `break`

10. **Fill the blank for the code below using for....loop to iterate the variable Student_name**
    ```python
    Student_name = ["John", "Ruth", "Paul", "Joe", "Emma"]
    for student in Student_name:
        # (body of loop)
    ```

---

## APPLIED QUIZ 3

1. **Arrange the following in the order of execution: `hello()`, `def`, `hello():`, `print("Hello! How are you?")`.**
   - **Answer:**
     1. `def hello():` (Function Definition)
     2. `hello()` (Function Call)
     3. `print("Hello! How are you?")` (Execution within function)

2. **What would be the result of the below:**
   ```python
   def calculate(x, y):
       s = x + y
       print(s)
   calculate(3, -5)
   ```
   - **Answer:** `-2`

3. **Fill in the blank spaces to define a function "shortest" that compares the length of its argument and return the shortest value.**
   ```python
   def shortest(a, b):
       if len(a) <= len(b):
           return a
       else:
           return b
   ```

4. **How would you close a file stored in a variable "course_work.txt"?**
   *Assuming the variable holding the file object is named `f` or similar, as "course_work.txt" is the filename.*
   - **Answer:** `file_variable.close()` (e.g., `f.close()`)
