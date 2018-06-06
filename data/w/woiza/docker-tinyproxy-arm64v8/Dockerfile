FROM resin/aarch64-alpine:latest  
  
RUN [ "cross-build-start" ]  
  
RUN set -xe && \  
apk add --no-cache tinyproxy  
  
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf  
  
COPY start.sh start.sh  
  
RUN chmod +x start.sh  
  
RUN [ "cross-build-end" ]  
  
ENTRYPOINT ["/start.sh"]  
  
# Default to dump service log  
CMD /usr/sbin/tinyproxy -d -c /etc/tinyproxy/tinyproxy.conf  
  

