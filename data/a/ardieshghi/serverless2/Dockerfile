FROM node:6.10  
MAINTAINER Ardeshir Eshghi  
  
RUN apt-get update -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy python-pip groff-base
git python2.7-dev curl less  
RUN pip install awscli  
  
RUN \  
npm install -g serverless  

