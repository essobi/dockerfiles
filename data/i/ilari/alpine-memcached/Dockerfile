FROM alpine:3.3  
MAINTAINER ilari.makela@wunderkraut.com  
  
ENV MEMCACHED_MEMORY 128  
ENV MEMCACHED_MAX_CONNECTIONS 1024  
ENV MEMCACHED_MAX_ITEM_SIZE 4M  
  
COPY start.sh /start.sh  
  
# Update the package repository and install applications  
RUN apk --no-cache --update add memcached && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/* && \  
chmod 755 /start.sh  
  
# Expose port 11211  
EXPOSE 11211  
CMD ["/start.sh"]  
  
USER memcached

