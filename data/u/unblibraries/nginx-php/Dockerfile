FROM unblibraries/nginx:alpine  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
LABEL ca.unb.lib.php="5"  
LABEL vcs-ref="alpine"  
LABEL vcs-url="https://github.com/unb-libraries/docker-nginx-php"  
  
ENV COMPOSER_PATH /usr/local/bin  
ENV PHP_FPM_ERROR_LOG /proc/self/fd/2  
ENV PHP_PID_DIR /var/run/php  
  
RUN apk --update add php5-fpm php5-json php5-zlib php5-xml php5-phar php5-gd
php5-iconv php5-mcrypt curl php5-curl php5-openssl && \  
rm -f /var/cache/apk/* && \  
ln -s /usr/bin/php5 /usr/bin/php && \  
mkdir -p ${PHP_PID_DIR}/ && \  
chown ${NGINX_RUN_USER}:${NGINX_RUN_GROUP} ${PHP_PID_DIR}/ && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=${COMPOSER_PATH} \--filename=composer  
  
COPY conf/nginx/app.conf /etc/nginx/conf.d/app.conf  
COPY conf/php/app-php.ini /etc/php5/conf.d/zz_app.ini  
COPY conf/php/app-fpm.conf /etc/php5/fpm.d/zz_app.conf  
  
COPY scripts /scripts  
RUN chmod -R 755 /scripts  

