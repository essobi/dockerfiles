  
  
FROM ubuntu:14.04  
MAINTAINER Aaron J Ban <ajb@stellaverse.com>  
  
RUN apt-get update && apt-get install -y htop nano curl nodejs npm nodejs-
legacy  
  
RUN mkdir /srv/Hello  
  
ADD . /srv/Hello  
  
RUN cd /srv/Hello && npm install  
  
EXPOSE 3333  
CMD ["nodejs","/srv/Hello/hello.js"]  
  

