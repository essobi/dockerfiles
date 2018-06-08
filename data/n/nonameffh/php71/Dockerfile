FROM nonameffh/centos:latest  
  
MAINTAINER Aleksey Tarasov <dark.ffh@gmail.com>  
  
# update packages  
RUN yum -y update \  
# install php  
&& yum -y install \  
php71u-cli \  
php71u-common \  
php71u-bcmath \  
php71u-gd \  
php71u-mbstring \  
php71u-mcrypt \  
php71u-json \  
php71u-opcache \  
php71u-dba \  
php71u-fpm \  
php71u-imap \  
php71u-intl \  
php71u-mysqlnd \  
php71u-pdo \  
php71u-opcache \  
php71u-pecl-amqp \  
php71u-pecl-memcached \  
php71u-pecl-redis \  
php71u-pecl-imagick \  
php71u-pgsql \  
php71u-soap \  
php71u-xml \  
php71u-dbg \  
php71u-pecl-xdebug \  
# install git  
&& yum -y install git \  
&& yum -y clean all  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/ \  
&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
# Set user and group ID and own www root  
RUN usermod -u 1000 php-fpm && groupmod -g 1000 php-fpm && chown -R php-
fpm:php-fpm /var/www/html  
  
COPY fpm/php-fpm.conf /etc/php-fpm.conf  
COPY fpm/www.conf /etc/php-fpm.d/www.conf  
  
COPY entrypoint.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
# Expose ports  
EXPOSE 9000  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["php-fpm"]  

