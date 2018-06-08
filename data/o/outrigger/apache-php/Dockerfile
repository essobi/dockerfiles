FROM outrigger/apache-php-base  
  
RUN yum -y install \  
https://www.softwarecollections.org/en/scls/remi/php56more/epel-7-x86_64/download/remi-
php56more-epel-7-x86_64.noarch.rpm && \  
yum -y install \  
gcc-c++ \  
make \  
rh-php56 \  
rh-php56-php-devel \  
rh-php56-php-gd \  
rh-php56-php-xml \  
rh-php56-php-pdo \  
rh-php56-php-mysql \  
rh-php56-php-mbstring \  
rh-php56-php-fpm \  
rh-php56-php-opcache \  
rh-php56-php-pecl-memcache \  
rh-php56-php-pecl-xdebug \  
rh-php56-php-pecl-zip \  
# The packages below are from php56more.  
more-php56-php-mcrypt \  
more-php56-php-pecl-xhprof \  
more-php56-php-pecl-yaml && \  
yum clean all  
  
  
ENV PHP_HOME /opt/rh/rh-php56  
RUN ln -sfv ${PHP_HOME}/root/usr/bin/* /usr/bin/ && \  
ln -sfv ${PHP_HOME}/root/usr/sbin/* /usr/sbin/ && \  
ln -svf /dev/stderr /var${PHP_HOME}/log/php-fpm/error.log  
  
# Install phpredis  
ENV PHPREDIS_VERSION 3.1.2  
RUN curl -L -o /tmp/phpredis.tar.gz
"https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz" && \  
tar -xzf /tmp/phpredis.tar.gz -C /tmp && \  
rm /tmp/phpredis.tar.gz && \  
cd "/tmp/phpredis-$PHPREDIS_VERSION" && \  
phpize && \  
./configure && \  
make && \  
make install && \  
# Clean up build dependencies.  
yum -y remove gcc-c++ make rh-php56-php-devel && \  
yum clean all  
  
COPY root /  

