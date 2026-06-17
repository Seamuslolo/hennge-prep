## Test Case Practice 

# Problem & Assumption
Implement and test an is_even function.


# v1
- Create a function corresponding to each test cases
# v2
- Created two functions using pytest.mark.parametrize for the valid and invalid input.

# What I learned / Would do differnet
- parametrization allows related test cases to share one test function 
- when testing is_even functions with several integer inputs, I can use pytest.mark.parametrize instead of  writing a separate test function for every number.
- Bool is related to int internally, implementation uses an exact type check so boolean input are treated as invalid inputs.
- it tells pytest to run the same test function for each set of arguments provided. number and expected are the parameter names, each tuple provides the vales passed to those parameters 
- python function should use lowercase 
- always add docstring for function

