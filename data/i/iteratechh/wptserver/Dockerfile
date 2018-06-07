FROM php:5.6-apache  
MAINTAINER Hauke Mettendorf <hauke.mettendorf@iteratec.de>  
  
ENV PATH=$PATH:/scripts  
  
RUN echo deb http://www.deb-multimedia.org jessie main non-free >>
/etc/apt/sources.list && \  
apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y --force-yes \  
deb-multimedia-keyring \  
imagemagick \  
libjpeg-progs \  
exiftool \  
unzip \  
wget \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libcurl4-openssl-dev \  
python \  
python-pillow  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y --force-yes\  
ffmpeg && \  
apt-get clean && \  
apt-get autoclean  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
docker-php-ext-install zip && \  
docker-php-ext-install curl && \  
a2enmod expires headers rewrite  
  
RUN apt-get install -y libmagickwand-6.q16-dev --no-install-recommends && \  
ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin && \  
pecl install imagick && \  
echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini  
  
RUN cd /tmp && \  
wget https://github.com/iteratec-hh/webpagetest/archive/multistep.zip && \  
unzip multistep.zip && \  
cd webpagetest-multistep && \  
cp -a www/. /var/www/html && \  
rm -rf /tmp/* && \  
chown -R www-data:www-data /var/www/html && \  
cd /var/www/html && \  
chmod 0777 dat && \  
chmod 0777 -R work && \  
chmod 0777 logs && \  
mkdir -p results && \  
chmod 0777 -R results  
  
RUN cd /var/www/html/settings && \  
mv settings.ini.sample settings.ini && \  
mv connectivity.ini.sample connectivity.ini  
  
COPY config/locations.ini /var/www/html/settings/locations.ini  
  
COPY config/php.ini /usr/local/etc/php/  
  
COPY config/apache2.conf /etc/apache2/apache2.conf  
  
COPY config/crontab /etc/crontab  
  
# Install and config supervisor  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config/supervisord/supervisord_apache.conf
/etc/supervisor/conf.d/supervisord_apache.conf  
COPY config/supervisord/supervisord_cron.conf
/etc/supervisor/conf.d/supervisord_cron.conf  
  
# Create script directory  
RUN mkdir -p /scripts/settings  
  
# Copy scripts  
COPY scripts/migrate-settings /scripts/migrate-settings  
COPY scripts/start_archiving.sh /scripts/start_archiving.sh  
  
# Set execution bit  
RUN chmod +x /scripts/migrate-settings  
RUN chmod +x /scripts/start_archiving.sh  
  
VOLUME /var/www/html/settings  
VOLUME /var/www/html/results  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord"]  

