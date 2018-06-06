# Working from ubuntu where python3 is default (3.6.2 currently)  
FROM python:3  
MAINTAINER Bil Bas  
  
RUN mkdir /code  
  
# Python  
WORKDIR /code  
ENV PYTHONUNBUFFERED 1  
COPY requirements.txt /code/  
RUN pip install -r requirements.txt  
  
# Nodejs  
WORKDIR /tmp  
RUN apt-get update  
RUN apt-get install curl -y  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
nodejs -y  
RUN npm install webpack -g  
COPY package.json /tmp/  
RUN npm install  
  
# webpack  
WORKDIR /code  
COPY webpack.config.js /code/webpack.config.js  
COPY assets /code/assets/  
RUN cp -a /tmp/node_modules /code/  
RUN webpack  
RUN mkdir -p logs  
  
COPY . /code/

