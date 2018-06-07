FROM node:boron-alpine  
MAINTAINER Juan Luis Baptiste <juan.baptiste@gmail.com>  
ENV STORJ_CONFIG_FILE "/config/config.json"  
RUN apk update && \  
apk add --no-cache bash g++ git make openssl-dev python vim openrc openntpd
tmux && \  
npm install --global storjshare-daemon && \  
npm cache clean && \  
apk del git openssl-dev python vim && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/npm* && \  
storjshare --version  
ADD *.sh /  
RUN chmod 755 /run.sh  
  
CMD ["/run.sh"]  
EXPOSE 4000-4003  

