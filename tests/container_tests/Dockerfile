FROM python:3.7.4-alpine

WORKDIR /tests
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install wheel
RUN python -m pip install -r requirements.txt

CMD python -m pytest . --doctest-modules --junitxml=test_results/container-test-results.xml
