FROM php:5.6-fpm  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update && apt upgrade -y && apt install -y ssmtp git zlib1g-dev
libmemcached-dev libmcrypt-dev libldap2-dev freetds-dev libjpeg-dev libpng-dev
libfreetype6-dev libcurl4-gnutls-dev libxml2-dev libicu-dev libgmp3-dev
libxslt1-dev wget python-setuptools libssl-dev  
  
RUN apt install -y cmake clang build-essential automake libpcre++-dev bison &&
cd /tmp && git clone https://github.com/swig/swig.git && cd swig &&
./autogen.sh && ./configure --prefix=/usr && make && make install  
  
RUN cd /tmp && mkdir proton && cd proton && wget
https://dist.apache.org/repos/dist/release/qpid/proton/0.16.0/qpid-
proton-0.16.0.tar.gz && tar xzvpf qpid-proton* && \  
cd qpid-proton* && mkdir build && cd build && CXX=clang++ CC=clang cmake
-DCMAKE_CXX_FLAGS=-std=c++11 -DSYSINSTALL_BINDINGS=ON
-DCMAKE_INSTALL_PREFIX=/usr .. && \  
make && make install && rm -rf /tmp/proton  
  
RUN cd /tmp && \  
wget http://ftp.ru.debian.org/debian/pool/main/f/firebird3.0/firebird-
dev_3.0.2.32703.ds4-14_amd64.deb && \  
wget
http://ftp.ru.debian.org/debian/pool/main/f/firebird3.0/libfbclient2_3.0.2.32703.ds4-14_amd64.deb
&& \  
wget
http://ftp.ru.debian.org/debian/pool/main/f/firebird3.0/firebird3.0-common_3.0.2.32703.ds4-14_all.deb
&& \  
wget
http://ftp.ru.debian.org/debian/pool/main/f/firebird3.0/firebird3.0-common-
doc_3.0.2.32703.ds4-14_all.deb && \  
wget
http://ftp.ru.debian.org/debian/pool/main/libt/libtommath/libtommath1_1.0-4_amd64.deb
&& \  
wget
http://ftp.ru.debian.org/debian/pool/main/n/ncurses/libtinfo5_6.0+20171125-1_amd64.deb
&& \  
wget
http://ftp.ru.debian.org/debian/pool/main/n/ncurses/libncurses5_6.0+20171125-1_amd64.deb
&& \  
wget
http://ftp.ru.debian.org/debian/pool/main/n/ncurses/libncursesw5_6.0+20171125-1_amd64.deb
&& \  
wget http://ftp.ru.debian.org/debian/pool/main/f/firebird3.0/libib-
util_3.0.2.32703.ds4-14_amd64.deb && \  
dpkg -i *.deb && rm *.deb && \  
wget http://ftp.ru.debian.org/debian/pool/main/n/ncurses/libtinfo-
dev_6.0+20171125-1_amd64.deb && \  
wget http://ftp.ru.debian.org/debian/pool/main/n/ncurses/ncurses-
bin_6.0+20171125-1_amd64.deb && \  
dpkg -i *.deb && rm *.deb  
  
