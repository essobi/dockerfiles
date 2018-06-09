FROM linarotechnologies/alpine:edge  
  
RUN apk add --no-cache tinyproxy  
  
# Tinyproxy config file (use Debian location currently)  
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf  
  
EXPOSE 8080  
COPY start.sh start.sh  
RUN chmod +x start.sh  
ENTRYPOINT ["/start.sh"]  
  
# Default to dump service log  
CMD /usr/sbin/tinyproxy -d -c /etc/tinyproxy/tinyproxy.conf  

