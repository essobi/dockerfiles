FROM ubuntu:14.04  
MAINTAINER Anton Serdyuk <anton.serdyuk@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm git  
  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
RUN npm install -g strider@1.6.4  
  
CMD ["strider"]

