FROM node:6  
MAINTAINER Rafael Roman "rafael@notastica.org"  
ENV DB_PATH=/data/orchestrator.json  
  
ADD . /app  
  
WORKDIR /app  
  
VOLUME /data  
  
RUN npm install  
RUN npm run build  

