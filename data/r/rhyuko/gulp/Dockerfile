FROM debian  
MAINTAINER Rhyuko <rvolhuer@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y build-essentials nodejs npm  
  
RUN npm install --global gulp-cli  
  
RUN mkdir data  
WORKDIR /data  
  
RUN npm install  
RUN gulp watch  
  
VOLUME /data  

