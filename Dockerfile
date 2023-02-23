FROM python:3.8

RUN mkdir /profanity-check-ui/

WORKDIR /profanity-check-ui/

COPY requirements.txt requirements.txt

COPY . /profanity-check-ui/

RUN pip install -r requirements.txt

RUN python3 -m spacy download en
