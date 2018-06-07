FROM alpine  
  
RUN apk add --update git openssh && rm -rf /var/cache/apk/*  
  
VOLUME /var/repo  
VOLUME /var/config  
  
WORKDIR /var/repo  
  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

