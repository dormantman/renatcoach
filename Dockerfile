FROM python:3.6

RUN apt-get -y update

RUN apt-get install -yqq python-psycopg2
RUN apt-get install -yqq libpq-dev

RUN mkdir /renatcoach
WORKDIR /renatcoach

COPY requirements.txt /renatcoach/

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /renatcoach/
WORKDIR /renatcoach/