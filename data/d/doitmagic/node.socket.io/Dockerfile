FROM phusion/baseimage:0.9.17  
  
MAINTAINER Doitmagic <razvan@doitmagic.com>  
  
RUN mkdir -p /var/script  
  
RUN apt-get update && apt-get install -y nodejs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install -y npm  
RUN /usr/bin/npm install express && /usr/bin/npm install socket.io &&
/usr/bin/npm install redis && /usr/bin/npm install ioredis && /usr/bin/npm
install redis-notifier && /usr/bin/npm install request  
  
VOLUME /var/script  
  
WORKDIR /var/script  
  
EXPOSE 3500/tcp  
  
CMD "/bin/sh" "-c" "node index.js"  

