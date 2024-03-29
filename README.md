# About Calculator
This Calculator is created as my very first project for Turing College, Sprint 1. 08 February, 2023.

# Functionality
This is a Calculator that can be used to:
1. Add numbers;
2. Subtract numbers;
3. Multiply numbers;
4. Divide numbers;
5. Take nth root of a positive numbers.

Calculator has its own memory which can be reset, like in a pocket calculator.

Calculator has user-friendly command line interface, where possible commands are outlined, and calculation results are displayed.

# Instalation
This package is uploaded to PiPI and can be installed using pip command:
pip install calculator_kazbad

To start calculating:
1. Run python (i.e. macOS shell enter: % python)
2. Enter: from calculator_kazbad import calculator
3. Calculator should start running and greet you with list of commands.

# Example
Firs command line prompt outlines the possible operations and user inputs to utilise it. Calculations start with internal memory value of 0. For example:

input: +
input: 1
output: Answer: 1.0

Calculations can continue with a new internal memory value (continuing from previous example):

input: +
input: 1
output: Answer: 2.0

If memory value is 0, and multiplication of division operation is chosen, user is asked to input new value, for example:

input: Answer: 0.0
input: * 
input/output: Type a new multiplier: 10
input/output: Type a multiplicand: 5
output: Answer: 50.0

If n-th root operation is attempted with negative memory value, user is asked to input new value, for example:

Answer: -60.0
n
Type a new positive radicand: 9
Type a root index: 2
Answer: 3.0

# Testing
Calculator methods was tested using 'pytest' package and it passed all 6 tests. Additionally this package has test.py file to repeat tests independently.

# Feedback
Feedback and improvement suggestions on this package is appreciatd. You can create a pull request or open an issue in GitHub.
 
# License
MIT

