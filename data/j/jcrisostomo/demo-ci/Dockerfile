FROM node:6.3.1  
MAINTAINER InterWare  
  
RUN mkdir -p /opt/app  
COPY . /opt/app  
RUN cd /opt/app && npm install  
  
WORKDIR /opt/app  
  
CMD ["npm","run", "start"]

