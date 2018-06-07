FROM ubuntu:latest  
RUN apt-get update  
RUN apt-get install -y git  
  
MAINTAINER Aamir Latif <aamir@vendr.tech>  
  
FROM node  
  
RUN npm install sails -g  
  
RUN mkdir -p /service/app  
WORKDIR /service/app  
  
#FROM vendr/financials:latest  
COPY package.json /service/app  
#RUN export PATH="$HOME/usr/bin/git/bin:$PATH"  
RUN npm install --production  
  
COPY . /service/app  
  
EXPOSE 80  
CMD NODE_ENV=production sails lift

