FROM php:7.1.3-fpm  
  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
MAINTAINER Mark Schenzle <markseisler@gmail.com>  
  
WORKDIR "/"  
  
COPY start.sh /start.sh  
  
# composer  
COPY composer/composer /usr/local/bin/composer  
  
# extra packages  
RUN echo "\nexport TERM=xterm" >> /etc/bash.bashrc \  
&& apt-get update && apt-get install -y --no-install-recommends \  
apt-utils  
  
RUN echo '\n\  
deb http://packages.dotdeb.org jessie all\n\  
deb-src http://packages.dotdeb.org jessie all\n'\  
>> /etc/apt/sources.list  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 7E3F070089DF5277 \  
&& apt-get update && apt-get install -y --no-install-recommends \  
zip \  
unzip \  
git-core \  
vim \  
telnet \  
tar \  
&& rm -rf /var/lib/apt/lists/*  
  
# xdebug installation  
COPY xdebug/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
COPY xdebug/xdebug-2.5.3.tgz /xdebug-2.5.3.tgz  
RUN tar -xf /xdebug-2.5.3.tgz \  
&& cd xdebug-2.5.3 \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& rm -rf xdebug-2.5.3 \  
/xdebug-2.5.3 \  
/xdebug-2.5.3.tgz  
  
EXPOSE 9000  
CMD ["/start.sh"]  

