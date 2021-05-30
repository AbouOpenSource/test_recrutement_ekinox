FROM python:3.8
MAINTAINER Abou SANOU
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "./main.py" ]