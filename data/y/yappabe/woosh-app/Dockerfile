FROM debian:jessie  
  
MAINTAINER Joeri Verdeyen <joeriv@yappa.be>  
  
RUN mkdir -p /var/www/app/tmp/cache/acl && \  
mkdir -p /var/www/app/tmp/cache/models && \  
mkdir -p /var/www/app/tmp/cache/persistent && \  
mkdir -p /var/www/app/tmp/cache/upload && \  
mkdir -p /var/www/app/tmp/cache/views && \  
mkdir -p /var/www/app/tmp/logs && \  
mkdir -p /var/www/app/tmp/sessions && \  
mkdir -p /var/www/app/tmp/processing && \  
mkdir -p /var/www/app/tmp/unsent_mails && \  
mkdir -p /var/www/app/html/cjs && \  
mkdir -p /var/www/app/html/ccss && \  
chmod -R 777 /var/www/app/html/cjs && \  
chmod -R 777 /var/www/app/html/ccss && \  
chmod -R 777 /var/www/app/tmp/ && \  
chmod -R 777 /var/www/app/vendor/meenie/munee/cache/ || true  
  
VOLUME ["/var/www", "/var/www/app/tmp/"]  

