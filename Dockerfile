FROM python:3.7.4-alpine

WORKDIR /var/www
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install wheel
RUN python -m pip install -r requirements.txt

ENV FLASK_APP run.py
CMD python -m flask run -h 0.0.0.0 -p 5000
