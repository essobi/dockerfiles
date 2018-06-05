FROM python:3.6-alpine3.6  
MAINTAINER Dave Chevell  
  
WORKDIR /usr/src/app  
  
RUN apk --update add git openssh  
  
COPY requirements.txt /usr/src/app/requirements.txt  
RUN pip install --upgrade pip && pip install --no-cache-dir -r
requirements.txt  
  
COPY . /usr/src/app

