FROM node:6.10.2-alpine  
  
MAINTAINER Mikhail.Angelov (@MikhailAngelov)  
  
RUN mkdir -p /opt/bconf  
WORKDIR /opt/bconf  
  
RUN export TERM=xterm  
RUN npm install forever -g  
  
COPY ./package.json ./  
COPY ./yarn.lock ./  
RUN yarn install --production  
  
COPY ./dist dist  
COPY ./snode snode  

