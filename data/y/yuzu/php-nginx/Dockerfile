FROM php:7.0-fpm  
COPY . /src  
RUN \  
curl -L -s http://apt.vixns.net/vixns.gpg | apt-key add - && \  
echo "deb http://apt.vixns.net jessie contrib non-free main" >>
/etc/apt/sources.list && \  
echo "deb http://http.debian.net/debian jessie-backports contrib non-free
main" >> /etc/apt/sources.list && \  
apt-get update && apt-get \--no-install-recommends -t jessie-backports -y
dist-upgrade && \  
apt-get install \--no-install-recommends -t jessie-backports -y ca-
certificates nginx runit file re2c libicu-dev zlib1g-dev libmcrypt-dev
libmagickcore-dev libmagickwand-dev libmagick++-dev libjpeg-dev libpng12-dev
libicu52 libmcrypt4 g++ imagemagick git libssl-dev xfonts-base xfonts-75dpi
libfreetype6-dev && \  
mkdir -p /usr/local/etc/php-fpm.d && \  
docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/lib && docker-php-ext-install sockets intl zip mbstring mcrypt gd &&
\  
pecl install imagick-beta && \  
echo "extension=imagick.so" >> "/usr/local/etc/php/conf.d/ext-imagick.ini" &&
\  
echo "date.timezone=UTC" >> "/usr/local/etc/php/conf.d/timezone.ini" && \  
echo "zend_extension=opcache.so" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.enable_cli=1" >> "/usr/local/etc/php/conf.d/ext-opcache.ini" &&
\  
echo "opcache.memory_consumption=128" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.interned_strings_buffer=8" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.max_accelerated_files=4000" >> "/usr/local/etc/php/conf.d/ext-
opcache.ini" && \  
echo "opcache.fast_shutdown=1" >> "/usr/local/etc/php/conf.d/ext-opcache.ini"
&& \  
curl -sS https://getcomposer.org/installer | php -- \--install-
dir=/usr/local/bin \--filename=composer && \  
ln -sf /proc/1/fd/1 /var/log/nginx/access.log && \  
ln -sf /proc/1/fd/2 /var/log/nginx/error.log && \  
rm /usr/local/etc/php-fpm.d/*conf && \  
dpkg \--purge libicu-dev libmagickcore-dev libmagickwand-dev libmagick++-dev
libfreetype6-dev libmagickcore-6.q16-dev libgraphviz-dev libglib2.0-dev
libtiff5-dev libwmf-dev libcairo2-dev libgdk-pixbuf2.0-dev libfontconfig1-dev
librsvg2-dev libmagickwand-6.q16-dev libmagick++-6.q16-dev && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /etc/service/php-fpm/ && \  
mkdir -p /etc/service/nginx/ && \  
mv /src/policy.xml /etc/ImageMagick-6/policy.xml && \  
mv /src/nginx.conf /etc/nginx/nginx.conf && \  
mv /src/php-fpm.conf /usr/local/etc/php-fpm.conf && \  
mv /src/www.conf /usr/local/etc/php-fpm.d/www.conf && \  
mv /src/php-fpm.sh /etc/service/php-fpm/run && \  
mv /src/nginx.sh /etc/service/nginx/run && \  
mv /src/runsvdir-start.sh /sbin/runsvdir-start && \  
rm -rf /src  
  
EXPOSE 80  
  
CMD ["/sbin/runsvdir-start"]  

