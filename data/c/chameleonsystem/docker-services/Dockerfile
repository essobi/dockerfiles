FROM php:7.1-fpm  
  
# Adding some basic stuff to make chameleon run  
RUN apt-get update && apt-get install -y \  
aspell \  
aspell-de \  
freetds-dev \  
libmemcached-dev \  
libtidy-dev \  
zlib1g-dev \  
git  
  
RUN git clone -b php7 --single-branch https://github.com/php-memcached-
dev/php-memcached.git \  
&& ( \  
cd php-memcached \  
&& phpize \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& rm -rf php-memcached \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/ \  
&& docker-php-ext-enable memcached \  
&& docker-php-ext-install -j$(nproc) opcache iconv mbstring pdo_mysql
pdo_dblib tidy  
  
# Adding layer for imagemagick. This adds A LOT of extra payload to this
docker.  
# Remove it if you don't need it  
RUN apt-get update && apt-get install -y \  
imagemagick libmagickwand-dev libmagickcore-dev jpegoptim optipng pngquant
libcurl3-dev libicu-dev \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd soap zip opcache bcmath sockets curl
intl mysqli  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove  
  
# pre-installing blackfire  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp  
  
# installing blackfire cli  
RUN mkdir -p /tmp/blackfire \  
&& curl -A "Docker" -L
https://blackfire.io/api/v1/releases/client/linux_static/amd64 | tar zxp -C
/tmp/blackfire \  
&& mv /tmp/blackfire/blackfire /usr/bin/blackfire \  
&& rm -Rf /tmp/blackfire  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/proxy.conf /usr/local/etc/php-fpm.d/  
  
COPY config/patchpanel.sh /  
COPY tools /usr/local/bin/tools  
  
RUN chmod 755 /patchpanel.sh  
  
# workaround: symlinking /usr/bin/php as it's expected in that location by
some scripts  
RUN ln -s /usr/local/bin/php /usr/bin/php  
  
WORKDIR /usr/local/apache2/htdocs/customer  
  
ENTRYPOINT [ "/patchpanel.sh" ]  
CMD [ "php-fpm" ]  

