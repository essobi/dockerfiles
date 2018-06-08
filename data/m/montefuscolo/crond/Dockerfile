FROM alpine:latest  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@gmail.com>  
  
RUN apk update && \  
apk add dcron && \  
rm -rf /var/cache/apk/*  
  
VOLUME /etc/periodic  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD [ "crond", "-d", "-l5" ]  
  

