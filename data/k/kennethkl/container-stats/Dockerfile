FROM node:alpine  
  
ADD stats.sh /stats.sh  
  
RUN npm install -g turtle-race \  
&& npm install docker-stats \  
&& chmod +x stats.sh  
  
CMD ./stats.sh

