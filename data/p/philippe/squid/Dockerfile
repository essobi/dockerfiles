FROM alpine:3.6  
RUN apk add --update squid=3.5.23-r2 && rm -rf /var/cache/apk/*  
  
RUN ln -sf /dev/stdout /var/log/squid/access.log  
RUN ln -sf /dev/stdout /var/log/squid/store.log  
RUN ln -sf /dev/stdout /var/log/squid/cache.log  
  
COPY squid.conf /etc/squid/squid.conf  
COPY run.sh /run.sh  
  
RUN chmod +x /run.sh  
  
EXPOSE 3128  
CMD ["/run.sh"]

