FROM lsiobase/alpine:3.6  
MAINTAINER Brice Mancone  
  
# global environment settings  
ENV \  
ELFINDER_DOWNLOAD="https://github.com/Studio-42/elFinder/archive/2.1.26.zip" \  
ELFINDER_USER=abc  
  
# install packages  
RUN \  
apk add --no-cache \  
nginx \  
php7 \  
php7-fpm \  
php7-json \  
php7-mbstring \  
php7-curl \  
php7-gd \  
php7-intl \  
php7-session \  
unzip \  
curl  
  
  
# install elfinder  
RUN \  
rm -rf /var/www && \  
curl -L -O "${ELFINDER_DOWNLOAD}" && \  
unzip *.zip && \  
rm -f *.zip && \  
mv elFinder-* /var/www && \  
chown -R "${ELFINDER_USER}":"${ELFINDER_USER}" /var/www && \  
mv /var/www/php/connector.minimal.php-dist /var/www/php/connector.minimal.php
&& \  
rm -rf /var/www/files && \  
ln -s /data /var/www/files  
  
# cleanup  
RUN rm -rf etc/nginx/conf.d/default.conf  
  
# copy local files  
COPY root /  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
VOLUME /data

