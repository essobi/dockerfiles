FROM node:7  
MAINTAINER Joseph Estefane <estefanejoe@gmail.com>  
  
RUN apt-get update \  
&& apt-get install git \  
&& apt-get clean  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install -g gulp bower jshint  
  
WORKDIR /mnt  
  
VOLUME ["/mnt"]

