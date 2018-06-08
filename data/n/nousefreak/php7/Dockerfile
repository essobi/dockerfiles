FROM ubuntu-upstart:14.04  
  
MAINTAINER Dries De Peuter <dries@nousefreak.be>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C \  
&& echo "deb http://ppa.launchpad.net/nginx/development/ubuntu trusty main" >
/etc/apt/sources.list.d/nginx-development.list  
  
RUN apt-get update \  
&& apt-get install -y \  
aufs-tools \  
automake \  
bison \  
btrfs-tools \  
build-essential \  
curl \  
git \  
libbz2-dev \  
libcurl4-openssl-dev \  
libmcrypt-dev \  
libxml2-dev \  
re2c \  
libpq-dev \  
libpng-dev \  
zlib1g-dev \  
libpcre3-dev \  
libjpeg-dev \  
libreadline-dev \  
nginx \  
&& apt-get clean  
  
# get the latest PHP source from master branch  
RUN git clone --depth=1 https://github.com/php/php-src.git /usr/local/src/php  
  
# # we re going to be working out of the PHP src directory for the compile
steps  
WORKDIR /usr/local/src/php  
ENV PHP_DIR /usr/local/php  
  
# # configure the build  
RUN ./buildconf \  
&& ./configure \  
--enable-fpm \  
--enable-ftp \  
--enable-zip \  
--enable-sockets \  
--enable-cli \  
--enable-opcache \  
# --enable-soap \  
--enable-sockets \  
--enable-sysvmsg \  
--enable-sysvsem \  
--enable-sysvshm \  
--enable-mbstring \  
--enable-mbregex \  
# --enable-shmop \  
# --enable-wddx \  
--enable-exif \  
--enable-fpm \  
--enable-ftp \  
--enable-gd-native-ttf \  
# --enable-dba  
--enable-calendar \  
--enable-bcmath \  
--with-gd \  
--with-pdo-mysql \  
--with-pdo-pgsql \  
--with-curl \  
--with-config-file-path=/etc \  
--with-config-file-scan-dir=/Library/Server/Web/Config/php \  
--with-libxml-dir=/usr \  
--with-openssl=/usr \  
--with-kerberos=/usr \  
--with-zlib=/usr \  
--with-bz2=/usr \  
--disable-cgi \  
--with-curl=/usr \  
# --with-ndbm=/usr  
--with-png-dir=no \  
--with-gd \  
--with-jpeg-dir \  
--with-icu-dir=/usr \  
--with-ldap=/usr \  
# --with-ldap-sasl=/usr \  
# --with-libedit \  
# --with-mysql=mysqlnd \  
# --with-mysqli=mysqlnd \  
# --with-readline \  
# --with-snmp=/usr \  
# --with-tidy \  
--with-xmlrpc \  
--with-iconv-dir=/usr \  
# --with-xsl=/usr \  
--with-pcre-regex=/usr \  
--prefix=$PHP_DIR --with-config-file-path=$PHP_DIR --with-config-file-scan-
dir=$PHP_DIR/conf.d --with-libdir=/lib/x86_64-linux-gnu \  
&& make && make install \  
&& cp php.ini-development /usr/local/php/php.ini \  
&& sed -i 's/;date.timezone =/date.timezone = Europe\/Brussels/'
/usr/local/php/php.ini \  
&& cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf
\  
&& cp sapi/fpm/php-fpm /usr/local/bin  
  
COPY conf/init.nginx.conf /etc/init/nginx.conf  
COPY conf/init.php-fpm.conf /etc/init/php-fpm.conf  
COPY conf/nginx.conf /etc/nginx/sites-enabled/default  
COPY conf/php.pool.conf /usr/local/php/etc/php-fpm.d/www.conf  
  
ENV PATH $PATH:/usr/local/php/bin  
  
WORKDIR /var/www/html  
  
EXPOSE 80  

