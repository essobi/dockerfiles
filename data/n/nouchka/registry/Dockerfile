FROM registry:2  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
RUN apk add --update apache2-utils && \  
apk add --update openssl && \  
rm -rf /var/cache/apk/*  
  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
ENV REGISTRY_PASSWORD registry-password  
  
VOLUME ["/certs", "/var/lib/registry"]  
  
ENTRYPOINT ["/start.sh"]  

