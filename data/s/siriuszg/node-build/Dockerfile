FROM node:7.4.0-alpine  
  
MAINTAINER siriuszg <zhigang52110@sina.com>  
  
RUN mkdir -p /usr/local/node && mkdir -p /etc/node-cache  
  
RUN npm config set cache "/etc/node-cache"  
  
ADD ./exec.sh /usr/local/node  
  
RUN chmod +x /usr/local/node/exec.sh  
  
RUN npm install -g yarn  
  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/bin/sh","/usr/local/node/exec.sh"]

