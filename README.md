# Laboratory 6

## Laboratory ObjectivesExplore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using:
	1. input and output
	1. errors and exceptions
1. Run and test a Python program.


## Getting Started
1. Open the Terminal program in Tuffix.
1. Change the present working directory to the `Documents` directory by typing the following command at the command prompt:

    ```
    cd Documents
    ```

1. Make a copy of this Github repository on your computer using the `git` and `clone` commands that you will input to the terminal. The commands take a URL as a parameter to specify where it can get a copy of the repository. You can find the URL by clicking on the green *Clone or download* button at the top right part of this page. Copy the URL and replace the example text shown below. Note that `username` should be replaced with your own Github username. When you hit <kbd>Enter</kbd> it will ask you to provide your Github username and token. Once done, you will have a copy of the repository on your computer.
    ```
    git clone https://github.com/aadi1720/lab06-username.git
    ```
1. Navigate into the new directory using the command line. Note that `username` should be replaced with your own Github username.  As a shortcut, you can type the first few letters of the folder name and press <kbd>Tab</kbd> so that it auto completes the folder name for you.

     ```
     cd lab06-username
     ```
     
## Program Instructions
In this lab assignment, students will work on two Python files: `main.py` and `calculator.py`.

**main.py (Main Program):**

1. Create a Python program named `main.py` that acts as a calculator application. This program will allow users to perform mathematical operations on two input numbers.

1. Implement a function `get_float_input(prompt)` that takes a prompt as an argument and repeatedly asks the user for input until a valid floating-point number is entered. This function should handle potential ValueError exceptions and print an error message when the input is invalid.

1. In the `main` function:
   - Display a welcome message to the user.
   - Use the `get_float_input` function to collect two floating-point numbers from the user: `num1` and `num2`.
   - Utilize the functions from the `calculator` module (provided in `calculator.py`) to perform the following operations:
     - Addition
     - Subtraction
     - Multiplication
     - Division (with error handling for division by zero)

1. Handle exceptions:
   - Use try-except blocks to handle potential exceptions during division. If the user attempts to divide by zero, display an appropriate error message.

1. Create a structured dictionary called `results` to store:
   - The user's input numbers (`num1` and `num2`)
   - The results of the mathematical operations (addition, subtraction, multiplication, and division, with appropriate error messages if applicable).

1. Prompt the user to enter the name of a JSON file where the data should be saved.
   
1. Use the `json` module to save the `results` dictionary as structured JSON data in the specified file. Handle exceptions that may occur during the JSON file saving process and provide meaningful error messages.

**calculator.py (Calculator Module):**

1. Create a Python module named `calculator.py` that contains four mathematical functions: `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, and `divide(a, b)`.

1. Implement each function to perform the corresponding mathematical operation on two input arguments (`a` and `b`).

1. Pay special attention to error handling in the `divide` function. Raise a `ZeroDivisionError` exception if the second argument (`b`) is zero.

1. Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements. 

    ```
	python3 -m main
    
    ```

1. Run the unit testing program to ensure that your program runs as expected.

    ```
	 python3 -m unittest -v test1
	 python3 -m unittest -v test2
    
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `python3 -m unittest -v test` repeatedly until it passes all the test.

## Submission
Periodically throughout the exercise, and when you have completed the exercise, **submit the complete repository to Github**.

   <pre>git add .<br>git commit -m "<i>your comment</i>"<br>git push</pre>

In case it asks you  to configure global variables for an email and name, just copy the commands it provides then replace the dummy text with your email and Github token.

   <pre>git config --global user.email "<i>tuffy@csu.fullerton.edu</i>"<br>git config --global user.name "<i>Tuffy Titan</i>"<br>git commit -m "<i>your comment</i>"<br>git push</pre>

When you completed the final Github push, go back into github.com through the browser interface and ensure all your files have been correctly updated.  You should have the following files:
```
main.py
calculator.py
test_results.json
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|initial git clone of this repository to your Tuffix machine|
|10|main.py file submitted and meets the program requirements |
|10|calculator.py file submitted and meets the program requirements |
|15|unit test passes Test01|
|15|unit test passes Test02|

