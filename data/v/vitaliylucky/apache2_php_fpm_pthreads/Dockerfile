FROM ubuntu:14.04.3  
  
MAINTAINER Vitaliy Lyubimov <lubimov.vitaliy.51400@gmail.com>  
  
CMD /home/start.sh && /bin/bash  
  
# Add multiverse repositories:  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu trusty-updates multiverse" >>
/etc/apt/sources.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu trusty-updates multiverse"
>> /etc/apt/sources.list  
  
######################################  
# Compile the php 5.6 #  
######################################  
  
# Required libraries  
  
RUN apt-get update \  
&& apt-get install -y gcc make libzzip-dev libreadline-dev libxml2-dev \  
libssl-dev libmcrypt-dev libcurl4-openssl-dev lib32bz2-dev wget tar gzip
php5-dev \  
nano  
  
  
# Install services & dependencies  
RUN apt-get install -y apache2-mpm-worker apache2-threaded-dev libapache2-mod-
fastcgi libxml2-dev  
  
# Download the PHP source  
RUN cd /usr/local/src \  
&& wget http://ua2.php.net/distributions/php-5.6.17.tar.gz \  
&& tar zxvf php-5.6.17.tar.gz \  
&& cd php-5.6.17 \  
&& ./configure --enable-debug --enable-maintainer-zts --enable-pthreads
--prefix=/usr --with-config-file-path=/etc --with-apxs2=/usr/bin/apxs2
--enable-fpm \  
\--with-pdo-pgsql --with-zlib-dir --with-freetype-dir --enable-mbstring
--with-libxml-dir=/usr --enable-soap --enable-calendar --with-curl --with-
mcrypt \  
\--with-zlib --with-pgsql --disable-rpath --enable-inline-optimization --with-
bz2 --with-zlib --enable-sockets --enable-sysvsem \  
\--enable-sysvshm --enable-pcntl --enable-mbregex --enable-exif --enable-
bcmath --with-mhash --enable-zip --with-pcre-regex --with-mysql --with-pdo-
mysql \  
\--with-mysqli --with-openssl \  
\--with-fpm-user=www-data --with-fpm-group=www-data --with-
libdir=/lib/x86_64-linux-gnu --enable-ftp \  
\--with-kerberos --with-gettext --with-xmlrpc --enable-opcache --enable-fpm  
  
  
# Compile PHP  
RUN echo "##################Compile PHP##################" \  
&& cd /usr/local/src/php-5.6.17 \  
&& make \  
&& make install  
  
# Install pthreads-2.0.10  
RUN cd /usr/local/src/php-5.6.17 \  
&& pecl install pthreads-2.0.10 \  
&& cp php.ini-development /etc/php.ini \  
&& echo "extension=pthreads.so" >> /etc/php.ini \  
&& echo "##################Check pthreads##################" \  
&& cp sapi/fpm/init.d.php-fpm /etc/init.d/php-fpm \  
&& chmod +x /etc/init.d/php-fpm  
  
RUN php -m | grep pthreads  
  
  
# Cleanup  
#RUN rm -r /var/lib/apt/lists/* \  
# /var/www/html/*  
  
  
# Prepare startup script  
ADD start.sh /home/start.sh  
RUN chmod +x /home/start.sh  
  
#Prepare web-server configuration  
  
ADD config/php5-fpm.conf /etc/apache2/conf-available/php5-fpm.conf  
ADD config/www.conf /usr/etc/php-fpm.conf  
  
RUN a2enconf php5-fpm  
  
RUN a2enmod fastcgi actions expires headers rewrite socache_shmcb ssl  
  
ADD config/index.php /var/www/html/index.php  
ADD config/pthreads.php /var/www/html/pthreads.php  
  
EXPOSE 80 443  

