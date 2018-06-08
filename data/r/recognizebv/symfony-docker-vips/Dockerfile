FROM recognizebv/symfony-docker:php7-dev  
  
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
zlib1g-dev \  
libfreetype6-dev \  
pkg-config \  
imagemagick \  
libmagickwand-dev \  
libcurl4-openssl-dev \  
automake \  
build-essential \  
curl \  
gobject-introspection \  
gtk-doc-tools \  
libglib2.0-dev \  
libturbojpeg-dev \  
libpng-dev \  
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
libcfitsio-dev \  
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
&& docker-php-ext-enable imagick \  
&& rm -rf /tmp/pear \  
&& npm install uglify-js -g \  
&& npm install less -g  
  
RUN echo "opcache.load_comments = On" >> /usr/local/etc/php/conf.d/docker-php-
ext-opcache.ini  
  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  

