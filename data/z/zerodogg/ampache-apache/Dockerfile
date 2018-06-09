FROM php:7.1-apache-stretch  
MAINTAINER zerodogg  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install wget inotify-tools sudo
gnupg2  
  
RUN echo 'deb http://download.videolan.org/pub/debian/stable/ /' >>
/etc/apt/sources.list ;\  
echo 'deb-src http://download.videolan.org/pub/debian/stable/ /' >>
/etc/apt/sources.list  
  
RUN wget -O - https://download.videolan.org/pub/debian/videolan-apt.asc|sudo
apt-key add - && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install pwgen lame libvorbis-dev
vorbis-tools flac libmp3lame-dev libavcodec-extra* libtheora-dev libvpx-dev
libav-tools git libpng-dev libjpeg-dev libfreetype6-dev  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr --with-png-dir=/usr
--with-jpeg-dir=/usr; \  
docker-php-ext-install pdo_mysql gd  
  
# Install composer for dependency management  
RUN php -r "readfile('https://getcomposer.org/installer');" | php && \  
mv composer.phar /usr/local/bin/composer  
  
ADD https://github.com/ampache/ampache/archive/master.tar.gz /opt/ampache-
master.tar.gz  
ADD ampache.cfg.php.dist /var/temp/ampache.cfg.php.dist  
  
# extraction / installation  
RUN rm -rf /var/www/html/* && \  
tar -C /var/www/html/ -xf /opt/ampache-master.tar.gz ampache-master --strip=1
&& \  
chown -R www-data /var/www/html/ && \  
cd /var/www/html && sudo -u www-data composer install --prefer-source --no-
interaction && \  
chown -R www-data /var/www/html  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
VOLUME ["/media"]  
VOLUME ["/var/www/html/config"]  
VOLUME ["/var/www/html/themes"]  
EXPOSE 80  
CMD ["/run.sh"]  

