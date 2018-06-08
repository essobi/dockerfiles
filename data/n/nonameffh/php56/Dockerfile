FROM nonameffh/centos:latest  
  
MAINTAINER Aleksey Tarasov <dark.ffh@gmail.com>  
  
# update packages  
RUN yum -y update \  
# install php  
&& yum -y install \  
php56u \  
php56u-cli \  
php56u-common \  
php56u-bcmath \  
php56u-gd \  
php56u-mbstring \  
php56u-mcrypt \  
php56u-opcache \  
php56u-dba \  
php56u-fpm \  
php56u-imap \  
php56u-intl \  
php56u-mysqlnd \  
php56u-pdo \  
php56u-opcache \  
php56u-pecl-amqp \  
php56u-pecl-memcached \  
php56u-pecl-redis \  
php56u-pecl-json \  
php56u-pecl-imagick \  
php56u-pgsql \  
php56u-soap \  
php56u-xml \  
php56u-dbg php56u-pecl-xdebug \  
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

