#  
# Network of Innovators Dockerfile for web  
#  
# https://github.com/govlab/noi2  
#  
FROM debian:jessie  
MAINTAINER John Krauss <john@thegovlab.org>  
  
RUN apt-get update && apt-get -y dist-upgrade  
RUN apt-get install -y python-pip libpq-dev python-dev postgresql-client-9.4
libffi-dev curl  
  
RUN mkdir -p /noi/app  
COPY . /noi/app  
  
RUN pip install --upgrade pip  
RUN pip install -r /noi/app/requirements.txt  
  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g postcss-cli autoprefixer  
  
EXPOSE 5000  

