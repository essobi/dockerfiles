FROM php:7.0-fpm  
  
RUN apt-get update \  
&& apt-get install -y \  
# Base dependencies  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
git \  
vim \  
wget \  
lynx \  
psmisc \  
cron \  
&& apt-get clean  
  
  
RUN mkdir -p /var/spool/cron/crontabs/ \  
&& touch /var/spool/cron/crontabs/root  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/; \  
docker-php-ext-install \  
gd \  
intl \  
mcrypt \  
mbstring \  
pdo_mysql \  
xsl \  
zip \  
soap \  
opcache  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=256M'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=0'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
echo 'opcache.enable=1'; \  
echo 'opcache.save_comments=1'; \  
echo 'opcache.revalidate_path=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
ADD php.ini /usr/local/etc/php/conf.d/magento2.ini  
  
##  
# Install composer  
# source: https://getcomposer.org/download/  
##  
##  
RUN curl -L https://getcomposer.org/installer -o composer-setup.php && \  
php composer-setup.php && \  
rm composer-setup.php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +rx /usr/local/bin/composer && \  
# Remove cache and tmp files  
rm -rf /var/cache/apk/*  
  
  
# Defaults  
ENV MYSQL_USER magento2  
ENV MYSQL_DATABASE magento2  
ENV MYSQL_PASSWORD password  
ENV DB_HOST db  
ENV TIMEZONE UTC  
ENV CURRENCY USD  
ENV LANGUAGE en_US  
ENV USE_SECURE 0  
ENV USE_SECURE_ADMIN 0  
ENV DEPLOY_MODE production  
ENV MAGENTO_VERSION 2.2.0  
ENV BASE_URL http://127.0.0.1  
ENV BACKEND_FRONTNAME admin  
ENV USE_REWRITES 0  
ENV FILE_SYSTEM_OWNER root  
  
WORKDIR /var/www/html  
  
# http://devdocs.magento.com/guides/v2.0/install-gde/install/cli/install-cli-
backup.html  
RUN ulimit -s 65536  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
#COPY .aws/ /root/.aws  
# Setup goofys (s3 mount) https://github.com/kahing/goofys  
# RUN wget -P /usr/local/bin
https://github.com/kahing/goofys/releases/download/v0.0.17/goofys  
# RUN chmod u+x /usr/local/bin/goofys  
# RUN echo "goofys#s3://afrozania/pub/media /mnt/var/www/html/pub/media fuse
_netdev,allow_other,--file-mode=0666 0 0" > /etc/fstab  
VOLUME /var/www/html  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["php-fpm"]  

