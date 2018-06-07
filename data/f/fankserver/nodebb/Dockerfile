FROM node:6-alpine  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk add --no-cache ssmtp bash git  
  
RUN mkdir -p /usr/src/app && \  
chown -R node:node /usr/src/app  
WORKDIR /usr/src/app  
  
VOLUME ["/usr/src/app"]  
  
USER node  
ENTRYPOINT ["/entrypoint.sh"]  

