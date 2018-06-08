FROM outrigger/servicebase  
  
RUN yum -y update && yum -y install httpd  
RUN yum -y install \  
cronolog \  
centos-release-scl-rh  
  
EXPOSE 80  
RUN mkdir -p /var/lib/php/session  
  
COPY root /  
  
VOLUME ["/var/log/httpd", "/var/lib/php/session"]  
  
ENV PROXY_TIMEOUT 120  
ENV PHP_MAX_EXECUTION_TIME 60  
ENV PHP_MAX_CHILDREN 5  
ENV PHP_MEMORY_LIMIT 256m  
ENV PHP_OPCACHE_MEMORY 192  
ENV PHP_XDEBUG false  
ENV PHP_XHPROF false  
ENV PHP_TIMEZONE UTC  
ENV PHP_POST_MAX_SIZE 12M  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV DOCROOT /var/www/html  

