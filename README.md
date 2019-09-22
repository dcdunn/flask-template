# Template for a flask website

# Testing the app
There are unit tests, smoke tests and container tests for the application, intended 
for both local development and for running in a build pipeline. 

## Unit tests
These tests are located in ```tests\unit_tests```. They can be run using the pytest
module. First install the extra python modules needed for running the tests. 
```
pip install -r tests/requirements.txt
python -m pytest tests/unit_tests/


# Building the site locally
Create a python3 virtual environment:
```
python3 -m venv venv
```
and activate it
```
source venv/bin/activate
```

You can now pull the modules that are needed for the site:
```
pip install wheel
pip install -r requirements.txt
```


