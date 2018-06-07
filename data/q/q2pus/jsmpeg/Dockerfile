FROM node:6-alpine  
  
RUN apk add --no-cache ffmpeg \  
&& npm -g install http-server  
  
COPY jsmpeg /opt/jsmpeg  
  
RUN cd /opt/jsmpeg \  
&& npm install ws  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

