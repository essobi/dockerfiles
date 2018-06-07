FROM node  
MAINTAINER Christoph Bühler <christoph@smartive.ch>  
  
COPY startup.sh /startup.sh  
  
RUN npm install -g supervisor bower tsd node-gyp && \  
mkdir /app && \  
chmod +x /startup.sh && \  
apt-get update && \  
apt-get install -y python make gcc  
  
ENV IGNORE_FILES="noop" MAIN_FILE="app.js" EXTENSIONS="node,js,json"
WATCHING="."  
EXPOSE 9000 3001  
CMD ["/startup.sh"]  

