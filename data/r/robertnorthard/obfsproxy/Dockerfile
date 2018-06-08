FROM python:2.7.12-alpine  
  
MAINTAINER Robert Northard <robertnothard@googlemail.com>  
  
RUN apk add --update alpine-sdk && \  
rm -rf /var/cache/apk* && \  
pip install obfsproxy  
  
ENV LOG_MIN_SEVERITY info  
ENV DESTINATION_ADDRESS 192.168.99.100  
ENV DESTINATION_PORT 8081  
ENV LISTEN_ADDRESS 0.0.0.0  
ENV LISTEN_PORT 8080  
ADD /resources/scripts/* /data/  
RUN chmod +x /data/*  
  
EXPOSE 8080  
ENTRYPOINT ["/data/obfsproxy.sh"]  

