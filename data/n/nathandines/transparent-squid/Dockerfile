FROM alpine:latest  
  
RUN apk --no-cache add \  
iptables \  
openssl \  
squid  
  
ADD squid.conf /etc/squid/squid.conf  
ADD entrypoint.sh /src/entrypoint.sh  
  
ENTRYPOINT ["/src/entrypoint.sh"]  
  
CMD ["/bin/sh"]  

