FROM node:0.10  
MAINTAINER Tim Rupe <tim@rupe.org>  
  
ADD . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm install -g bower-registry  
  
EXPOSE 8888  
CMD ["./bowerRegistry.sh"]  

