FROM node:7.8-alpine  
  
# musl-dev is required for the node-sass binary from
https://github.com/sass/node-sass/issues/1589  
RUN npm install -g bower gulp node-sass  
  
COPY ./docker-entrypoint.sh /  
  
WORKDIR /app  
ENTRYPOINT ["/docker-entrypoint.sh"]  

