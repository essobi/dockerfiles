FROM alpine:3.4  
MAINTAINER Lochnair <lochnair@care.army>  
LABEL Description="Docker image for Squid based on the offical Alpine Linux
image (3.4)"  
  
# Install Squid  
RUN apk add \  
\--no-cache \  
\--update \  
squid  
  
# Enable caching by default  
RUN sed -i 's|#cache_dir ufs /var/cache/squid 100 16 256|cache_dir aufs
/var/cache/squid 100 16 256|' /etc/squid/squid.conf  
  
# Disable access to Squid from localhost  
RUN sed -i 's|#http_access deny to_localhost|http_access deny to_localhost|'
/etc/squid/squid.conf  
  
# Expose port  
EXPOSE 3128  
# Create swap directories  
RUN /usr/sbin/squid -Nz -f /etc/squid/squid.conf  
  
# Define volumes  
VOLUME /etc/squid  
VOLUME /var/cache/squid  
VOLUME /var/log/squid  
  
ENTRYPOINT ["/usr/sbin/squid", "-N", "-Y", "-C", "-d", "1", "-f",
"/etc/squid/squid.conf"]  

