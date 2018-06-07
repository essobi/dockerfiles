#
http://dockerfile.readthedocs.io/en/latest/content/DockerImages/dockerfiles/php-
nginx.html  
  
FROM webdevops/php-nginx:7.1  
  
ENV ICU_DATA=/opt/icu/icudt52l  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y libjpeg-dev \  
libfreetype6-dev \  
libmagickwand-dev \  
libicu-dev \  
ffmpeg \  
pkg-config \  
autoconf \  
g++ \  
make \  
openssl \  
libsasl2-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
\--no-install-recommends  
  
RUN mkdir -p /opt/icu/icudt52l && \  
curl -o /opt/icu/icudt52l/metaZones.res \  
http://source.icu-
project.org/repos/icu/data/trunk/tzdata/icunew/2016f/44/le/metaZones.res && \  
curl -o /opt/icu/icudt52l/timezoneTypes.res \  
http://source.icu-
project.org/repos/icu/data/trunk/tzdata/icunew/2016f/44/le/timezoneTypes.res
&& \  
curl -o /opt/icu/icudt52l/windowsZones.res \  
http://source.icu-
project.org/repos/icu/data/trunk/tzdata/icunew/2016f/44/le/windowsZones.res &&
\  
curl -o /opt/icu/icudt52l/zoneinfo64.res \  
http://source.icu-
project.org/repos/icu/data/trunk/tzdata/icunew/2016f/44/le/zoneinfo64.res  
  
RUN docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install -j$(nproc) iconv \  
&& docker-php-ext-install xml \  
&& docker-php-ext-install intl \  
&& pecl install timezonedb \  
&& echo "extension=timezonedb.so" > /usr/local/etc/php/conf.d/timezonedb.ini \  
&& pecl install mongodb \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/ext-mongo.ini  
  
RUN apt-get purge -y -f --force-yes \  
libjpeg-dev \  
libicu-dev \  
libsasl2-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
&& docker-image-cleanup

