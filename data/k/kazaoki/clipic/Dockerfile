FROM alpine  
MAINTAINER kazaoki lab.  
  
# Add PHP & etc  
# -------------  
RUN apk --update add php-gd openssl && \  
rm -rf /var/cache/apk/*  
  
# Added shell files  
# -----------------  
ADD clipic.php /opt/clipic.php  
CMD ["/usr/bin/php", "/opt/clipic.php"]  

