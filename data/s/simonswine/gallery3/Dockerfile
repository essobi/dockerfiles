FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get install -y \  
apache2 \  
libapache2-mod-php5 \  
curl \  
php5-mysql \  
imagemagick \  
graphicsmagick \  
dcraw && \  
apt-get clean autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV VERSION_GALLERY3 3.0.9  
ENV VERSION_CONTRIB b97f3d3b564f54947c5b04b78b9d3bc54cc64d15  
ENV VERSION_PROGRESS e641a1f454ba17a6fe81def9ea054f75229da26b  
RUN \  
rm -rf /var/www/* && \  
curl -L https://github.com/gallery/gallery3/archive/${VERSION_GALLERY3}.tar.gz
| \  
tar xzf - -C /var/www --strip-components=1 && \  
curl -L
https://github.com/gallery/gallery3-contrib/archive/${VERSION_CONTRIB}.tar.gz
| \  
tar xzf - gallery3-contrib-${VERSION_CONTRIB}/3.0/modules -C /var/www --strip-
components=2 && \  
curl -L
https://github.com/mstoltenburg/html5_upload_progress/archive/${VERSION_PROGRESS}.tar.gz
| \  
tar xzf - -C /var/www/modules --strip-components=1 && \  
chown -R www-data:www-data /var/www/  
  
RUN a2enmod rewrite  
RUN a2enmod expires  
ADD /apache-default /etc/apache2/sites-available/000-default.conf  
  
ADD htaccess /var/www/.htaccess  
ADD php.ini /etc/php5/apache2/php.ini  
  
VOLUME ["/var/www/var"]  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

