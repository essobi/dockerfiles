FROM xenolf/lego  
MAINTAINER Stephane Albert "sheeprine@nullplace.com"  
ENV DAYS 15  
ENV NOTIF_MAIL changeme  
ENV HTTP_PORT 1080  
ENV TLS_PORT 1443  
RUN apk add --no-cache openssl && rm -rf /var/cache/apk/*  
  
ADD entrypoint.sh /  
  
VOLUME /data  
  
ENTRYPOINT ["/entrypoint.sh"]  

