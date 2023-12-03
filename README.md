# Take-Home Test

## Explanations of the different files

### test_1.py
This script processes log lines.
    - 'is_log_line()' validates whether a line of a .log file is valid (has a valid
       timestamp, error, and message). A boolean is returned from this function.
    - 'get_dict' converts the lof data into a dictionary format. 

Lines 55 onwards contain inbuilt tests which were expected to be left unaltered. 


### test_2.py & test_test_2.py
The 'test_2.py' script reads from an API which contains data about the nearest courts given a valid
postcode endpoint. Data, including the postcode of relevant individuals, is read from the 
'people.csv' and ultimately used to generate a dictionary containing the person's 
information and the details of the required court. 

    - 'read_csv()' extracts data from the relevant csv about the people and puts it in a list. 
    - 'get_nearest_courts()' finds the courts closest to each person based on their postcode
       and returns all of the relevant information for that entry (person's name, desired court,
       person's postcode, name of nearest desired court, dx number, distance to court).
    - 'format_extracted_data()' converts the data from the previous function into a list of 
        dictionaries.

The 'test_test_2.py' file tests the function returns, and the expected errors, of test_2.py


### test_3.py & test_test_3.py
The 'test_3.py' script contains one function ('sum_current_time()'), which takes in an input 
time string of format "HH:MM:SS" and adds the values of HH, MM, and SS. It returns an integer. 

The 'test_test_3.py' file tests that 'sum_current_time()' returns the expected answer, and that
it raises an error if the input is not a string. 


## Original Instructions:

#### Data engineering Python tests

> For interviews in April 2022.

This test is to assess your ability to write Python code and to discuss how you think about coding problems during the interview. Don't worry if you don't complete the whole test - you can still pass the interview.

You should have been introduced to a person you can contact to clarify questions or solve technical issues. If anything is unclear or something is wrong, ask them as soon as possible. Asking questions will not affect how we score you on the test, so it is better to ask sooner rather than later.

You are free to use the internet to solve these tests and you can install additional packages. However, the solutions to this test can be achieved using Python and its standard libraries. Use whatever you're most comfortable with. This coding test was written and tested with python 3.8.

##### Working with the code

If you can, clone this repo and work on your solutions on your own computer. 

If you don't have a computer where you can do this, you can [complete the test on Google Colab](https://colab.research.google.com/drive/1jIYgeEKarkr6FHAnys6wVSoTIl24PjW6?usp=sharing) instead. Please create a copy of the notebook before you start.

During the interview we'll ask you to share your screen to show and discuss your solutions. You don't need to push your changes to Github or save them anywhere else.


##### Doing the tests

There are 3 scripts in the root of this repo/directory:

- test_1.py
- test_2.py
- test_3.py

These scripts do not need to be completed in order, but we do recommend you do.

In each script is a comment block starting with `[TODO]`. This lays out what needs to be done to solve the test for that particular script. The remaining comments are there to explain the code and direct you.

##### Test 1
This asks you to extract and structure data from the file `sample.log`. You'll need to complete 2 short functions.

When you think you have the answer, run `python test_1.py` and it will be automatically tested.

##### Test 2
This asks you do get data from an API and match it with data from the file `people.csv`. 

You're free to approach this however you like. We'll ask you to describe your approach and reasoning during the interview.

##### Test 3
This asks you to fix a broken function and then write a unit test for it.
