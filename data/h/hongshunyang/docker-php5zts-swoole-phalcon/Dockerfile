FROM hongshunyang/docker-php5zts  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
## support swoole - 2.0.7  
## support phalcon - 3.0.4  
ENV SWOOLE_VERSION 2.0.7  
ENV CPHALCON_VERSION 3.1.1  
ENV CPHALCON_DOWNLOAD_URL
https://github.com/phalcon/cphalcon/archive/v$CPHALCON_VERSION.tar.gz  
  
RUN apk add -U --virtual build-deps autoconf build-base linux-headers git \  
&& pecl install swoole-$SWOOLE_VERSION \  
&& cd /tmp/ \  
&& wget -qO- $CPHALCON_DOWNLOAD_URL | tar xvz \  
&& cd cphalcon-$CPHALCON_VERSION/build/ \  
&& ./install \  
&& cd ~ \  
&& rm -rf /tmp/* \  
&& apk del -U build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN echo "extension=swoole.so" > /etc/php5/conf.d/swoole.ini  
RUN echo "extension=phalcon.so" > /etc/php5/conf.d/phalcon.ini  
  
COPY tmpl/_etc_php5_php-fpm.conf.tmpl /etc/php5/php-fpm.conf.tmpl  
  
RUN dockerize -template "/etc/php5/php-fpm.conf.tmpl:/etc/php5/php-fpm.conf"  
  

