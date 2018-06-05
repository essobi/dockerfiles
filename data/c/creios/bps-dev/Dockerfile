# CHOSING DEBIAN  
FROM debian:8  
MAINTAINER Tim Tegeler <tegeler@creios.net>  
  
## SETTING ENVIRONMENT  
ENV ENVIRONMENT docker-dev  
  
# APT-GET  
RUN apt-get -qq update && \  
apt-get install -y \  
apache2 \  
git \  
libmagickwand-dev \  
links \  
make \  
openssh-client \  
php-pear \  
php5 \  
php5-dev \  
php5-gd \  
php5-mysql \  
php5-xdebug \  
php5-intl \  
php5-gmp \  
php5-curl \  
pkg-config \  
wget  
  
## APACHE  
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf && \  
a2ensite 000-default && \  
a2enmod rewrite && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
## PHP  
RUN echo "xdebug.remote_enable=true" >> /etc/php5/apache2/conf.d/20-xdebug.ini
&& \  
echo "xdebug.remote_connect_back=true" >>
/etc/php5/apache2/conf.d/20-xdebug.ini && \  
echo "xdebug.profiler_enable=true" >> /etc/php5/apache2/conf.d/20-xdebug.ini
&& \  
echo "xdebug.profiler_enable_trigger=true" >>
/etc/php5/apache2/conf.d/20-xdebug.ini && \  
echo "xdebug.profiler_output_dir=/var/www/profiling" >>
/etc/php5/apache2/conf.d/20-xdebug.ini && \  
pecl install imagick && \  
echo 'extension=imagick.so' >> /etc/php5/apache2/conf.d/imagick.ini && \  
echo 'extension=imagick.so' >> /etc/php5/cli/conf.d/imagick.ini && \  
pecl install gender && \  
echo 'extension=gender.so' >> /etc/php5/apache2/conf.d/imagick.ini && \  
echo 'extension=gender.so' >> /etc/php5/cli/conf.d/imagick.ini && \  
sed -i "s/error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT/error_reporting
= E_ALL/" /etc/php5/apache2/php.ini && \  
sed -i "s/display_errors = Off/display_errors = On/" /etc/php5/apache2/php.ini
&& \  
sed -i "s/display_startup_errors = Off/display_startup_errors = On/"
/etc/php5/apache2/php.ini && \  
sed -i "s/post_max_size = 8M/post_max_size = 100M/" /etc/php5/apache2/php.ini
&& \  
sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 100M/"
/etc/php5/apache2/php.ini && \  
sed -i "s/;always_populate_raw_post_data = -1/always_populate_raw_post_data =
-1/" /etc/php5/apache2/php.ini  
  
## PDFLib  
RUN wget -O /tmp/pdflib.tar.gz
"http://www.pdflib.com/binaries/PDFlib/904/PDFlib-9.0.4-Linux-x86_64-php.tar.gz"
&& \  
tar -zxf /tmp/pdflib.tar.gz -C /tmp
"PDFlib-9.0.4-Linux-x86_64-php/bind/php/php-560/php_pdflib.so" && \  
mv "/tmp/PDFlib-9.0.4-Linux-x86_64-php/bind/php/php-560/php_pdflib.so" "$(php
-r 'echo ini_get("extension_dir");')/" && \  
rm -rf "/tmp/PDFlib-9.0.4-Linux-x86_64-php" && \  
echo 'extension=php_pdflib.so' > /etc/php5/apache2/conf.d/pdflib.ini && \  
echo 'extension=php_pdflib.so' > /etc/php5/cli/conf.d/pdflib.ini  
  
## CI  
RUN mkdir ~/.ssh && \  
printf 'Host *\n\tStrictHostKeyChecking no\n\n' > ~/.ssh/config  
  
## Composer  
COPY install-composer.sh .  
RUN ./install-composer.sh && \  
rm install-composer.sh  
  
WORKDIR /var/www  
  
EXPOSE 80  
COPY httpd-foreground /usr/local/bin/  
CMD ["httpd-foreground"]  

