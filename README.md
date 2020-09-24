# ROT Encoder Challenge for Veeqo

## Installation Instructions
1. Copy and unzip files, `cd` into the directory
1. Install Python (3.7.8) - https://www.python.org/downloads/release/python-378/
1. Install `pip` for package management
    - Note: pip is already installed since your are using Python 3 >=3.4 downloaded from python.org. If you are working in a Virtual Environment created by virtualenv or pyvenv. Just make sure to upgrade pip.
1. Run `pip install -r requirements.txt` to install dependencies
1. Move into rotencode directory `cd rotencoder`
1. Run  `python manage.py runserver` to start the development server
1. Navigate to http://127.0.0.1:8000/encoder


## Notes
- ROT encoder function lives in `rotencoder/encoder/functions.py`
- Run `python functions.py` from `encoder` directory to run tests in the terminal

# Challenge Instructions

## Before you start:

- We do not require you to complete this task in a specific language. Choose one which you are comfortable with
- There is no set time limit to complete this in, as long as it is sent to us by the deadline. We are not looking for perfection or even for you to complete every task listed, but more about the way you think about problems
- Feel free to be creative and add your own features which aren't listed below if you have time
- Please send runnable instructions with your code for us to able to test

## Instructions:

- You are required to create a basic program which implements the basis of a ROT-13 algorithm, taking a string as an input and replacing each letter with the 13th letter after it. For example if I input "hello world" it should return "uryyb jbeyq".
- You should be able to customize the rotation value. IE I should be able to change 13 to any number [ n ] between 1 and 25 and it will replace each letter with the nth letter after it.
- It should not change punctuation or numbers
- It should be case sensitive
- (BONUS) build a client side interface for the program where the user can enter the string and rotation value and then see the returned output

## Test Cases:

- Rotation: 13, User Input: "Hello World", Expected Output: "Uryyb Jbeyq"
- Rotation: 13, User Input: "The Number 16.", Expected Output: "Gur Ahzore 16."
- Rotation: 19, User Input: "Hello World!", Expected Output: "Axeeh Phkew!"