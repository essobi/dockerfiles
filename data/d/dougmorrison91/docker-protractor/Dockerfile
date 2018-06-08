FROM node:0.12.7  
MAINTAINER doug.morrison91@gmail.com  
  
RUN apt-get update --fix-missing  
RUN apt-get install --yes --force-yes netcat git xvfb chromium openjdk-7-jre-
headless libgconf-2-4 libexif12  
  
COPY . /src  
  
RUN npm update -g  
RUN cd /src; npm install  
RUN /src/node_modules/.bin/webdriver-manager update --standalone  

