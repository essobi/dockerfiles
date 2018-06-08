FROM alpine:3.7  
LABEL maintainer="Michael H. Oshita <ijinpublic+github@gmail.com>"  
  
RUN apk --update add squid  
  
# Redirect logs to stdout for the container  
RUN ln -sf /dev/stdout /var/log/squid/access.log && \  
ln -sf /dev/stdout /var/log/squid/store.log && \  
ln -sf /dev/stdout /var/log/squid/cache.log  
  
COPY squid.conf /etc/squid/squid.conf  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 3128  
CMD ["/run.sh"]  

