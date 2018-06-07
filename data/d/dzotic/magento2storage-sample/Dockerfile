FROM jelastic/storage  
MAINTAINER Jelastic  
WORKDIR /data  
ADD scripts/varnish-probe.php /data/  
COPY /dumps/ /data  
RUN rm -rf /data/var/*; \  
ls /data; \  
cd /data/ && find var vendor pub/static pub/media app/etc -type f -exec chmod
g+w {} \; && find var vendor pub/static pub/media app/etc -type d -exec chmod
g+w {} \; && chmod u+x bin/magento  
ADD scripts/env.php /data/app/etc/  

