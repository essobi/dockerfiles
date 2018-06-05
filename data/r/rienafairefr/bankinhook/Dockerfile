FROM python:3.4.6-alpine  
  
MAINTAINER Matthieu Berthomé  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh gcc g++ python python-dev py-pip
libxml2-dev libffi-dev libxslt-dev openssl-dev  
  
ENV INSTALL_PATH /bankinhook  
RUN mkdir -p $INSTALL_PATH  
COPY requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
  
COPY . $INSTALL_PATH  
WORKDIR $INSTALL_PATH  
  
EXPOSE 8080  
RUN pip install --editable .  
RUN pip install gunicorn json-logging-py  

