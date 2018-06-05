FROM python:2.7  
MAINTAINER Aditya Wirayudha <adityaw@erasysconsulting.com>  
RUN apt-get update  
RUN apt-get install -y nodejs npm  
RUN apt-get clean -y  
RUN npm cache clean -f  
RUN npm install -g n  
RUN n 5.10.1  
RUN ln -sf /usr/local/n/versions/node/5.10.1/bin/node /usr/bin/node  
RUN npm install -g bower  
RUN pip install fabric awscli --upgrade  

