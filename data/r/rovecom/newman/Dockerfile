FROM node:4.6.2-alpine  
MAINTAINER Erwin Steffens <esteffens@rovecom.nl>  
  
ENV NEWMAN_VERSION 3.3.0  
RUN npm install -g newman@${NEWMAN_VERSION};  
  
WORKDIR /work  
  
CMD ["newman", "--version"]

