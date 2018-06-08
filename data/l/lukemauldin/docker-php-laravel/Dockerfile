FROM php:5.4.45-apache  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#Create and expose webiste directory  
RUN mkdir -p /var/www/html/public  
VOLUME ["/var/www/html"]  
  
# Setup Apache and PHP  
RUN apt-get -o 'Acquire::CompressionTypes::Order::="gz"' update && \  
apt-get install -y --no-install-recommends \  
libmcrypt-dev \  
libbz2-dev \  
libfreetype6-dev \  
libpng12-dev && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/lib/x86_64-linux-gnu && \  
docker-php-ext-install mcrypt bz2 gd mbstring zip pdo_mysql mysql mysqli pcntl
bcmath && \  
apt-get purge --auto-remove -y libmcrypt-dev libbz2-dev libpng12-dev
libfreetype6-dev && \  
apt-get install -y --no-install-recommends libmcrypt4 libbz2-1.0 libpng12-0
libfreetype6 && \  
a2enmod rewrite && \  
a2enmod expires  
  
# Copy config files  
COPY config/apache.conf /etc/apache2/apache2.conf  
COPY config/php.ini /usr/local/etc/php/php.ini  
  
# Configure opcache  
RUN apt-get install --no-install-recommends unzip && \  
curl -L -o /root/opcache.zip -L
https://github.com/zendtech/ZendOptimizerPlus/archive/v7.0.5.zip && \  
cd /root && \  
unzip opcache.zip && \  
cd /root/ZendOptimizerPlus-7.0.5 && \  
/usr/local/bin/phpize && \  
./configure --with-php-config=/usr/local/bin/php-config && \  
make && \  
make install && \  
cd /root && \  
rm -fr /root/ZendOptimizerPlus-7.0.5 && \  
rm -fr /root/opcache.zip  
  
# Configure xdebug  
RUN curl -L -o /root/xdebug.tgz https://pecl.php.net/get/xdebug-2.3.2.tgz && \  
cd /root && \  
tar -zxvf xdebug.tgz && \  
cd /root/xdebug-2.3.2 && \  
/usr/local/bin/phpize && \  
./configure --enable-xdebug --with-php-config=/usr/local/bin/php-config && \  
make && \  
make install && \  
cd /root && \  
rm -fr /root/xdebug-2.3.2 && \  
rm -fr /root/xdebug.tgz  
  

