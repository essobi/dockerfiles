FROM shenron/nginx:1.12.2  
MAINTAINER Thomas CASTELLY <thomas@tcy.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y apt-transport-https lsb-release ca-
certificates wget &&\  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
RUN apt-get update && apt-get install -y \  
# For memcached  
pkg-config \  
php5.6-dev \  
php5.6-fpm \  
php5.6-xml \  
unzip \  
libaio-dev \  
libmemcached-dev \  
libzip-dev \  
unzip \  
wget  
  
# Copy link config between PHP and Nginx  
COPY /conf/nginx/ /etc/nginx/conf.d/  
  
# Copy base PHP config  
COPY /conf/php/ /etc/php/5.6/fpm/  
  
# Copy link config between PHP and Nginx  
COPY /conf/nginx/ /etc/nginx/conf.d/  
  
# install oracle client  
COPY /conf/oracle/ /tmp/  
  
ENV LD_LIBRARY_PATH="/usr/local/instantclient_12_1"  
RUN unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/ &&
\  
unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/ && \  
unzip /tmp/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip -d /usr/local/ && \  
ln -s /usr/local/instantclient_12_1 /usr/local/instantclient && \  
ln -s /usr/local/instantclient/libclntsh.so.12.1
/usr/local/instantclient/libclntsh.so && \  
ln -s /usr/local/instantclient/sqlplus /usr/bin/sqlplus && \  
rm /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip /tmp/instantclient-sdk-
linux.x64-12.1.0.2.0.zip /tmp/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip
&&\  
echo 'instantclient,/usr/local/instantclient' | pecl install oci8-1.4.10 && \  
echo "extension=oci8.so" >> /etc/php/5.6/fpm/php.ini  
  
# Install other extensions  
RUN pecl install\  
xdebug\  
memcached-2.2.0 \  
zip  
  
# Install PHPUnit  
RUN wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
COPY /conf/entrypoint.sh /  
COPY /conf/entrypoint-nginx-conf.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR /var/www  
  
# Nginx: 80, 440  
# PHP: 900  
EXPOSE 80 443 900  

