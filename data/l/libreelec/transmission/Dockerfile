FROM alpine:3.3  
MAINTAINER docker@libreelec.tv  
  
RUN apk add --update transmission-daemon && rm -rf /var/cache/apk/*  
  
VOLUME ["/downloads", "/incomplete", "/watch", "/config"]  
  
ADD ./settings.json /settings.json  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
EXPOSE 9091 45555  
CMD ["/start.sh"]  

