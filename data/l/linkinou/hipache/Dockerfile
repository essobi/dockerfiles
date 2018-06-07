FROM ubuntu:14.04  
MAINTAINER cedric.merouani@gmail.com  
  
RUN apt-get -y update  
  
RUN apt-get -y install nodejs npm  
  
RUN npm install -g eventemitter3@0.1.6 hipache@0.3.1 --production  
  
# Expose Hipache  
EXPOSE 80  
ENV SERVER_ACCESSLOG /var/log/hipache-access.log  
ENV SERVER_WORKERS 10  
ENV SERVER_MAXSOCKETS 100  
ENV SERVER_DEADBACKENDTTL 30  
ENV SERVER_TCPTIMEOUT 30  
ENV SERVER_RETRYONERROR 3  
ENV SERVER_DEADBACKENDON500 false  
ENV SERVER_HTTPKEEPALIVE false  
ENV SERVER_LRUCACHE_SIZE 5  
ENV SERVER_LRUCACHE_TTL 5  
ENV SERVER_HTTP_PORT 80  
ENV SERVER_HTTP_BIND 0.0.0.0  
ENV SERVER_HTTPS_PORT 43  
ENV SERVER_HTTPS_BIND 0.0.0.0  
ENV SERVER_USER www-data  
ENV SERVER_GROUP www-data  
ENV SERVER_DEBUG false  
ENV SERVER_HTTPS_KEY /etc/ssl/ssl.key  
ENV SERVER_HTTPS_CERT /etc/ssl/ssl.crt  
ENV SERVER_SSL_PASSPHRASE null  
ENV DRIVER redis:  
  
ADD . /  
RUN chmod +x /*.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

