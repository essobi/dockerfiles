FROM node:8  
RUN mkdir /src  
  
ENV GIT_DIR=/src  
  
RUN npm install -g webpack webpack-cli  
RUN npm install -g pm2  
RUN npm install -g node-gyp  
  
WORKDIR /src  
  
# Setup startup script  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

