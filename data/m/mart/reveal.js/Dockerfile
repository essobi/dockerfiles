FROM ubuntu:14.04  
MAINTAINER Martin Migasiewicz <sowasdummes@gmail.com>  
  
RUN apt-get update  
RUN apt-get update && apt-get install -y wget  
RUN apt-get update && apt-get install -y nodejs npm nodejs-legacy  
RUN npm install -g grunt-cli  
  
# Obtain reveal.js  
ENV VERSION 3.0.0  
RUN wget https://github.com/hakimel/reveal.js/archive/$VERSION.tar.gz  
RUN tar zxvf $VERSION.tar.gz  
RUN rm $VERSION.tar.gz  
RUN mv reveal.js-$VERSION /revealjs  
  
# Install reveal.js dependencies  
RUN cd /revealjs && npm install  
  
EXPOSE 8000  
RUN mkdir /revealjs/md  
WORKDIR /revealjs  
  
ENTRYPOINT grunt serve  
  

