FROM buildpack-deps:jessie  
MAINTAINER halito! <devs@halito.com>  
#Credits to Eugene Ware <eugene@noblesamurai.com> and Ignacio Flores
<ignacio@introbay.com>  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -r /var/lib/apt/lists/*  
  
##<apache2>##  
RUN apt-get update \  
&& apt-get install -y apache2-bin apache2-dev apache2.2-common --no-install-
recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /var/www/html \  
&& mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html
\  
&& chown -R www-data:www-data /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event \  
&& a2enmod mpm_prefork  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist  
COPY apache2.conf /etc/apache2/apache2.conf  
##</apache2>##  
# compile openssl, otherwise --with-openssl won't work  
RUN CFLAGS="-fPIC" \  
&& OPENSSL_VERSION="1.0.2d" \  
&& cd /tmp \  
&& mkdir openssl \  
&& curl -sL "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz"
-o openssl.tar.gz \  
&& curl -sL
"https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz.asc" -o
openssl.tar.gz.asc \  
&& tar -xzf openssl.tar.gz -C openssl --strip-components=1 \  
&& cd /tmp/openssl \  
&& ./config shared && make && make install \  
&& rm -rf /tmp/*  
  
ENV PHP_VERSION 5.3.29  
ENV PHP_INI_DIR /usr/local/lib  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
# php 5.3 needs older autoconf  
RUN set -x \  
&& apt-get update && apt-get install -y autoconf2.13 && rm -r
/var/lib/apt/lists/* \  
&& curl -SLO http://launchpadlibrarian.net/140087283/libbison-
dev_2.7.1.dfsg-1_amd64.deb \  
&& curl -SLO
http://launchpadlibrarian.net/140087282/bison_2.7.1.dfsg-1_amd64.deb \  
&& dpkg -i libbison-dev_2.7.1.dfsg-1_amd64.deb \  
&& dpkg -i bison_2.7.1.dfsg-1_amd64.deb \  
&& rm *.deb \  
&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2/from/this/mirror" -o
php.tar.bz2 \  
&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2.asc/from/this/mirror"
-o php.tar.bz2.asc \  
&& mkdir -p /usr/src/php \  
&& tar -xf php.tar.bz2 -C /usr/src/php --strip-components=1 \  
&& rm php.tar.bz2* \  
&& cd /usr/src/php \  
&& ./buildconf --force \  
&& ./configure --disable-cgi \  
$(command -v apxs2 > /dev/null 2>&1 && echo '--with-apxs2' || true) \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--with-mysql \  
\--with-mysqli \  
\--with-pdo-mysql \  
\--with-openssl=/usr/local/ssl \  
&& make -j"$(nproc)" \  
&& make install \  
&& dpkg -r bison libbison-dev \  
&& apt-get purge -y --auto-remove autoconf2.13 \  
&& make clean  
  
COPY docker-php-* /usr/local/bin/  
COPY apache2-foreground /usr/local/bin/  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev libpq-dev zip \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql zip  
  
# install git, zip  
RUN apt-get update && apt-get install -y git zip \  
&& rm -rf /var/lib/apt/lists/*  
  
## Dev configuration  
RUN pecl install -o -f xdebug-2.2.7 \  
&& docker-php-ext-enable xdebug  
  
COPY x-error.ini $PHP_INI_DIR/conf.d/  
COPY xdebug.ini $PHP_INI_DIR/conf.d/  
  
ENV COMPOSER_HOME /root/composer  
ENV COMPOSER_VERSION master  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
CMD ["apache2-foreground"]  

