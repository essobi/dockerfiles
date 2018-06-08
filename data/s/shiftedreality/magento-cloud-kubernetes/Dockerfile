FROM richarvey/nginx-php-fpm:1.3.10  
ENV GIT_REPO https://github.com/magento/magento-cloud.git  
ENV GIT_BRANCH master  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV MAGENTO_ROOT /var/www/html  
ENV PHP_MEM_LIMIT 2048  
VOLUME /root/.composer/cache  
  
RUN docker-php-ext-install bcmath  
  
RUN apk update && \  
apk upgrade && \  
apk add coreutils && \  
apk add findutils && \  
apk add gzip  
  
ADD scripts/start.sh /start.sh  
ADD bin/* /usr/local/bin/  
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf  
  
RUN ["chmod", "+x", "/usr/local/bin/magento-installer"]  
RUN ["chmod", "+x", "/usr/local/bin/magento-command"]  
RUN ["chmod", "+x", "/usr/local/bin/ece-command"]  
  
CMD ["/start.sh"]  

