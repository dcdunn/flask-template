# Template for a flask website

# Pre-requisites
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
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```

# Build
To build an image to test locally, from the top-level 
```
docker build -f Dockerfile -t app:dev .
```
The tag ```dev``` can of course be anything you like.

To run the container:
```
docker run -p 5000:5000 --name app --rm -d app:dev
```
which will forward ```localhost:5000``` to the flask application. 


# Testing the app
There are unit tests, smoke tests and container tests for the application, intended 
for both local development and for running in a build pipeline. 


## Unit tests
These tests are located in ```tests\unit_tests```. They can be run using the pytest
module. First install the extra python modules needed for running the tests. 
```
pip install -r tests/unit_tests/requirements.txt
python -m pytest tests/unit_tests/
```

### Container tests
The container tests check that the docker container operates correctly.
The tests are run by using ```docker-compose``` to create a network with the
container-under-test and a container that runs a test suite. Before running the tests,
build the container as described above and set an environment variable to tell
```docker-compose``` which container you want to test
```
export APP_CONTAINER=app:dev
cd tests/container_tests
docker-compose build
docker-compose up --exit-code-from testsuite
docker-compose down
```



