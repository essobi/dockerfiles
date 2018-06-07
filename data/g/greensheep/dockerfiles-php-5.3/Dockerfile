FROM ubuntu:14.04  
MAINTAINER Tom Hill <tom@greensheep.io>  
  
# Add libraries directory  
ADD ./lib /home/lib  
  
##########################  
## INSTALL DEPENDENCIES ##  
##########################  
  
# Install packages  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
autoconf \  
build-essential \  
imagemagick \  
libgd3 \  
libgd-dev \  
mcrypt \  
libmcrypt-dev \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
zlib1g-dev  
  
# Build and install PHP  
WORKDIR /home/lib/php-5.3  
RUN tar -xvf php-5.3.29.tar.gz  
WORKDIR /home/lib/php-5.3/php-5.3.29  
RUN ./configure --enable-fpm --with-mysql --with-mysqli --with-zlib --with-
jpeg-dir --with-gd --with-freetype-dir --with-curl --with-openssl --with-pdo-
mysql --with-mcrypt  
RUN make clean  
RUN make  
RUN make install  
RUN cp sapi/fpm/php-fpm /usr/local/bin  
  
###############  
## CONFIGURE ##  
###############  
  
# PHP config files  
ADD ./conf/php/php.ini /usr/local/php/php.ini  
ADD ./conf/php/php-fpm.conf /usr/local/etc/php-fpm.conf  

