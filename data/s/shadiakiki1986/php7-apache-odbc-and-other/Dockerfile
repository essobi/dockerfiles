FROM php:7-apache  
MAINTAINER Shadi Akiki  
  
# use apt-cacher  
# RUN echo "Acquire::http::Proxy \"http://172.17.0.2:3142\";" | tee
/etc/apt/apt.conf.d/01proxy  
# install development packages  
# To avoid prompt for new config: http://stackoverflow.com/a/23048987/4126114  
# Note that for php7, replace  
# * libapache2-mod-php5 with php-mbstring  
# * php5-odbc with php-odbc  
RUN apt-get -qq update > /dev/null && \  
DEBIAN_FRONTEND=noninteractive apt-get -qq -y install \  
curl git libmcrypt-dev libyaml-dev \  
vim unixodbc unixodbc-dev tdsodbc \  
libssl-dev \  
zlib1g-dev \  
wget unzip \  
< /dev/null > /dev/null  
  
# install php extensions  
RUN docker-php-ext-install mcrypt mbstring bcmath > /dev/null  
  
# 2016-11-14 move to yaml-2.0.0 after using yaml-beta from
http://stackoverflow.com/questions/34169346/pecl-yaml  
RUN pecl channel-update pecl.php.net && \  
pecl install \  
zip yaml-2.0.0 mongodb \  
< /dev/null > /dev/null  
  
# 2016-09-xx: no need for yaml since already installed with pecl. What about
mongo and zip?  
# 2016-11-14: despite the note above, the enable below is needed for yaml (as
well as mongo and zip)  
RUN docker-php-ext-enable zip mcrypt mongodb yaml  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer  
  
# cannot install odbc wihtout the below because of https://github.com/docker-
library/php/issues/103#issuecomment-160772802  
RUN set -x \  
&& cd /usr/src/ && tar -xf php.tar.xz && mv php-7* php \  
&& cd /usr/src/php/ext/odbc \  
&& phpize \  
&& sed -ri 's@^ *test +"\$PHP_.*" *= *"no" *&& *PHP_.*=yes *$@#&@g' configure
\  
&& ./configure --with-unixODBC=shared,/usr > /dev/null \  
&& docker-php-ext-install odbc > /dev/null  
  
# install redis extension: note that this is php 7 but it's on debian:jessie,
so cant just apt-get install php-redis  
# Reference: https://anton.logvinenko.name/en/blog/how-to-install-redis-and-
redis-php-client.html  
# scroll down to section on php 7  
# also  
# https://github.com/docker-library/php/issues/263#issuecomment-233280040  
RUN cd /tmp && \  
wget --quiet https://github.com/phpredis/phpredis/archive/php7.zip -O
phpredis.zip && \  
unzip -q -o /tmp/phpredis.zip && mv /tmp/phpredis-* /usr/src/php/ext/redis &&
\  
cd /usr/src/php/ext/redis && \  
phpize && ./configure > /dev/null && \  
docker-php-ext-install redis > /dev/null  
  
# check that redis indeed got installed  
RUN php -r "if (new Redis() == true){ echo \"OK \r\n\"; }"  
  
# Install php sockets extension  
RUN docker-php-ext-install sockets > /dev/null  
  
# check that all were indeed installed  
RUN php -i|grep mongo \  
&& php -i | grep zip \  
&& php -i | grep odbc \  
&& php -i | grep redis \  
&& php -i | grep sockets \  
&& php -i | grep yaml  
  
# Fix timezone: http://serverfault.com/a/683651  
ENV TZ=Asia/Beirut  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# make the composer cache into a shared volume for persistence and sharing
among derived images  
VOLUME /root/.composer/cache  

