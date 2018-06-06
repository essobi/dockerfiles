FROM php:7.1  
RUN echo "127.0.0.1 mysql" >> /etc/hosts \  
&& apt-get update \  
&& apt-get install -y unzip zlib1g-dev git \  
&& docker-php-ext-install pdo pdo_mysql zip \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Node  
ENV NPM_CONFIG_LOGLEVEL notice  
ENV NODE_VERSION 8.9.1  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV SYMFONY_ENV prod  
ENV LIBVIPS_VERSION_MAJOR 8  
ENV LIBVIPS_VERSION_MINOR 5  
ENV LIBVIPS_VERSION_PATCH 8  
ENV LIBVIPS_VERSION
$LIBVIPS_VERSION_MAJOR.$LIBVIPS_VERSION_MINOR.$LIBVIPS_VERSION_PATCH  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Install PHP extensions  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
pkg-config \  
imagemagick \  
libmcrypt-dev \  
libmagickwand-dev \  
libcurl4-openssl-dev \  
automake \  
build-essential \  
curl \  
gobject-introspection \  
gtk-doc-tools \  
libglib2.0-dev \  
libturbojpeg1-dev \  
libpng12-dev \  
libwebp-dev \  
libtiff5-dev \  
libgif-dev \  
libexif-dev \  
libxml2-dev \  
libpoppler-glib-dev \  
swig \  
libmagickwand-dev \  
libpango1.0-dev \  
libmatio-dev \  
libopenslide-dev \  
libcfitsio3-dev \  
libgsf-1-dev \  
fftw3-dev \  
liborc-0.4-dev \  
librsvg2-dev  
  
# Build libvips  
RUN cd /tmp \  
&& curl -L -O
https://github.com/jcupitt/libvips/releases/download/v$LIBVIPS_VERSION/vips-$LIBVIPS_VERSION.tar.gz
\  
&& tar zxvf vips-$LIBVIPS_VERSION.tar.gz \  
&& cd /tmp/vips-$LIBVIPS_VERSION \  
&& ./configure --enable-debug=no --without-python $1 \  
&& make \  
&& make install \  
&& ldconfig \  
&& apt-get remove -y automake build-essential \  
&& apt-get autoremove -y \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pecl install imagick vips \  
&& echo "extension=vips.so" > /usr/local/etc/php/conf.d/vips.ini \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-enable imagick \  
&& rm -rf /tmp/pear \  
&& npm install uglify-js -g \  
&& npm install less -g  
  
RUN echo "opcache.load_comments = On" >> /usr/local/etc/php/conf.d/docker-php-
ext-opcache.ini  
  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data

