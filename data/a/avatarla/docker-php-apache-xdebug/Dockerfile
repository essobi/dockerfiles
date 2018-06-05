FROM webdevops/php-apache:ubuntu-14.04  
  
MAINTAINER Pedro Mintt <enrique.garrido@avatarla.com>  
  
  
ENV XDEBUG_VERSION 2.2.7  
ENV XDEBUG_MD5 71a6b75885207e79762e1e7aaf5c3993  
  
  
RUN set -x \  
&& curl -SL "http://www.xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz" -o
xdebug.tgz \  
&& echo $XDEBUG_MD5 xdebug.tgz | md5sum -c - \  
&& mkdir -p /usr/src/xdebug \  
&& tar -xf xdebug.tgz -C /usr/src/xdebug --strip-components=1 \  
&& rm xdebug.* \  
&& cd /usr/src/xdebug \  
&& phpize \  
&& ./configure \  
&& make -j"$(nproc)" \  
&& make install \  
&& make clean  
  
COPY ext-xdebug.ini /usr/local/etc/php/conf.d/  
  

