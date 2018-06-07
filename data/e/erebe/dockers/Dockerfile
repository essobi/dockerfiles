FROM alpine:latest  
MAINTAINER github@erebe.eu  
  
ADD postfix-wrapper.sh /usr/bin/postfix-wrapper.sh  
RUN apk update && \  
apk add ca-certificates postfix procmail curl && \  
rm -rf /var/cache/apk/* && \  
adduser -D erebe && \  
mkdir /home/erebe/procmail && \  
mkdir /data && \  
chmod 777 -R /data  
  
VOLUME /data  
  
CMD ["/usr/bin/postfix-wrapper.sh"]  
  

