FROM centos:7.2.1511  
  
MAINTAINER "Chen Lin" <chenlin@seekasia.com>  
  
WORKDIR /tmp  
# Install all required package; Use --nogpgcheck to avoid nokey warning  
RUN \  
yum update -y && \  
yum install -y \--nogpgcheck deltarpm-3.6-3.el7.x86_64 && \  
yum install -y \--nogpgcheck epel-release && \  
yum install -y \--nogpgcheck nginx && \  
yum install -y \--nogpgcheck wget.x86_64 && \  
yum install -y \--nogpgcheck tar.x86_64 && \  
yum install -y \--nogpgcheck gcc.x86_64 && \  
yum install -y \--nogpgcheck make.x86_64 && \  
yum install -y \--nogpgcheck libXpm-devel.x86_64 && \  
yum install -y \--nogpgcheck t1lib-devel.x86_64 && \  
yum install -y \--nogpgcheck gmp-devel.x86_64 && \  
yum install -y \--nogpgcheck libxml2-devel && \  
yum install -y \--nogpgcheck openssl-devel.x86_64 && \  
yum install -y \--nogpgcheck libcurl-devel.x86_64 && \  
yum install -y \--nogpgcheck libjpeg-turbo-devel.x86_64 && \  
yum install -y \--nogpgcheck libpng-devel.x86_64 && \  
yum install -y \--nogpgcheck freetype-devel.x86_64 && \  
yum install -y \--nogpgcheck libxslt-devel.x86_64 && \  
yum install -y \--nogpgcheck libmcrypt-devel.x86_64 && \  
yum install -y \--nogpgcheck ImageMagick-devel.x86_64 && \  
yum install -y \--nogpgcheck autoconf && \  
yum install -y \--nogpgcheck gcc-c++.x86_64 && \  
yum install -y \--nogpgcheck supervisor && \  
yum install -y \--nogpgcheck sendmail && \  
yum clean all && \  
`########## Install FreeTDS ##########` && \  
cd /tmp && \  
wget ftp://ftp.freetds.org/pub/freetds/stable/freetds-0.92.79.tar.gz && \  
tar -zxvf freetds-0.92.79.tar.gz && \  
cd freetds-0.92.79 && \  
./configure \--prefix=/usr/local/freetds-0.92.79 && \  
make && \  
make install && \  
ln -s /usr/local/freetds-0.92.79/lib /usr/local/freetds-0.92.79/lib64 && \  
`########## Install PHP ##########` && \  
cd /tmp && \  
wget http://my1.php.net/distributions/php-5.4.39.tar.gz && \  
tar -zxvf php-5.4.39.tar.gz && \  
cd php-5.4.39 && \  
./configure \--prefix=/usr/local/php-5.4.39 \--disable-debug \--enable-
sigchild \--enable-fpm \--enable-cgi \--enable-sockets \--enable-pcntl
\--enable-mbstring \--enable-calendar \--enable-gd-native-ttf \--enable-gd-
jis-conv \--with-zlib-dir=/usr \--with-png-dir=/usr \--with-jpeg-dir=/usr
\--with-freetype-dir=/usr \--with-xpm-dir=/usr
\--with-t1lib=/usr/local/t1lib-5.1.2 \--with-xsl=/usr \--with-gd \--with-
gettext \--with-iconv \--with-curl \--with-mhash \--with-mcrypt \--with-
mysql=mysqlnd \--with-mysqli=mysqlnd \--with-mssql=/usr/local/freetds-0.92.79
\--with-gmp \--with-pear \--with-openssl \--with-pdo-
dblib=/usr/local/freetds-0.92.79 \--with-pdo-mysql=mysqlnd \--enable-zip
\--with-libdir=lib64 \--enable-bcmath \--enable-soap && \  
make && \  
make install && \  
`########## Prepare PHP Extenstion Path ##########` \  
mkdir /usr/local/php-5.4.39/lib/php/extensions && \  
mkdir /usr/local/php-5.4.39/lib/php/extensions/no-debug-non-zts-20100525 && \  
`########## Clean Tmp Folder ##########` && \  
rm -rf /tmp/* /var/tmp/* && \  
`########## Add PHP to execution path ##########` && \  
ln -s /usr/local/php-5.4.39/bin/php /usr/bin/php  
# Apply PHP Configuration  
ADD config/php.ini /usr/local/php-5.4.39/lib/php.ini  
  
RUN \  
`########## Install Zend Opcache PHP Ext ##########` \  
cd /tmp && \  
wget http://pecl.php.net/get/zendopcache-7.0.4.tgz && \  
tar -zxvf zendopcache-7.0.4.tgz && \  
cd zendopcache-7.0.4 && \  
/usr/local/php-5.4.39/bin/phpize && \  
./configure \--with-php-config=/usr/local/php-5.4.39/bin/php-config && \  
make && \  
make install && \  
`########## Install Imagick PHP Ext ##########` \  
cd /tmp && \  
wget http://pecl.php.net/get/imagick-3.1.2.tgz && \  
tar -zxvf imagick-3.1.2.tgz && \  
cd imagick-3.1.2 && \  
/usr/local/php-5.4.39/bin/phpize && \  
./configure \--with-php-config=/usr/local/php-5.4.39/bin/php-config && \  
make && \  
make install && \  
`########## Install Lib Memcached required for PHP Memcached PHP Ext
##########` \  
cd /tmp && \  
wget
https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
&& \  
tar -zxvf libmemcached-1.0.18.tar.gz && \  
cd libmemcached-1.0.18 && \  
./configure && \  
make && \  
make install && \  
`########## Install Memcached PHP Ext ##########` \  
cd /tmp && \  
wget http://pecl.php.net/get/memcached-2.1.0.tgz && \  
tar -zxvf memcached-2.1.0.tgz && \  
cd memcached-2.1.0 && \  
/usr/local/php-5.4.39/bin/phpize && \  
./configure \--with-php-config=/usr/local/php-5.4.39/bin/php-config && \  
make && \  
make install && \  
`########## Clean Tmp Folder ##########` && \  
rm -rf /tmp/* /var/tmp/* && \  
`########## Create Parent Host Folder ##########` && \  
mkdir -p /data && \  
mkdir -p /data/www && \  
mkdir -p /data/log && \  
mkdir -p /data/log/nginx && \  
mkdir -p /data/log/php && \  
mkdir -p /data/log/supervisor && \  
mkdir -p /data/api-root && \  
mv /etc/localtime /etc/localtime.bak && \  
ln -s /usr/share/zoneinfo/Asia/Singapore /etc/localtime  
# Apply Configuration  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/freetds.conf /usr/local/freetds-0.92.79/etc/freetds.conf  
ADD config/php-fpm.conf /usr/local/php-5.4.39/etc/php-fpm.conf  
ADD config/supervisord.conf /etc/supervisord.conf  
# Data Volumes  
VOLUME ["/data"]  
  
# Nginx Ports  
EXPOSE 80  
EXPOSE 8008  
EXPOSE 9001  
  
# Start the supervisord and it will start PHP-FPM and Nginx  
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  
  
  
# FROM — Specify which image to use for the container.  
# RUN — Run a command on the container. Used for things like installing
packages, etc.  
# ADD - Copies new files, directories or remote file URLs from <src> and adds
them to the filesystem of the container at the path <dest>  
# EXPOSE — Open ports from the Docker container to the host.  
# CMD — The default command to run when the container is started. Can be
overridden from the command line at runtime.  
# ENTRYPOINT — Similar to the CMD option in that it will be the default
command that is run but this one cannot be overridden from the command line.  
# VOLUME instruction makes the directory available as a volume that other
containers can mount by using the --volumes-from  
# Note: Different with Old Live Env:  
# - newrelic  
# - curl: AsynchDNS setting  
# https://hub.docker.com/r/dylanlindgren/docker-nginx/~/dockerfile/  
# https://hub.docker.com/r/million12/nginx/~/dockerfile/  
# https://hub.docker.com/r/dylanlindgren/docker-laravel-nginx/~/dockerfile/  

