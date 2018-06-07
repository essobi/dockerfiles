FROM debian:wheezy  
MAINTAINER Tom Hill <tom@greensheep.io>  
  
# Install packages  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
autoconf \  
automake \  
libtool \  
re2c \  
flex \  
bison \  
build-essential \  
wget \  
libgd2-xpm-dev \  
mcrypt \  
libmcrypt-dev \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libgif-dev \  
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
  
# Add libraries  
ADD ./lib /home/lib  
# WebP (newer than provided by apt-get)  
WORKDIR /home/lib/libwebp-0.4.2  
RUN tar xvzf libwebp-0.4.2.tar.gz \  
&& cd libwebp-0.4.2 \  
&& ./configure \  
&& make \  
&& make install  
  
# ImageMagick  
WORKDIR /home/lib/ImageMagick-6.9.0-0  
RUN tar xvzf ImageMagick-6.9.0-0.tar.gz \  
&& cd ImageMagick-6.9.0-0 \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig /usr/local/lib  
  
RUN rm -rf /var/lib/apt/lists/*  
# Build and install PHP / PHP-FPM  
WORKDIR /home/lib/php-5.5  
RUN tar -xvf php-5.5.18.tar.gz  
WORKDIR /home/lib/php-5.5/php-5.5.18  
RUN ./configure \  
\--enable-fpm \  
\--with-config-file-path=/etc/php5 \  
\--with-mysql \  
\--with-mysqli \  
\--with-zlib \  
\--with-jpeg-dir \  
\--with-gd \  
\--with-freetype-dir \  
\--with-curl \  
\--with-openssl \  
\--with-pdo-mysql \  
\--with-mcrypt \  
\--enable-zip  
RUN make clean  
RUN make  
RUN make install  
RUN cp sapi/fpm/php-fpm /usr/local/bin  
  
# PHP config files  
ADD ./conf/php/php.ini /etc/php5/php.ini  
ADD ./conf/php/php-fpm.conf /usr/local/etc/php-fpm.conf  
  
# Install php-fpm init script  
RUN cp sapi/fpm/init.d.php-fpm.in /etc/init.d/php-fpm \  
&& chmod 755 /etc/init.d/php-fpm \  
&& sed -i "s/php_fpm_BIN=@sbindir@/php_fpm_BIN=\/usr\/local\/bin/g"
/etc/init.d/php-fpm \  
&& sed -i "s/php_fpm_CONF=@sysconfdir@/php_fpm_CONF=\/usr\/local\/etc/g"
/etc/init.d/php-fpm \  
&& sed -i "s/php_fpm_PID=@localstatedir@/php_fpm_PID=\/var/g" /etc/init.d/php-
fpm  
  
# ImageMagick pecl extension  
RUN pear config-set php_ini /etc/php5/php.ini \  
&& pecl config-set php_ini /etc/php5/php.ini  
WORKDIR /home/lib/pecl-extensions  
RUN tar xvzf imagick-3.1.2.tgz \  
&& cd imagick-3.1.2 \  
&& phpize \  
&& ./configure --with-imagick=/usr/bin/convert \  
&& make \  
&& make install  
  
# Clean up  
WORKDIR /home  
RUN rm -rf ./*  

