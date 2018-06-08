FROM node:6-alpine  
  
RUN apk --no-cache add python su-exec git make g++  
  
RUN npm install ssb-patchwork -g  
  
COPY docker-entrypoint /docker-entrypoint  
  
VOLUME /home/node/.ssb  
ENTRYPOINT ["/docker-entrypoint"]  
EXPOSE 7777  

