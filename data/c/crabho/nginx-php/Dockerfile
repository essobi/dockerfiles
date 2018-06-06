FROM centos:7  
MAINTAINER Skiychan <dev@skiy.net>  
##  
# Nginx: 1.9.11  
# PHP : 7.0.3  
##  
#Install system library  
#RUN yum update -y  
ENV PHP_VERSION 7.0.3  
ENV NGINX_VERSION 1.9.11  
RUN yum install -y gcc \  
gcc-c++ \  
autoconf \  
automake \  
libtool \  
make \  
cmake && \  
yum clean all  
  
#Install PHP library  
## libmcrypt-devel DIY  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
yum install -y wget \  
zlib \  
zlib-devel \  
openssl \  
openssl-devel \  
pcre-devel \  
libxml2 \  
libxml2-devel \  
libcurl \  
libcurl-devel \  
libpng-devel \  
libjpeg-devel \  
freetype-devel \  
libmcrypt-devel \  
openssh-server \  
python-setuptools && \  
yum clean all  
  
#Add user  
RUN groupadd -r www && \  
useradd -M -s /sbin/nologin -r -g www www  
  
#Download nginx & php  
RUN mkdir -p /home/nginx-php && cd $_ && \  
wget -c -O nginx.tar.gz http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz
&& \  
wget -O php.tar.gz http://php.net/distributions/php-$PHP_VERSION.tar.gz && \  
curl -O -SL https://github.com/xdebug/xdebug/archive/XDEBUG_2_4_0RC3.tar.gz  
  
#Make install nginx  
RUN cd /home/nginx-php && \  
tar -zxvf nginx.tar.gz && \  
cd nginx-$NGINX_VERSION && \  
./configure --prefix=/usr/local/nginx \  
\--user=www --group=www \  
\--error-log-path=/var/log/nginx_error.log \  
\--http-log-path=/var/log/nginx_access.log \  
\--pid-path=/var/run/nginx.pid \  
\--with-pcre \  
\--with-http_ssl_module \  
\--without-mail_pop3_module \  
\--without-mail_imap_module \  
\--with-http_gzip_static_module && \  
make && make install  
  
#Make install php  
RUN cd /home/nginx-php && \  
tar zvxf php.tar.gz && \  
cd php-$PHP_VERSION && \  
./configure --prefix=/usr/local/php \  
\--with-config-file-path=/usr/local/php/etc \  
\--with-config-file-scan-dir=/usr/local/php/etc/php.d \  
\--with-fpm-user=www \  
\--with-fpm-group=www \  
\--with-mcrypt=/usr/include \  
\--with-mysqli \  
\--with-pdo-mysql \  
\--with-openssl \  
\--with-gd \  
\--with-iconv \  
\--with-zlib \  
\--with-gettext \  
\--with-curl \  
\--with-png-dir \  
\--with-jpeg-dir \  
\--with-freetype-dir \  
\--with-xmlrpc \  
\--with-mhash \  
\--enable-fpm \  
\--enable-xml \  
\--enable-shmop \  
\--enable-sysvsem \  
\--enable-inline-optimization \  
\--enable-mbregex \  
\--enable-mbstring \  
\--enable-ftp \  
\--enable-gd-native-ttf \  
\--enable-mysqlnd \  
\--enable-pcntl \  
\--enable-sockets \  
\--enable-zip \  
\--enable-soap \  
\--enable-session \  
\--enable-opcache \  
\--enable-bcmath \  
\--enable-exif \  
\--enable-fileinfo \  
\--disable-rpath \  
\--enable-ipv6 \  
\--disable-debug \  
\--without-pear && \  
make && make install  
  
#Add xdebug extension  
RUN cd /home/nginx-php && \  
tar -zxvf XDEBUG_2_4_0RC3.tar.gz && \  
cd xdebug-XDEBUG_2_4_0RC3 && \  
/usr/local/php/bin/phpize && \  
./configure --enable-xdebug --with-php-config=/usr/local/php/bin/php-config &&
\  
make && \  
cp modules/xdebug.so /usr/local/php/lib/php/extensions/xdebug.so  
  
RUN cd /home/nginx-php/php-$PHP_VERSION && \  
cp php.ini-production /usr/local/php/etc/php.ini && \  
cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf &&
\  
cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-
fpm.d/www.conf  
  
#Install supervisor  
RUN easy_install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /var/run/sshd && \  
mkdir -p /var/run/supervisord  
  
#Add supervisord conf  
ADD config/supervisord.conf /etc/supervisord.conf  
  
#Remove zips  
RUN cd / && rm -rf /home/nginx-php  
  
ADD config/index.php /data/www/index.php  
  
ADD config/xdebug.ini /usr/local/php/etc/php.d/xdebug.ini  
  
#Update nginx config  
ADD config/nginx.conf /usr/local/nginx/conf/nginx.conf  
  
#Start  
ADD config/start.sh /start.sh  
RUN chmod +x /start.sh  
  
#Set port  
EXPOSE 80 443 9000  
#Start it  
ENTRYPOINT ["/start.sh"]  
  
#Install package  
COPY ./package/* /tmp/  
  
#libmemcached  
#http://libmemcached.org/libMemcached.html  
RUN cd /tmp && \  
tar -zxvf libmemcached-1.0.18.tar.gz && \  
cd libmemcached-1.0.18 && \  
./configure --disable-sasl && \  
make && \  
make install && \  
rm /tmp/libmemcached-1.0.18.tar.gz && \  
rm -rf /tmp/libmemcached-1.0.18  
  
#php memcached  
#https://github.com/php-memcached-dev/php-memcached  
RUN cd /tmp && \  
tar -zxvf php-memcached-2.2.0-php7.tar.gz && \  
cd php-memcached-2.2.0-php7 && \  
/usr/local/php/bin/phpize && \  
./configure --disable-memcached-sasl --with-php-config=/usr/local/php/bin/php-
config && \  
make && \  
make install && \  
rm /tmp/php-memcached-2.2.0-php7.tar.gz && \  
rm -rf /tmp/php-memcached-2.2.0-php7  
  
#rabiitmq-c  
#https://github.com/alanxz/rabbitmq-c  
RUN cd /tmp && \  
tar -zxvf rabbitmq-c-0.7.1.tar.gz && \  
cd rabbitmq-c-0.7.1 && \  
./configure && \  
make && \  
make install && \  
rm /tmp/rabbitmq-c-0.7.1.tar.gz && \  
rm -rf /tmp/rabbitmq-c-0.7.1  
  
#php amqp  
#https://github.com/pdezwart/php-amqp  
RUN cd /tmp && \  
tar -zxvf php-amqp-php7.tar.gz && \  
cd php-amqp-php7 && \  
/usr/local/php/bin/phpize && \  
./configure --with-php-config=/usr/local/php/bin/php-config && \  
make && \  
make install && \  
rm /tmp/php-amqp-php7.tar.gz && \  
rm -rf /tmp/php-amqp-php7  
  
#config  
COPY ./config/php.ini /usr/local/php/etc/  
RUN echo extension=amqp.so > /usr/local/php/etc/php.d/amqp.ini && \  
echo extension=memcached.so > /usr/local/php/etc/php.d/memcached.ini  

