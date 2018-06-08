FROM php:7.1-fpm  
  
MAINTAINER Luca Orlandi <luca.orlandi@gmail.com>  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get upgrade -y && apt-get install -y libpng-dev
libjpeg-dev libmcrypt-dev libcurl4-openssl-dev libicu-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd opcache intl pdo_mysql mcrypt bcmath  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.remote_connect_back=on" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_host=127.17.0.1" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& cp /usr/local/etc/php/conf.d/xdebug.ini /usr/local/etc/php-fpm.d/  
  
RUN apt-get update && apt-get install -y msmtp  
ADD msmtprc /etc/.msmtp_php  
RUN chown www-data. /etc/.msmtp_php && chmod 600 /etc/.msmtp_php  
  
# magento2 requirements  
RUN apt-get install -y libxslt1.1 libxslt1-dev  
RUN docker-php-ext-install xsl soap zip  
  
#ADD magento.ini /usr/local/etc/php-fpm.d/magento.conf  
ADD magento.ini /usr/local/etc/php/conf.d/  
ADD magento.pool.conf /usr/local/etc/php-fpm.d/www.conf  
#ADD 20-xdebug.ini /usr/local/etc/php-fpm.d/20-xdebug.conf  
#ADD 20-xdebug.ini /usr/local/etc/php/conf.d/  
RUN usermod -u 1000 www-data  
  
RUN apt-get install -y cron  
RUN apt-get autoremove -y && apt-get autoclean -y  
ADD crontab /var/spool/cron/crontabs/www-data  
RUN chmod 0644 /var/spool/cron/crontabs/www-data  
  
# Install composer (see
https://github.com/composer/docker/blob/8a2a40c3376bac96f8e3db2f129062173bff7734/1.6/Dockerfile)  
RUN docker-php-ext-install zip  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.6.2  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/b107d959a5924af895807021fcef4ffec5a76aa9/web/installer
\  
&& php -r " \  
\$signature =
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& composer --ansi --version --no-interaction \  
&& rm -rf /tmp/* /tmp/.htaccess  
  
RUN apt-get install git -y  
  
RUN mkdir /var/www/html/var /var/www/html/media && chown -Rf www-data.
/var/www/html/var /var/www/html/media  
VOLUME /var/www/html  
  
COPY startup.sh /  
  
CMD ["/startup.sh"]  
  
EXPOSE 9000  

