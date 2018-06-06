FROM agaveapi/php-api-base:alpine  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>  
  
ENV DOCUMENT_ROOT /var/www/code/public  
  
ADD code /var/www/code  
  
WORKDIR /var/www/code  
  
RUN sed -i 's/^#LoadModule deflate_module/LoadModule deflate_module/g'
/etc/apache2/httpd.conf && \  
sed -i 's/^#LoadModule expires_module/LoadModule expires_module/g'
/etc/apache2/httpd.conf && \  
sed -i 's#opcache.enable_cli=1#opcache.enable_cli=0#g'
/etc/php/conf.d/opcache-recommended.ini  
  
RUN composer install && \  
ls -al  
  
RUN ls -al  
  
RUN chown -R apache:apache .  

