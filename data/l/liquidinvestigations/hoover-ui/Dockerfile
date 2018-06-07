FROM node:7  
RUN mkdir -p /opt/hoover/ui  
WORKDIR /opt/hoover/ui  
  
ADD package.json /opt/hoover/ui/  
RUN npm install  
  
ADD . /opt/hoover/ui/  

