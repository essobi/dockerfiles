FROM alpine:latest  
  
MAINTAINER thuan@nguyens.xyz  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.12.0-alpha3/confd-0.12.0-alpha3-linux-
amd64 /usr/bin/confd  
  
RUN chmod +x /usr/bin/confd  
  
ADD ./confd /etc/confd  
ADD entrypoint.sh /entrypoint.sh  
  
RUN apk add --update aria2 && rm -rf /var/cache/apk/* && mkdir /etc/aria2/ &&
chmod a+rwx /etc/aria2/  
  
EXPOSE 6800  
ENTRYPOINT /entrypoint.sh  
  

