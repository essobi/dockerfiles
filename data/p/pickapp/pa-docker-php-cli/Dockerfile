FROM php:7.1-alpine  
MAINTAINER Adam Wallner <wallner@bitbaro.hu>  
  
RUN apk \--no-cache add openssl \  
&& apk add \--no-cache \  
#--repository http://dl-cdn.alpinelinux.org/alpine/edge/main\  
# Needed libs  
libgcc libpng libjpeg-turbo libwebp libmcrypt gettext fontconfig lcms2 libltdl
libpng tiff libwebp zlib fftw \  
# Install build packages temporarily  
${PHPIZE_DEPS} git libtool libmcrypt-dev openssl-dev libpng-dev libjpeg-turbo-
dev libwebp-dev gettext-dev freetype-dev fontconfig-dev ghostscript-dev tiff-
dev lcms2-dev fftw-dev \  
  
# Install newer imagemagick (7.0.5-6)  
&& mkdir -p /src/dest && cd /src \  
&& wget http://www.imagemagick.org/download/ImageMagick-7.0.5-6.tar.gz \  
&& tar -xzvf ImageMagick-7.0.5-6.tar.gz && cd ImageMagick-7.0.5-6 \  
&& export CPU=`cat /proc/cpuinfo | grep -c processor` \  
&& ./configure \  
\--enable-shared \  
\--disable-static \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--disable-docs \  
\--disable-hdri \  
\--without-x \  
\--with-tiff \  
\--with-lcms2 \  
\--with-gslib \  
\--without-perl \  
\--without-fpx \  
\--without-wmf \  
\--without-gvc \  
\--without-rsvg \  
\--without-lqr \  
\--without-pango \  
\--with-gs-font-dir=/usr/share/fonts/Type1 \  
\--with-modules \  
&& make -j${CPU} && make DESTDIR="/src/dest" -j${CPU} install \  
&& find "/src/dest" -name '.packlist' -o -name 'perllocal.pod' -o -name '*.bs'
-delete \  
&& cp -R /src/dest/* / \  
&& rm -rf /src \  
  
# Extract PHP sources install deps  
&& docker-php-source extract \  
  
# Install extensions from PECL  
&& pecl update-channels \  
&& pecl install xdebug mongodb channel://pecl.php.net/Weakref-0.3.3 \  
# We need to select prefix for imagemagick  
&& printf "\n" | pecl install imagick \  
# Install the following packages from PHP source (inside image)  
&& docker-php-ext-install gd gettext mcrypt mysqli opcache pcntl pdo_mysql
sockets \  
&& docker-php-ext-enable gd.so gettext.so imagick.so mcrypt.so mysqli.so
opcache.so pcntl.so pdo_mysql.so sockets.so weakref.so xdebug.so mongodb.so \  
  
# Clean unnecessare packages  
&& apk del ${PHPIZE_DEPS} git libtool libmcrypt-dev openssl-dev libpng-dev
libjpeg-turbo-dev libmcrypt-dev libwebp-dev gettext-dev freetype-dev
fontconfig-dev ghostscript-dev tiff-dev lcms2-dev fftw-dev \  
  
# Clean PHP sources  
&& docker-php-source delete \  
  
# Create opcache dir  
&& mkdir -p /var/www/.opcache && chown www-data:www-data /var/www/.opcache  

