FROM alpine:3.2  
RUN apk add --update squid  
  
RUN ln -sf /dev/stdout /var/log/squid/access.log  
RUN ln -sf /dev/stdout /var/log/squid/store.log  
RUN ln -sf /dev/stdout /var/log/squid/cache.log  
  
COPY squid.conf /etc/squid/squid.conf  
COPY run.sh /run.sh  
  
EXPOSE 3128  
CMD ["/run.sh"]  