RUN ln -s /usr/include/ldap.h /usr/lib/x86_64-linux-gnu && \  
ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/ && \  
mkdir /root/sybase && mkdir /root/sybase/include && mkdir /root/sybase/lib &&
\  
ln -s /usr/include/syb*.h /root/sybase/include && \  
ln -s /usr/lib/x86_64-linux-gnu/libsyb* /root/sybase/lib && \  
docker-php-ext-configure pdo_dblib --with-pdo-dblib=/root/sybase && \  
docker-php-ext-configure ldap --with-ldap=/usr/lib/x86_64-linux-gnu && \  
docker-php-ext-configure mysqli --with-mysqli=mysqlnd && \  
docker-php-ext-configure mysql && \  
docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
sed -i 's~;pid.*~pid=/run/php-fpm.pid~ig' /usr/local/etc/php-fpm.conf && \  
cd /root && git clone https://github.com/php-memcached-dev/php-memcached && cd
php-memcached && git checkout REL2_0 && phpize && ./configure --disable-
memcached-sasl && make && make install && echo "extension=memcached.so"
>>/usr/local/etc/php/conf.d/docker-php-ext-memcached.ini && rm -r /root/php-
memcached && \  
cd /root && git clone https://github.com/phpredis/phpredis && cd phpredis &&
phpize && ./configure && make && make install && echo "extension=redis.so"
>>/usr/local/etc/php/conf.d/docker-php-ext-redis.ini && rm -rf /root/phpredis
&& \  
docker-php-ext-install -j4 pdo interbase ctype iconv mcrypt ldap curl
pdo_mysql mysqli soap intl gd gmp bcmath mbstring zip pcntl xsl json phar
pdo_dblib pdo_firebird mysql && \  
echo "zend_extension=opcache.so" >/usr/local/etc/php/conf.d/docker-php-ext-
opcache.ini && \  
echo "extension=phar.so" >/usr/local/etc/php/conf.d/docker-php-ext-phar.ini &&
\  
echo "extension=json.so" >/usr/local/etc/php/conf.d/docker-php-ext-json.ini &&
\  
echo "extension=curl.so" >/usr/local/etc/php/conf.d/docker-php-ext-curl.ini &&
\  
echo "extension=iconv.so" >/usr/local/etc/php/conf.d/docker-php-ext-iconv.ini
&& \  
echo "extension=interbase.so" >/usr/local/etc/php/conf.d/docker-php-ext-
interbase.ini && \  
echo "extension=curl.so" >/usr/local/etc/php/conf.d/docker-php-ext-curl.ini &&
\  
echo "extension=pdo.so" >/usr/local/etc/php/conf.d/docker-php-ext-pdo.ini && \  
echo "extension=pdo_firebird.so" >/usr/local/etc/php/conf.d/docker-php-ext-
pdo_firebird.ini && \  
echo "extension=ctype.so" >/usr/local/etc/php/conf.d/docker-php-ext-ctype.ini
&& \  
echo "extension=mysql.so" >/usr/local/etc/php/conf.d/docker-php-ext-mysql.ini
&& \  
ln -s /usr/local/bin/php /usr/bin/php && \  
mkdir /root/conf.d && mv /usr/local/etc/php/conf.d/proton.ini
/root/conf.d/docker-php-ext-proton.ini && \  
cp -v /usr/local/etc/php/conf.d/* /root/conf.d/ && \  
cd /usr/bin && wget https://getcomposer.org/composer.phar && mv composer.phar
composer && chmod +x composer && \  
wget http://gordalina.github.io/cachetool/downloads/cachetool.phar && mv
cachetool.phar cachetool && chmod +x cachetool && \  
rm -rf /var/lib/apt/lists/* && mkdir -p /run/php && mkdir /var/log/supervisor/
&& /usr/bin/easy_install supervisor && /usr/bin/easy_install supervisor-stdout
&& mkdir /etc/container.run  
#setup php-nginx binding  
ADD fastcgi-php.conf /etc/nginx/snippets/fastcgi-php.conf  
ADD startFPMWithDockerEnvs.sh /usr/local/etc/php/startFPMWithDockerEnvs.sh  
  
ADD php-production.ini /usr/local/etc/php/  
ADD php-development.ini /usr/local/etc/php/  
  
ADD 00-enable_modules /etc/container-run.d/  
ADD 01-apply_environment /etc/container-run.d/  
  
# Supervisor Config  
ADD supervisord.conf /etc/supervisord.conf  
  
#Attach volume to web-root  
VOLUME ["/var/www/html/"]  
  
ENV TIMEZONE GMT  
ENV PHP_MODULES opcache phar json  
ENV DEBUG false  
ENV DEVUSER www-data  
  
EXPOSE 9000  
  
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]  

